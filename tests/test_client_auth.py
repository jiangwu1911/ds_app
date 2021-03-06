# -*- coding: UTF-8 -*-

import sys
import unittest
import json
import httplib2
from urllib import urlencode

from test_base import BaseTestCase


class LoginTestCase(BaseTestCase):
    def test_login_wiith_empty_username(self):
        content = self.get_token('', 'admin')
        error = json.loads(content)['error']['code']
        self.assertEqual(error, "400", "test login with empty username failed")


    def test_login_wiith_wrong_username(self):
        content = self.get_token('admin1', 'admin')
        error = json.loads(content)['error']['code']
        self.assertEqual(error, "403", "test login with wrong username failed")


    def test_login_wiith_wrong_password(self):
        content = self.get_token('admin', 'admin1')
        error = json.loads(content)['error']['code']
        self.assertEqual(error, "403", "test login with wrong password failed")


    def test_login(self):
        content = self.get_token('admin', 'admin')
        token = json.loads(content)['success']['token']
        self.assertTrue(len(token)>0, 'test login failed')

        h = httplib2.Http()
        resp, content = h.request(self.base_url + "logout",
                                  "POST",
                                  headers={'Content-Type': 'application/x-www-form-urlencoded',
                                           'X-Auth-Token': token}
                                 )


    def test_logout_token_not_found(self):
        h = httplib2.Http()
        token = '123456'
        resp, content = h.request(self.base_url + "logout",
                                  "POST",
                                  headers={'Content-Type': 'application/x-www-form-urlencoded',
                                           'X-Auth-Token': token})

    def test_list_role(self):
        content = self.get_token('熊大', 'abc123')
        token = json.loads(content)['success']['token']
        h = httplib2.Http()
        resp, content = h.request(self.base_url + "roles",
                                  "GET",
                                  headers={'Content-Type': 'application/x-www-form-urlencoded',
                                           'X-Auth-Token': token}
                                 )
        roles = json.loads(content)['roles']
        self.assertTrue(len(roles)>1, 'test_list_role failed')


    def test_login_sql_injection(self):
        content = self.get_token("ad'min", "admin")


if __name__ == "__main__":
    unittest.main()
