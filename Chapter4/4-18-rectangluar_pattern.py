'''
Created on Jun 6, 2016

@author: Alexander
'''
#This program displays a rectangular Pattern
#of asterisks.
rows=int(input('How many rows? '))
cols=int(input('How many columns? '))

for r in range(rows):
    for c in range(cols):
        print('*',end='')
    print()
