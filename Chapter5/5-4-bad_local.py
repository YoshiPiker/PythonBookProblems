'''
Created on Jun 6, 2016

@author: Alexander
'''
#Definition of the main function.
def main():
    get_name()
    print('Hello',name) #This causes an Error!
    
#Definition of the get_name function.
def get_name():
    name=input('Enter you name: ')
    
#Call the main function.
main()