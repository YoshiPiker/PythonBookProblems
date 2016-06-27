'''
Created on Jun 4, 2016

@author: Alexander
'''
number=int(input('Enter a number ranging 1-7: '))
if number>7 or number<1:
    print('Error')
else:
    if number == 1:
        print('Monday')
    elif number ==2:
        print('Tuesday')
    elif number == 3:
        print('Wednesday')
    elif number == 4:
        print('Thursday')
    elif number == 5:
        print('Friday')
    elif number ==6:
        print('Saturday')
    else:
        print('Sunday')