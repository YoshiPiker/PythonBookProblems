'''
Created on Jun 9, 2016

@author: Alexander
'''
#This program the rolling of dice
import random

#Constants for the minimum and maximum random numbers
MIN = 1
MAX = 6

def main():
    #Creates a variable to control the loop
    again = 'y'
    
    #Simulate rolling the dice
    while again == 'y' or again == 'Y':
        print('Rolling the dice ...')
        print('Their values are:')
        print(random.ranint(MIN,MAX))
        print(random.ranint(MIN,MAX))
        
        #Do another roll of the dice?
        again = input('Roll them again? (y=yes): ')
        
#Call the main function.
main()