
# Select Rows and Columns

```python
import seaborn as sns

df = sns.load_dataset('penguins')
```

### Show column names

```python
df.columns
```

### Select a column

```python
df['species']
```

### Select multiple columns

Takes a list of column names

```python
df[['species', 'body_mass_g']]
```

### Select columns by position

Uses the Python slicing notation

```python
df.iloc[:, 1:4]
```

### Select the first rows

```python
df.head(3)
```

### Select the last rows

```python
df.tail(3)
```

### Select rows by position

```python
df.iloc[10:20]
```

### Select rows by index label

This is very useful if your index contains something else than numbers, e.g.

```python
by_species = df.set_index('species') # new DF with different index

by_species.loc['Gentoo']
```

### Filter by value

This is very powerful selection logic

```python
df[df['species'] == 'Adelie']

df[df['body_mass_g'] < 3000]

df[df['body_mass_g'].between(3000, 4000)]
```

### Select random rows

```python
df.sample(7)
```
