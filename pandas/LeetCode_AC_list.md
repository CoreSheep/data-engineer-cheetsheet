## LeetCode Problems Solved (Pandas)

**Total Solved: 13 problems** | **Difficulty: All Easy**

| # | Problem ID | Difficulty | Problem Name |
|---|:----------:|:----------:|:-------------|
| 1 | 175 | Easy | [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) |
| 2 | 181 | Easy | [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) |
| 3 | 182 | Easy | [Duplicate Emails](https://leetcode.com/problems/duplicate-emails/) |
| 4 | 183 | Easy | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) |
| 5 | 196 | Easy | [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/) |
| 6 | 197 | Easy | [Rising Temperature](https://leetcode.com/problems/rising-temperature/) |
| 7 | 511 | Easy | [Game Play Analysis I](https://leetcode.com/problems/game-play-analysis-i/) |
| 8 | 512 | Easy | [Game Play Analysis II](https://leetcode.com/problems/game-play-analysis-ii/) |
| 9 | 577 | Easy | [Employee Bonus](https://leetcode.com/problems/employee-bonus/) |
| 10 | 584 | Easy | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) |
| 11 | 586 | Easy | [Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/) |
| 12 | 595 | Easy | [Big Countries](https://leetcode.com/problems/big-countries/) |
| 13 | 596 | Easy | [Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/) |
| 14 | 597 | Easy | [Friend Requests I: Overall Acceptance Rate](https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/) |
| 15 | 603 | Easy | [Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/) |
| 16 | 610 | Easy | [Triangle Judgement](https://leetcode.com/problems/triangle-judgement/) |
| 17 | 613 | Easy | [Shortest Distance in a Line](https://leetcode.com/problems/shortest-distance-in-a-line/) |
| 18 | 619 | Easy | [Big Countries](https://leetcode.com/problems/big-countries/) |
| 19 | 620 | Easy | [Not Boring Movies](https://leetcode.com/problems/not-boring-movies/) |
| 20 | 1068 | Easy | [Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii/) |
| 21 | 1069 | Easy | [Product Sales Analysis IV](https://leetcode.com/problems/product-sales-analysis-iv/) |
| 22 | 1075 | Easy | [Project Employees I](https://leetcode.com/problems/project-employees-i/) |
| 23 | 1076 | Easy | [Project Employees II](https://leetcode.com/problems/project-employees-ii/) |
| 24 | 1082 | Easy | [Sales Analysis I](https://leetcode.com/problems/sales-analysis-i/) |
| 25 | 1083 | Easy | [Sales Analysis II](https://leetcode.com/problems/sales-analysis-ii/) |
| 26 | 1084 | Easy | [Sales Analysis III](https://leetcode.com/problems/sales-analysis-iii/) |
| 27 | 1141 | Easy | [User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i/) |
| 28 | 1142 | Easy | [User Activity for the Past 30 Days II](https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/) |
| 29 | 1173 | Easy | [Immediate Food Delivery I](https://leetcode.com/problems/immediate-food-delivery-i/) |
| 30 | 1179 | Easy | [Reformat Department Table](https://leetcode.com/problems/reformat-department-table/) |
| 31 | 1211 | Easy | [Queries Quality and Percentage](https://leetcode.com/problems/queries-quality-and-percentage/) |
| 32 | 1241 | Easy | [Number of Comments per Post](https://leetcode.com/problems/number-of-comments-per-post/) |
| 33 | 1280 | Easy | [Students and Examinations](https://leetcode.com/problems/students-and-examinations/) |
| 34 | 1303 | Easy | [Find the Team Size](https://leetcode.com/problems/find-the-team-size/) |
| 35 | 1322 | Easy | [Ads Performance](https://leetcode.com/problems/ads-performance/) |
| 36 | 1327 | Easy | [List the Products Ordered in a Period](https://leetcode.com/problems/list-the-products-ordered-in-a-period/) |
| 37 | 1350 | Easy | [Students With Invalid Departments](https://leetcode.com/problems/students-with-invalid-departments/) |
| 38 | 1378 | Easy | [Replace Employee ID With The Unique Identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/) |
| 39 | 1421 | Easy | [NPV Queries](https://leetcode.com/problems/npv-queries/) |
| 40 | 1435 | Easy | [Create a Session Bar Chart](https://leetcode.com/problems/create-a-session-bar-chart/) |
| 41 | 1484 | Easy | [Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/) |
| 42 | 1495 | Easy | [Friendly Movies Streamed Last Month](https://leetcode.com/problems/friendly-movies-streamed-last-month/) |


### note:
#### 1. how to aggregate data in pandas?
- use `groupby()` to group the data by a column
- use `agg()` to aggregate the data by a column
- use `size()` to get the number of rows in each group
- use `reset_index()` to convert the Series to a DataFrame
```python
df.groupby('column').agg({'other_column': 'mean'}) # mean, median, sum, size(all values including null values), count(all non-null values), max, min, first(the first value), last(the last value)
df.groupby("class").size().reset_index(name='count') # reset_index() is used to convert the Series to a DataFrame
df["count"].max() # get the maximum value of the "count" column, it is not a dataframe but a value

# multiple aggregations and custom aggregation functions with rename for the columns
def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries["quality_ratio"] = queries["rating"] / queries["position"]
    queries["is_poor"] = queries["rating"] < 3

    filtered = queries.groupby("query_name").agg(
        quality=("quality_ratio", "mean"),
        poor_query_percentage=("is_poor", lambda x: x.sum() / x.count() * 100)
    ).round(2)

    return filtered.reset_index()

# Use lambda function to create a new column with the percentage of poor queries
# x.sum() is used to count the number of True values in the "is_poor" column
# x.count() is used to count the number of values in the "is_poor" column
# lambda x: x.sum() / x.count() * 100 is used to calculate the percentage of poor queries
# round(2) is used to round the result to 2 decimal places (for two columns, the entire dataframe will be rounded to 2 decimal places)
# reset_index() is used to convert the Series to a DataFrame
# quality_ratio is the mean of the "quality_ratio" column
# poor_query_percentage is the percentage of poor queries
# query_name is the name of the query

```

#### 2. how to merge data in pandas?
```python
df.merge(other_df, on='key', how="left")
df.merge(other_df, left_on='key_a', right_on='key_b', how="left") # left_on and right_on are used to specify the columns to merge on
df.merge(df, on="key", how="left", suffixes=("_left", "_right")) # suffixes are used to specify the suffixes of the columns to merge on (self-join)
```

#### 3. how to sort data in pandas?
```python
df.sort_values('column', ascending=False, inplace=True)
df.sort_values(['column1', 'column2'], ascending=[False, True], inplace=True)
```

#### 4. how to filter data in pandas?
```python
df[df['column'] > value]
df[(df['column1'] > value1) and (df['column2'] > value2)] # filter by multiple conditions
```

#### 5. how to rename columns in pandas?
```python
df.rename(columns={'old': 'new'}, inplace=True) # don't forget to add columns={'old': 'new'} to save the changes
```

#### 6. how to add and shift columns in pandas?
```python
df['new_column'] = value # add a new column
df['new_column'] = df['column'] + 1 # add the value of the "column" column to the "new_column" column
df['new_column'] = df['column'].shift(1) # shift the value of the "column" column to the "new_column" column (get the previous value)
df['new_column'] = df['column'].shift(-1) # shift the value of the "column" column to the "new_column" column (get the next value)
```

#### 7. how to compare Timedelta in pandas?
```python
weather["record_date"] - weather["previous_date"] == pd.Timedelta(days=1) # compare the value of the "record_date" column to the "previous_date" column (get the difference)    
# convert date column to datetime in pandas
weather["record_date"] = pd.to_datetime(weather["record_date"])
weather["previous_date"] = pd.to_datetime(weather["previous_date"])

# 2. how to use dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second in pandas?
weather["record_date"] = pd.to_datetime(weather["record_date"])

weather["record_date"].dt.day # get the day of the week
weather["record_date"].dt.month # get the month of the year
weather["record_date"].dt.year # get the year of the month
weather["record_date"].dt.hour # get the hour of the day
weather["record_date"].dt.minute # get the minute of the hour
weather["record_date"].dt.second # get the second of the minute
```

#### 8. how drop duplicates in pandas?
```python
df.drop_duplicates(subset=['column1', 'column2'], keep='first', inplace=True) # drop duplicates by multiple columns, keep the first occurrence
# subset is used to specify the columns to drop duplicates on
# keep can be 'first', 'last', False
# False means drop all duplicates
# 'first' means keep the first occurrence
# 'last' means keep the last occurrence
```

#### 9. how to convert data type in pandas?
```python
df['column'] = df['column'].astype('int') # convert the data type of the "column" column to int
df['column'] = df['column'].astype('float') # convert the data type of the "column" column to float
df['column'] = df['column'].astype('str') # convert the data type of the "column" column to str
df['column'] = df['column'].astype('bool') # convert the data type of the "column" column to bool
df['column'] = df['column'].astype('datetime') # convert the data type of the "column" column to datetime
```

#### 10. how to use isin() in pandas?
```python
df[df['column'].isin(df['other_column'])] # filter the data by multiple values
# isin() is used to check if the value of the "column" column is in the "other_column" column
```

#### 11. how to use Series.diff() in pandas? (same for shift(), cumsum())
```python
df['column'].diff() # get the difference between the current value and the previous value

Use diff() 
s = pd.Series([1, 4, 7, 10])
s.diff()

# 0    NaN      # No previous element
# 1    3.0      # 4 - 1 = 3
# 2    3.0      # 7 - 4 = 3
# 3    3.0      # 10 - 7 = 3

s = pd.Series([10, 20, 30])

s.shift(1)    # [NaN, 10, 20]
s.cumsum()    # [10, 30, 60]
```

#### 12. how to use pivot() and pivot_table() in pandas?
```python
df = pd.DataFrame({
    "id": [1, 1, 2],
    "month": ["Jan", "Feb", "Jan"],
    "revenue": [100, 200, 150]
})

# Long format:
#    id  month  revenue
# 0   1    Jan      100
# 1   1    Feb      200
# 2   2    Jan      150

df.pivot(index="id", columns="month", values="revenue") (no duplicates for columns)

# Wide format:
# month  Feb    Jan
# id              
# 1      200.0  100.0
# 2      NaN    150.0


df.pivot_table(values='value', index='index', columns='column', aggfunc='mean') # pivot the data by the "index" column and the "column" column
# values is used to specify the column to pivot
# index is used to specify the column to pivot on
# columns is used to specify the column to pivot on
# aggfunc is used to specify the aggregation function
```

#### 13. how to use map() in column to replace the values?
```python
df['column'] = df['column'].map({'old': 'new'}) # replace the values of the "column" column with the "new" value

# e.g. map True to "Yes" and False to "No"
triangle["triangle"] = (
    (triangle["x"] + triangle["y"] > triangle["z"]) &
    (triangle["x"] + triangle["z"] > triangle["y"]) &
    (triangle["y"] + triangle["z"] > triangle["x"])
).map({True: "Yes", False: "No"})

[True, False, True].map({True: "Yes", False: "No"}) # ["Yes", "No", "Yes"]
```

#### 14. the difference between size() and count() in pandas/groupby()?
```python
df = pd.DataFrame({
    "a": [1, None, 3],
    "b": [4, 5, None]
})

df.size     # 6 (3 rows × 2 cols) as an attribute of the dataframe
df.count()  # Series: a=2, b=2 (non-null per column)


# size() and count() are different in groupby()
df = pd.DataFrame({
    "group": ["A", "A", "B"],
    "value": [1, None, 3]
})

df.groupby("group").size()
# group
# A    2
# B    1
# (counts all rows per group)

df.groupby("group").count()
# group  value
# A      1      (skips None)
# B      1

df.groupby("group").agg({"value": "nunique"}) # count the number of unique values in the "value" column 
# group  value
# A      1      (counts the number of unique values in the "value" column)
# B      1
```

#### 15. different ways to write a groupby()?
```python
sales.groupby("seller_id")["price"].sum()
sales.groupby("seller_id").agg({"price": "sum"})
sales.groupby("seller_id")["price"].agg("sum") # same as sales.groupby("seller_id")["price"].sum()
```

#### 16. pandas broadcasting for dataframe?
```python
s = pd.Series([10, 20, 30])

# Arithmetic
s + 5     # [15, 25, 35]
s - 5     # [5, 15, 25]
s * 2     # [20, 40, 60]
s / 10    # [1.0, 2.0, 3.0]

# Comparison (returns Boolean Series)
s > 15    # [False, True, True]
s < 25    # [True, True, False]
s == 20   # [False, True, False]
```

#### 17. how to use na-related functions in pandas?
```python
# check if the values are NaN or not
s = pd.Series([1, None, 3, None])

s.isna()     # [False, True, False, True]
s.isnull()   # [False, True, False, True] same as s.isna()
s.notna()    # [True, False, True, False]
s.notnull()  # [True, False, True, False] same as s.notna()


s = pd.Series([1, None, 3, None])
# fill the NaN values with 0 or "X"
s.fillna(0)     # [1, 0, 3, 0]
s.fillna("X")   # [1, "X", 3, "X"]
s.dropna()      # [1, 3]
s.ffill()       # [1, 1, 3, 3] (fill the next value)
s.bfill()       # [1, 3, 3, NaN] (fill the previous value)
# fill with NaN for integer and float
s.fillna(np.nan)

# count the number of NaN and non-NaN values
s.isna().sum()    # count of NaN
s.notna().sum()   # count of non-NaN

# drop the rows with NaN and fill the NaN values with 0
df = pd.DataFrame({
    "a": [1, None, 3],
    "b": [None, 5, 6]
})

df.dropna()              # rows with no NaN
df.dropna(axis=1)        # columns with no NaN
df.fillna({"a": 0, "b": 99})  # different fill per column
```

#### 18. rounding in python and how to use a standard rounding function?
```python
# python always rounds to even
round(0.5)  # 0 (rounds to even)
round(1.5)  # 2 (rounds to even)
round(2.5)  # 2 (rounds to even)
round(3.5)  # 4 (rounds to even)

# use traditional rounding by using apply(round2)
round2 = lambda x: round(x + 1e-9, 2)
df.apply(round2)
# 0.00
# 1.00
# 2.00
# 3.00
```

#### 19. how to use merge on cross table? (fully connected table)
```python
merged = students.merge(subjects, how="cross").sort_values("student_id")
# how="cross" is used to create a cross table
# sort_values("student_id") is used to sort the data by the "student_id" column

# students is like this:
# student_id  student_name
# 1           John
# 2           Jane
# 3           Jim

# subjects is like this:
#   subject_name
#         Math
#         Science
#         History

# merged is like this:

#  student_id  student_name   subject_name
#           1           John         Math
#           1           John        Science
#           1           John        History
#           2           Jane        Math
#           2           Jane        Science
#           2           Jane        History
#           3           Jim         Math
#           3           Jim         Science
#           3           Jim         History
```

#### 20. how to use pivot_table() on cross table?
```python
pivot_table = pd.pivot_table(merged, values="student_id", index="student_name", columns="subject_name", aggfunc="count")
# values is used to specify the column to pivot on
# index is used to specify the column to pivot on
# columns is used to specify the column to pivot on
# aggfunc is used to specify the aggregation function
```

#### 21. how to use apply() in pandas?
```python

def weather_type(countries: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    filtered = weather.merge(countries, on="country_id", how="left")
    filtered = filtered[(filtered["day"] >= "2019-11-01") & (filtered["day"] <= "2019-11-30")]
    weathers = filtered.groupby("country_name").agg(
        weather_degree_avg=("weather_state", "mean")
    ).reset_index()
    def weather_convert(avg_degree):
        if avg_degree <= 15:
            return "Cold"
        elif avg_degree >= 25:
            return "Hot"
        else:
            return "Warm" 
    weathers["weather_type"] = weathers["weather_degree_avg"].apply(weather_convert)
    return weathers[["country_name", "weather_type"]].sort_values("country_name")

# apply() is used to apply a function to a column or a dataframe
# weather_convert is a function that converts the average degree to a weather type
# weather_type is a new column that contains the weather type
# country_name is the column to sort the data by
```

#### 22. how to use query() in pandas?
```python
df_filtered = df.query("age > 30 and city == 'Berlin'")
# query() is used to filter the data by multiple conditions

df_filtered = df[(df["age"] > 30) & (df["city"] == "Berlin")]
# filter the data by multiple conditions
```

#### 23. how to use assign() in pandas?
```python
# how to use assign() to add a new column to the dataframe with a new column name
# and you and also use a lambda function to add a new column
df2 = df.assign(total=df["price"] * df["qty"])

df2 = (
    df.assign(
        total=lambda x: x["price"] * x["qty"],
        discounted=lambda x: x["total"] * 0.9,
    )
)
```
