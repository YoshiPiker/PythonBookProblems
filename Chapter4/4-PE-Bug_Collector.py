'''
Created on Jun 6, 2016

@author: Alexander
'''
#This program collects the amount of bugs found
#in a five day span

day_span=5
#The total amount of bugs
total=0

#Loop for each day
for curr_day in range(day_span):
    print('On day',curr_day+1,"",end='')
    total+=int(input('how many bugs were collected? '))
print('The total amount of bugs found in a',day_span,\
      'day span is',total)