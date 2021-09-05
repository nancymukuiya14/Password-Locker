import unittest
from password import User
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    """
    This defines test cases for credentials class

    """

    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.

        """
        self.new_credential = Credentials('Facebook','nancykigos','SantoRINI2021')

    def test_init(self):
        """
        Check if new Credentials have been initialized correctly

        """
        self.assertEqual(self.new_credential.account, 'Facebook')
        self.assertEqual(self.new_credential.userName, 'nancykigos')
        self.assertEqual(self.new_credential.password, 'SantoRINI2021')

    def save_credential_test(self):
        """
        Check if the credential object is saved into the credentials list.
        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_many_accounts(self):
        '''
        Check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("Facebook","nancykigos","SantoRINI2021")
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        """
        Remove an account credentials from our credentials_list
        """
        self.new_credential.save_details()
        test_credential = Credentials("Facebook","nancykigos","SantoRINI2021")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    # def test_find_credential_by_account(self):
    #     """
    #     find account
    #     """
    #     self.new_credential.save_details()
    #     test_credential = Credentials("Facebook","nancykigos","SantoRINI2021")
    #     test_credential.save_details()
        
    #     self.assertEqual(len(Credentials.find_by_account("Facebook")),2)
        
        

if __name__ == "__main__":
    unittest.main()
