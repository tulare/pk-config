# pk-config
Configuration management for python projects

## usage
```
import __main__ as locator
from pk_config import config

prj_path = config.project_path(locator)

# automatic database name : project-config.db
prj_database = config.project_database(locator)

# or specify database name : config.db
prj_database = config.project_database(locator, 'config.db')

# creates or loads configuration
conf = config.Configuration(prj_database)
```
