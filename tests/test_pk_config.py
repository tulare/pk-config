# -*- coding: utf-8 -*-

import unittest
import pathlib
from pk_config import config

from . import locator

# ---

class Test_00_config(unittest.TestCase) :

    def setUp(self) :
        self.database = config.project_database(locator)
        self.conf = config.Configuration(self.database)

    def tearDown(self):
        pass

    def test_00_Trivial(self) :
        assert True, 'True basic trivial test'

    def test_01_Location(self) :
        assert locator.location.exists(), 'location exists'
        assert locator.location.is_dir(), 'location is dir'

    def test_02_Database(self) :
        assert self.database.exists(), 'database exists'
        assert self.database.is_file(), 'database is file'

    def test_03_Text(self) :
        self.conf.add('test_text', 'texte')
        assert self.conf.get('test_text') == 'texte', 'add / get'
    
    def test_04_Json(self) :
        self.conf.add_json('test_json', True)
        assert self.conf.get_json('test_json', False), 'add_json / get_json'

    def test_05_DicoJson(self) :
        dico = { 'one' : { 'two' : 3 }}
        self.conf.add_json('test_dico_json', dico)
        assert self.conf.get_json('test_dico_json', {}) == dico, 'dico add_json / get_json'

    def test_06_keys(self) :
        assert isinstance(self.conf.keys, set), 'keys is set'
        assert self.conf.keys == set([
            'test_text', 'test_json', 'test_dico_json']), 'keys check'

    def test_99_Cleanup(self) :
        self.conf.connection.close()
        self.database.unlink()
        assert not self.database.exists(), 'database not exists'

# ---

if __name__ == '__main__' :
    unittest.main()
