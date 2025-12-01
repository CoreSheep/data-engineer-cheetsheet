import re
from typing import Optional
from datetime import datetime, timezone

COUNTRY_CODES = {
    "us": "United States", "usa": "United States",
    "gb": "United Kingdom", "gbr": "United Kingdom",
    "ca": "Canada", "can": "Canada",
    "fr": "France", "fra": "France",
    "de": "Germany", "deu": "Germany",
    "cn": "China", "chn": "China",
    "in": "India", "ind": "India",
    "jp": "Japan", "jpn": "Japan",
    "ru": "Russia", "rus": "Russia",
    "kr": "South Korea", "kor": "South Korea",
    "kp": "North Korea", "prk": "North Korea",
    "br": "Brazil", "bra": "Brazil",
    "ci": "Côte d'Ivoire", "civ": "Côte d'Ivoire",
    "ae": "United Arab Emirates", "are": "United Arab Emirates",
    # ....

}

# ------------------- NORMALIZATION -------------------

def normalize_company_name(name: str) -> str:
    return name.strip()

def normalize_country(name: str) -> str:
    clean = name.strip().lower()
    return COUNTRY_CODES.get(clean, name.strip().title())

def normalize_city(city: str) -> str:
    def title_word(w):
        return "-".join([p.capitalize() for p in w.split("-")])
    return " ".join([title_word(w) for w in city.strip().split()])

def normalize_ceo_name(name: str) -> str:
    titles = {"mr", "mrs", "ms", "dr", "prof"}
    parts = name.strip().split()
    filtered = [p for p in parts if p.lower().replace(".", "") not in titles]
    lowercase_particles = {"de", "da", "van", "von", "bin"}
    final = [p.capitalize() if p.lower() not in lowercase_particles else p.lower() for p in filtered]
    return " ".join(final)

def normalize_revenue(value: int) -> int:
    return round(value, 0)

# ------------------- VALIDATION -------------------

def validate_revenue(value):
    if isinstance(value, (int, float)):
        if value <= 0:
            raise ValueError("Revenue must be greater than zero")
        return int(value)
    elif isinstance(value, str):
        raw = value.strip().lower().replace(",", "")
        if raw.endswith("b"):
            num = int(float(raw[:-1]) * 1000)
        elif raw.endswith("t"):
            num = int(raw[:-1]) * 1_000_000
        else:
            try:
                num = int(raw)
            except:
                raise ValueError("Revenue string could not be parsed")
        if num <= 0:
            raise ValueError("Revenue must be > 0")
        return num
    else:
        raise ValueError("Revenue must be int, float, or string")

def validate_employee_count(value):
    if isinstance(value, int):
        num = value
    elif isinstance(value, float):
        num = int(value)
    elif isinstance(value, str):
        match = re.match(r"^\s*(\d+)\s*-\s*(\d+)\s*$", value)
        if match:
            low, high = int(match.group(1)), int(match.group(2))
            num = (low + high) // 2
        else:
            try:
                num = int(float(value.strip()))
            except:
                raise ValueError("Employee count string invalid")
    else:
        raise ValueError("Invalid type for employee count")
    if num < 0:
        raise ValueError("Employee count must be greater than zero")
    return num

def validate_stock_ticker(ticker: str) -> str:
    if not isinstance(ticker, str):
        raise ValueError("Stock ticker must be a string")
    ticker = ticker.strip().upper()
    if not ticker.isalnum():
        raise ValueError("Stock ticker must be alphanumeric")
    if len(ticker) > 10:
        raise ValueError("Stock ticker cannot exceed 10 characters")
    return ticker

# ------------------- COMPANY CLASS -------------------

class Company:
    def __init__(self, data: dict):
        self.company_name = normalize_company_name(data.get("company_name"))
        self.industry = data.get("industry")
        self.revenue_mil = normalize_revenue(validate_revenue(data.get("revenue_mil")))
        self.employee_count = validate_employee_count(data.get("employee_count"))
        self.country = normalize_country(data.get("country"))
        self.founded_year = data.get("founded_year")
        self.ceo_name = normalize_ceo_name(data.get("ceo_name"))
        self.headquarters_city = normalize_city(data.get("headquarters_city"))
        self.stock_ticker = validate_stock_ticker(data.get("stock_ticker"))
        self.ingestion_timestamp = datetime.now(timezone.utc)
        self.revenue_per_employee = (self.revenue_mil / self.employee_count) if self.employee_count > 0 else None

# ------------------- TEST CASES -------------------

test_cases = [
    {
        "company_name": "Zero Div Co",
        "industry": "Technology",
        "revenue_mil": 1000,
        "employee_count": 0,
        "country": "US",
        "founded_year": 2000,
        "ceo_name": "Mr. John Doe",
        "headquarters_city": "New York",
        "stock_ticker": "ZDC"
    },
    {
        "company_name": "NoneType Inc",
        "industry": "Finance",
        "revenue_mil": None,
        "employee_count": 50,
        "country": "GB",
        "founded_year": 1999,
        "ceo_name": "Dr. Alice Smith",
        "headquarters_city": "London",
        "stock_ticker": "NTI"
    },
    {
        "company_name": "AttrError Corp",
        "industry": "Retail",
        "revenue_mil": "100",
        "employee_count": "50-100",
        "country": "FR",
        "founded_year": 1980,
        "ceo_name": "Prof. Mark Lee",
        "headquarters_city": None,
        "stock_ticker": "AEC"
    },
    {
        "company_name": "Good Company Ltd",
        "industry": "Technology",
        "revenue_mil": "1.5b",
        "employee_count": "100-200",
        "country": "JP",
        "founded_year": 2015,
        "ceo_name": "Dr. Ken Tanaka",
        "headquarters_city": "Tokyo",
        "stock_ticker": "GCLTD"

    },
    {
        "company_name": "Healty LLC",
        "industry": "Healthcare",
        "revenue_mil": 500,
        "employee_count": 1_000_000,
        "country": "CA",
        "founded_year": 2010,
        "ceo_name": "Ms. Jane Roe",
        "headquarters_city": "Toronto",
        "stock_ticker": "AMLLC"
    }
]

# ------------------- RUN TEST CASES -------------------

for i, data in enumerate(test_cases, 1):
    print(f"\n--- Test case {i} ---")
    try:
        company = Company(data)
        print("SUCCESS:", vars(company))
    except ZeroDivisionError as e:
        print("ZeroDivisionError caught:", e)
    except TypeError as e:
        print("NoneType / TypeError caught:", e)
    except AttributeError as e:
        print("AttributeError caught:", e)
    except ValueError as e:
        print("ValueError caught:", e)
    except Exception as e:
        print("Other Exception caught:", e)



import csv
from io import StringIO
from datetime import datetime, timedelta
import pandas as pd

# ---------------------- CSV data as string ----------------------
csv_data = f"""user_id,timestamp,event
U1,2024-01-01 10:00,login
U1,2024-01-01 10:10,view_page
U1,2024-01-01 11:00,logout
U2,2024-01-01 09:00,login
U2,2024-01-01 09:20,purchase
U2,2024-01-01 12:00,logout
U3,2024-01-01 08:00,login
U3,2024-01-01 08:05,view_page
U3,2024-01-01 08:50,logout
"""






# Parse CSV data into list of dictionaries
events = []
f = StringIO(csv_data)
reader = csv.DictReader(f)
res = {}

for row in reader:
  user_item_list = []
  user_item = {}
  user_item['timestamp'] = row['timestamp']
  user_item['event'].append(row['event'])

  user_item_list.append(user_item)
  res[row['user_id']] = user_item_list



print(res)





# ---------------------- TODO: Group events by user_i  ----------------------
"""
Expected Output
{
    "U1": [
        {
            "events": ["login", "view_page"],
            "start_time": "2024-01-01 10:00:00",
            "end_time": "2024-01-01 10:10:00"
        },
        {
            "events": ["logout"],
            "start_time": "2024-01-01 11:00:00",
            "end_time": "2024-01-01 11:00:00"
        }
    ],
    "U2": [
        {
            "events": ["login", "purchase"],
            "start_time": "2024-01-01 09:00:00",
            "end_time": "2024-01-01 09:20:00"
        },
        {
            "events": ["logout"],
            "start_time": "2024-01-01 12:00:00",
            "end_time": "2024-01-01 12:00:00"
        }
    ],
    .....
"""


