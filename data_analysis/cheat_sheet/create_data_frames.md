
# Create DataFrames and Series

# Create DataFrames and Series

Often it is useful to convert other Python data structures to pandas types:

### Series from a Python List

```python
import pandas as pd

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
```

### Series from a Numpy array

The `index` parameter is optional

```python
import numpy as np

r = np.random(1, 10, size=10)
s = pd.Series(r)
```

### DataFrame from a nested list

```python
penguins = pd.DataFrame(
    [["Skipper", 12],
     ["Kowalski", 34],
     ["Rico", 56],
     ["Private", 78]],
    columns=["name", "id"])
```

### DataFrame from a dictionary

When using a dict, the keys are used as column names.

```python
penguins = pd.DataFrame({
    "name": ["Skipper", "Kowalski", "Rico", "Private"],
    "id": [12, 34, 56, 78]
})
```

### DataFrame from a Numpy array

Numpy makes it easy to create really huge DataFrames. The index and column names is totally optional, because consecutive numbers are used by default.

    :::python3
    data = np.random.normal(size=(100, 100))
    pd.DataFrame(data, index=range(100), columns=range(100))