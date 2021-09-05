import unittest
from password import User

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
        
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('Nancykigotho','Maldives106')
    def test_init(self):
        """
        Checking if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'Nancykigotho')
        self.assertEqual(self.new_user.password,'Maldives106')
        
    def test_save_user(self):
        """
        Test if a new user has been saved into the User list

        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
        
    def test_delete_user(self):
        """
        Test if a user can be deleted from the user list
        """
        self.new_user.save_user()
        test_user = User('Nancykigotho','Maldives106')
        self.assertEqual(len(User.user_list),1)
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),0)

    def test_user_exists(self):
        """
        Test if a user can be found by username
        """
        
        
        self.user_exists = User.check_user('Nancykigotho','Maldives106')
        
if __name__ == '__main__':
    unittest.main()
    

