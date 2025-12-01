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

#### 11. how to use Series.diff() in pandas?
```python
df['column'].diff() # get the difference between the current value and the previous value

Use diff() 
s = pd.Series([1, 4, 7, 10])
s.diff()

# 0    NaN      # No previous element
# 1    3.0      # 4 - 1 = 3
# 2    3.0      # 7 - 4 = 3
# 3    3.0      # 10 - 7 = 3
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
