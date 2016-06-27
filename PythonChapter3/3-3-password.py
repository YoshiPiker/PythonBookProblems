'''
Created on Jun 4, 2016

@author: Alexander
'''
#This program compares two strings.
#Get a password from the user.
password = input('Enter the password:')

#determine whether the correct password
#was entered.
if password == 'prospero':
    print('Password accepted')
else:
    print('Sorry, that is the wrong password.')