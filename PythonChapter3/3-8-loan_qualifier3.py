'''
Created on Jun 4, 2016

@author: Alexander
'''
#This program determines whether a bank customer
#qualifies for a loan.

min_salary = 30000.0 #The minimum annual salary
min_years = 2        #The minimum years on the jon

#Get the customer's annual salary.
salary = float(input('Enter your annual salary:'))

#Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
                         'years employed: '))

#Determine whether the customer qualifies.
if salary >= min_salary or years_on_job >= min_years:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan')