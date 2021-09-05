import random
import string


class Credentials():
    """
  Helps create new objects of credentials
  """

    credentials_list = []

    def __init__(self, account, userName, password):
        """
           This method defines user credentials.
           """
        self.account = account
        self.userName = userName
        self.password = password

    def save_credential(self):
        """
      method to store a new credential to the credentials list
      """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)
    def display_credentials(self):
        """
        method that returns the credentials list
        """
        return Credentials.credentials_list

    def generatePassword(stringLength=8):
        """Generate a random password string of letters and digits and special characters"""

        password = string.hexdigits
        return ''.join(random.choice(password) for i in range(stringLength))

    @classmethod
    def find_credential(cls, account):
        """
       This method takes in an account and returns a credential that is the same with that of the account_name.

       """
        find_credential = [credential 
        for credential in cls.credentials_list
            if credential.account == account]
        return find_credential
                
    #  find_credential = Credentials.find_by_account(account)
    #     for credential in cls.credentials_list:
    #         if credential.account == account:
    #             return credential

    @classmethod
    def verify_user(cls, username, password):
        """
       Verify whether the user is in our user_list or not
       """
        for credential in cls.credentials_list:
            return credential.userName == username and credential.password == password
        return False
        # current_user = find_credential(username, password)
        # return current_user
