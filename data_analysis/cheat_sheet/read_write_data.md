
# Read and Write Data

### Read CSV files

The `read_csv` function is often the first command used. It has a lot of optional parameters, 3 of which are shown here:

```python
import pandas as pd

df = pd.read_csv('penguins.csv', index_col=0, sep=',', header=True)
```

### Read Excel files

```python
df = pd.read_excel('penguins.xlsx', index_col=0)
```

### Read SQL

You will need to create a DB connection first. Requires installing the SQLAlchemy package and a DB connection package, e.g. `psycopg2` for PostGreSQL

```python
from sqlalchemy import create_engine

conn = create_engine('postgres//user:psw@host:port/dbname')
df = pd.read_sql('SELECT * FROM penguins', conn)
```

### Read JSON

Reading JSON only works if the structure is table-like.

```python
df = pd.read_json('penguins.json') 
```

### Read from Clipboard

This is sometimes useful when improvising

```python
df = pd.read_clipboard()
```
