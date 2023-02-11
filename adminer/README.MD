### Adminer

Simple python script to run sql commands on adminer web interface (for example if the database is only for localhost)

> Install
`pip install -r requirements.txt`

> Example
```python
import adminer
from typing import List

con: MysqlAdminer = MysqlAdminer.connect("your.server.com", "username", "password", "database")

result: List[dict] = con.query("select * from yourtable")
for row in result:
    print(row)

con.close()
```
