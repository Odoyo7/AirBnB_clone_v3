#!/usr/bin/python3
"""
Unit Test for User Class
"""
import unittest
from datetime import datetime
import models
import json

User = models.user.User
BaseModel = models.base_model.BaseModel


class TestUserDocs(unittest.TestCase):
    """Class for testing User Class docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   User  Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nUser Class from Models Module\n'
        actual = models.user.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'User class handles all application users'
        actual = User.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiates a new user'
        actual = User.__init__.__doc__
        self.assertEqual(expected, actual)


class TestUserInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  User  Class  .........')
        print('.................................\n\n')

    def test_instantiation(self):
        """... checks if User is properly instantiated"""
        my_user = User()
        self.assertIsInstance(my_user, User)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_user = User()
        my_str = str(my_user)
        my_list = ['User', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_user = User()
        my_str = str(my_user)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        my_user = User()
        my_user.save()
        actual = type(my_user.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        my_user = User()
        my_user_json = my_user.to_json()
        actual = 1
        try:
            serialized = json.dumps(my_user_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        """... to_json should include class key with value User"""
        my_user = User()
        my_user_json = my_user.to_json()
        actual = None
        if my_user_json['__class__']:
            actual = my_user_json['__class__']
        expected = 'User'
        self.assertEqual(expected, actual)

    def test_email_attribute(self):
        """... add email attribute"""
        my_user = User()
        my_user.email = "bettyholbertn@gmail.com"
        if hasattr(my_user, 'email'):
            actual = my_user.email
        else:
            acual = ''
        expected = "bettyholbertn@gmail.com"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main