'''
Created on Jun 4, 2016

@author: Alexander
'''
#This program gets three test scores and displays
#their average. It congratulates the user if the
#average is a high score

#The high score variable holds the value that is
#considered a high score.
high_score = 95

#Get the three test score
test1= int(input('Enter the score for test 1: '))
test2= int(input('Enter the score for test 2: '))
test3= int(input('Enter the score for test 3: '))

#Calculate the average test score.
average = (test1+test2+test3)/3

#print the average
print('The average score is', average)

#if the average is a high score,
#congratulate the user.
if average >=high_score:
    print('Congratulations!')
    print('That is a great average!')