'''
Created on Jun 5, 2016

@author: Alexander
'''
#This program converts the speeds 60 kph
#through 130 kph (in 10 kph increments)
#to mph

start_speed = 60
end_speed =131
increment = 10
conversion_factor = 0.6214

#print the table headings
print('KPH\t MPH')
print('-'*15)

#print the speeds.
for kph in range(start_speed, end_speed, increment):
    mph =kph * conversion_factor
    print(kph, '\t', format(mph,'.1f'))