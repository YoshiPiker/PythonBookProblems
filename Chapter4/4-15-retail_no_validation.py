'''
Created on Jun 6, 2016

@author: Alexander
'''
#This program calculates retail prices.

mark_up = 2.5 #The markup percentage
another = 'y' #Variable to control the loop.

#process one or more items.
while another == 'y' or another == 'Y':
    #Get the iterm's wholesale cost.
    wholesale = float(input("Enter the item's "+
                            "wholesale cost: "))
    
    #Calculate the retail price.
    retail = wholesale * mark_up
    
    #Display the retail price
    print('Retail price: $', format(retail,',.2f'))
    
    #Do this again?
    another = input('Do you have another item? ' +\
                    '(Enter y for yes): ')