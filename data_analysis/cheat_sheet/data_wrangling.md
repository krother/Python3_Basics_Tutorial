# Data Wrangling

The commands here operate mostly on a per-column-basis.

```python
import seaborn as sns
import pandas as pd
import numpy as np

df = sns.load_dataset('penguins')
```

### Add a Column

```python
# set entire column to same value
df['col1'] = 7

# use list-like data (pd.Series and np.array work as well)
data = list(range(df.shape[0])) # create list of correct length
df['col2'] = data
```

### Remove a Column

```python
del df['col1']
```

### Column Arithmetics

```python
df['body_mass_kg'] = df['body_mass_g'] / 1000

# log-transform
df['log_body_mass'] = np.log(df['body_mass_g'])
```

### Change Column Data Type

```python
# convert to string
df['mass'] = df['body_mass_g'].astype(str) + 'g'
```

### Set the Index Column

The index is a special column of a DataFrame, because it is treated differently by many operations in pandas.

```python
# put the species column in the index
df_species = df.set_index('species')

# now you can select by species easily:
df_species.loc['Gentoo']
```

Note that the `inplace=True` parameter modifies the DataFrame instead of returning a new one:

```python
df.set_index('species', inplace=True)
```

This notation is more memory-efficient, but it is more tricky in Jupyter notebooks (e.g. when you run that line twice you get different results.

To move the index to a regular column, use:

```python
df_reset = df.reset_index()  # inserts a numerical index
```

### Missing Values

Missing values are a common phenomenon. A quick way to diagnose missing values is:

```python
df.isna().sum().plot.bar()
```

Often, you might simply want to kick out all rows in which a None or NaN occurs:

```python
df_dropped = df.dropna(inplace=False)  # same logic as with set_index()
```

Alternatively, you might want to fill in a best guess value:

```python
df_fixed = df.fillna(42)
# or
df_fixed = df.fillna(df.median())
```

There are many, many strategies to fix missing values (imputation methods).

### Concatenate multiple DataFrames

```python
# suppose you have multiple DataFrames with the same columns
df1 = df.sample(5)
df2 = df.sample(5)
df3 = df.sample(5)

# connect them to one DataFrame vertically
df_all = pd.concat([df1, df2, df3])
```

### Swap Rows and Columns

Some operations (especially plotting) are easier to implement if you turn a DataFrame by 90°:

```python
df.transpose()
```

### Iterate

Usually, it is possible to write one-liners or concise expressions that get the job done. If this is not possible (or you are still learning this stuff and can’t figure out a better way yet), you may want to fall back to a `for` loop over all the rows.

for index, row in df.iterrows():
    print(index, row['body_mass_g']