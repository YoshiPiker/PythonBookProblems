'''
Created on Jun 9, 2016

@author: Alexander
'''
#This program simulates 10 tosses of a coin.
import random

#constants
HEAD = 1
TAILS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        #Simulate the coin toss.
        if random.randint(HEAD,TAILS)==HEAD:
            print('Heads')
        else:
            print('Tails')
#Call the main Function
main()