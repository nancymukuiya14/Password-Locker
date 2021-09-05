class User():
    """
    Create User class that generates new instances of a user.

    """
    user_list = []

    def __init__(self, username, password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        A method that saves a new user instace into the user list
        """
        User.user_list.append(self)

    @classmethod
    def find_user_by_username(cls, username):
        """
        Find user
        """
        for username in cls.user_list:
            if User.username == username:
                return User
    def delete_user(self):
        '''
        deletes a  saved account from the list
        '''
        User.user_list.remove(self)
    
    
    @classmethod    
    def check_user(cls, username, password):
        '''
        checks if the user exists
        '''
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return True
        return False
    
    def display_users(self):
        '''
        returns the user list
        '''
        return User.user_list
 
    