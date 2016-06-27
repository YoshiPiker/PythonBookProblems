'''
Created on Jun 4, 2016

@author: Alexander
'''
#This program demonstrates how a floating-Point
#number can be displayed as currency.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print('Your annual pay is $', \
      format(annual_pay, ',.2f'), \
      sep='')