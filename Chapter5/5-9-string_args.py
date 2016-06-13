'''
Created on Jun 8, 2016

@author: Alexander
'''
#This program demonstrates passing two String
#arguments to a function.

def main():
    first_name = input('Enter you first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is')
    reverse_name(first_name, last_name)
    
def reverse_name(first, last):
    print(last, first)

#Call the main function.
main()