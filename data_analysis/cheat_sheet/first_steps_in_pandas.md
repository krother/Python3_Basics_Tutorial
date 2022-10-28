
# First Steps in pandas

* `pd` refers to the pandas library imported with `import pandas as pd` .
* `df` refers to a DataFrame object, `s` to a Series object.

## Data I/O

- `pd.read_csv(filename)` - read a CSV file. Returns a DataFrame.
- `pd.read_excel(filename)` - read an Excel Spreadsheet. Returns a DataFrame.

### Inspect DataFrames

- `df.shape` - the number of rows and columns
- `df.info()` - displays columns and their types
- `s.value_counts()` - displays unique values and their counts

### Select Rows and Columns

- `df['col']` - selects a single column by its name
- `df.col` - also selects a column (only works if no white space in the name)

### Data Wrangling

- `df.sort_values(by=col1)` sorts the entire DataFrame (changes it in-place)

### Aggregation Functions

- `s.mean()` - calculates the mean
- `s.median()` - calculates the median
- `s.std()` - calculates the standard deviation
- also try `s.sum()` `s.count()` `s.min()` `s.max()`
- `df.groupby(col).agg_func()` - groups by a column and runs an aggregation function over each group (see above for choices for agg_func).

### Arithmetics

- `s.cumsum()` - cumulative sum of a column