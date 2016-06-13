'''
Created on Jun 8, 2016

@author: Alexander
'''
#Create a global Variable
number = 0

def main():
    global  number 
    number = int(input('Enter a number: '))
    show_number()
    
def show_number():
    print('The number you entered is', number)
    
#Call the main function.
main()