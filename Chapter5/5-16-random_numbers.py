'''
Created on Jun 9, 2016

@author: Alexander
'''
#This program displays a random Number
#in the range of 1 through 10.
import random

def main():
    #Get a random number.
    number = random.randint(1,10)
    #Display the number.
    print('The number is', number)
    
#Call the main Function.
main()