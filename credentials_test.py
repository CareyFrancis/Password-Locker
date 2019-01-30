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
