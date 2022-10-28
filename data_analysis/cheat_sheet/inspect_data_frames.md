
# Inspect DataFrames

These are few but very important diagnostic commands

### Number of Rows and Columns

```python
import seaborn as sns

df = sns.load_dataset('penguins')

df.shape
```

### Data Types

```python
df.dtypes
```

### Generic Overview

Data types + number of entries for each column + memory size

```python
df.info()
```

### Unique Value Count

```python
df['species'].value_counts()
```

### Unique Values

df['island'].unique()