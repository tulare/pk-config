# -*- coding: utf-8 -*-

# logging
import logging
logger = logging.getLogger(__name__)
logger.debug(f'MODULE {__name__}')

import pathlib
import sqlite3
import json

from .exceptions import ConfigurationError, ConfigurationKeyError
from ..patterns import Borg

__all__ = [
    'Configuration',
    'project_database', 'project_path',
]

# --------------------------------------------------------------------

def project_database(locator, db_name=None) :
    prj_path = project_path(locator)

    if db_name is None :
        db_name = prj_path.stem + '-config.db'

    if prj_path.is_file() :
        prj_path = prj_path.parent

    return prj_path.joinpath(db_name)

# --------------------------------------------------------------------

def project_path(locator) :
    try :
        prj_path = pathlib.Path(__loader__.archive).absolute()
    except (NameError, AttributeError) :
        prj_path = pathlib.Path(locator.__file__).absolute()

    # return dirname
    return prj_path.parent
        

# --------------------------------------------------------------------

class Configuration(Borg) :

    __namespace__ = 'config'

    def __init__(self, db_name=':memory:') :

        if not hasattr(self, '_database') :
            self.database = db_name

    @property
    def database(self) :
        return self._database

    @database.setter
    def database(self, db_name) :
        self._database = str(db_name)
        self.connection = sqlite3.connect(self._database)
        self.cursor = self.connection.cursor()

        # creation table config si nécessaire
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS config (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            )
            """
        )
        
    
    @property
    def items(self) :
        # select
        self.cursor.execute(
            """
            SELECT * FROM config
            """
        )
        return dict(self.cursor.fetchall())

    @property
    def keys(self) :
        return set(self.items.keys())

    def get(self, key, default=None) :
        self.cursor.execute(
            """
            SELECT value FROM config WHERE key = ?
            """,
            (key,)
        )
        row = self.cursor.fetchone()
        if row :
            return row[0]            
        else :
            if default is None :
                raise ConfigurationKeyError(key)
            return default

    def get_json(self, key, default=None) :
        
        try :
            json_str = self.get(key, default)
            return json.loads(json_str)
        except Exception as e :
            return default

    def add(self, key, value) :
        try :
            # insert
            self.cursor.execute(
                """
                INSERT INTO config VALUES(? , ?)
                """,
                (key, value)
            )
        except sqlite3.IntegrityError as e :
            # update
            self.cursor.execute(
                """
                UPDATE config SET value = ? WHERE key = ?
                """,
                (value, key)
            )
        finally :
            # commit
            self.connection.commit()

        return self.cursor.rowcount

    def add_json(self, key, value) :
        
        try :
            json_str = json.dumps(value)
            return self.add(key, json_str)
        except Exception as e :
            return 0
        
    def delete(self, key) :
        try :
            # delete
            self.cursor.execute(
                """
                DELETE FROM config WHERE key = ?
                """,
                (key,)
            )
        finally :
            # commit
            self.connection.commit()

        return self.cursor.rowcount
        
    def checklist(self, key_list) :
        missing = set(key_list).difference(self.keys)
        if missing :
            raise ConfigurationError(missing)

        return True
        
    def checkfile(self, chkfile) :
        with open(chkfile, 'r') as fd :
            key_list = set(line.strip() for line in fd)
            return self.checklist(key_list)
            
