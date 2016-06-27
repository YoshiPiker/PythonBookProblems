'''
Created on Jun 4, 2016

@author: Alexander
'''
#This program compares string with the < operator.
#Get two names from the user.
name1 = input('Enter a name(last name first): ')
name2 = input('Enter another name (last name first): ')

#Display the names in alphabetical order.
print('Here are the names, listed alphabetically')

if name1<name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)