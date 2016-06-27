'''
Created on Jun 4, 2016

@author: Alexander
'''
#This program demonstrates how a floating-Point
#number can be formatted.
amount_due = 5000.0
monthly_payment = amount_due/12
print('The monthly payment is', \
      format(monthly_payment, '.2f'))