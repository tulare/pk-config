# pk-config
Configuration management for python projects

## usage
first create an empty locator.py file in the project directory
```
project
  - locator.py
```

```
import locator
from pk_config import config
prj_path = config.project_path(locator)

# automatic database name : project-config.db
prj_database = config.project_database(locator)

# or specify database name : config.db
prj_database = config.project_database(locator, 'config.db')

# creates or loads configuration
conf = config.Configuration(prj_database)
```
