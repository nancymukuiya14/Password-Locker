#!/usr/bin/env python3.8
import unittest
from password import User
from credentials import Credentials


def create_user(username, password):
    '''
    Function to create a new user
    '''
    new_user_list = User(username, password)
    return new_user_list


def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()


def delete_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username)

def display_Credentials(user_name,password):
    '''
    Function to display credentials
    '''
    return Credentials.display_Credentials()

def create_Credentials(user_name,account,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(user_name,account,password)
    return new_credential
def save_Credentials(credential):
    '''
    Function to save credentials
    '''
    credential.save_Credentials()

def check_user(username):
    '''
    Function to check if a user exists
    '''
    return User.user_exist(username)
def user_exists(username,password):
    '''
    check if user exists
    '''
    return User.check_user(username,password)
def display_Credentials():
    '''
    Function to display credentials
    '''
    return Credentials.display_Credentials()
    
def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password = Credentials.generatePassword()
    return auto_password
def login_User(username,password):
    '''
    Function to login user
    '''
    check_user = Credentials.verify_user(username,password)
    return check_user

def main():
    print("Greetings!What is your name?")
    username = input()

    print(f"Dear {username}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new account,li -log in ex -exit the user list ")

        short_code = input().lower()
     # create and save new user
        if short_code == 'cc':
            print("New User")
            print("-"*10)

            print("Username ....")
            username = input()

            print("Password ...")
            password = input()

            save_users(create_user(username, password))
            print('\n')
            print(
                f"Your account has been created successfully.Your username is {username} and your password is {password}")
            print('\n')

        elif short_code == "li":
            print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("UserName: ")
        password = input("password: ")
        if user_exists(username,password):
            print(f"Greetings! {username}.Welcome,You have successfully now logged in")  
            print('\n')
            
            #create and save new credential
            while True:
             print("Use these short codes:\n cnc - Create a new credential \n dc - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
             short_code = input().lower().strip()
             if short_code == "cnc":
              print("Create New Credential")
              print("."*20)
              print("Account name ....")
              account = input().lower()
              print("Your Account username")
              userName = input()
              print("Your Password")
              Password = input()
              (account, userName, Password)
              print('\n')
              print(
              f"New Credentials for '{account}'  has been created \n")
              print('*'*10)
             
        elif short_code == 'dc':
         if User.display_Credentials():
             print("Here is a list of all your credentials")
             for credential in User.display_Credentials():
                 print(f"{credential.account}")
                 print('\n')
             
             while True:
                print(" TP - To type your own password if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    print(f"Your Own password now is {password}")
                if password_Choice == 'gp':
                    password = generate_Password()
                    print(f"You have successfully generated your own password")
                    break

        elif short_code == "ex":
            print("Adios .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == "__main__":
    main()
