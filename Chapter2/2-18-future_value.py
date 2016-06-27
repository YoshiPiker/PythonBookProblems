'''
Created on Jun 4, 2016

@author: Alexander
'''
#Get the desire future value.
Future_value = float(input('Enter the desired future value: '))

#Get he annual interest rate.
rate = float(input('Enter the annual interest rate: '))

#Get the number of years that the money will appreciate.
years = int(input('Enter the number of years the money will grow: '))

#Calculate the amount needed to deposit.
present_value = future_value/(1.0 + rate)**years

#Displays the amount needed to deposit.
print('You will need to deposit this amount:', present_value)