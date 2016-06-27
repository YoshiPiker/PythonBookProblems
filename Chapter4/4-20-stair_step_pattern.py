'''
Created on Jun 6, 2016

@author: Alexander
'''
#This program displays a stair-step pattern.
num_steps=6

for r in range(num_steps):
    for c in range(r):
        print(' ',end='')
    print('#')