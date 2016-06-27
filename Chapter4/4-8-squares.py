'''
Created on Jun 5, 2016

@author: Alexander
'''
#This program uses a loop to display a 
#table showing the numbers 1 through 10
#and their squares.

#Print the table headings.
print('Number\tSquare')
print('-'*15)

#Print the numbers 1 through 10
#and their squares.
for number in range(1,11):
    square = number**2
    print(number, '\t',square)