import unittest
from credentials import Credentials

class TestCredential(unittest.TestCase):
    '''
        The test credential class defines test cases for the credential class
    '''

    def setUp(self):
        '''
        The setUp method will run before each test case
        '''
        self.new_credential = Credentials('Twitter','fog123')
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.credential_detail,"Twitter")
        self.assertEqual(self.new_credential.password,"fog123")    

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential ser from the user_list
        '''

        Credentials.credential_list.remove(self)
