# -*- coding: UTF-8 -*-

import sys
import unittest
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

sys.path.append("..")
from appserver.model import User
from appserver.utils import obj_array_to_json
from appserver.utils import md5encode

reload(sys)
sys.setdefaultencoding( "utf-8" )

class UtilsTestCase(unittest.TestCase):
    def _create_session(self):
        engine = create_engine('mysql://%s:%s@%s/%s?charset=%s' %
                               ('root', '', 'localhost', 'cloudapi', 'utf8'),
                               echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
        

    def test_json_user_encode(self):
        session = self._create_session()
        results = session.query(User)
        str = obj_array_to_json(results, 'users')
        print json.loads(str) 


    def test_md5encode(self):
        print md5encode('admin')
        

if __name__ == "__main__":
    unittest.main()
