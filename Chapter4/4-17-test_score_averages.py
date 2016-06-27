'''
Created on Jun 6, 2016

@author: Alexander
'''
#This program averages test scores. it asks the user for the
#number of students and the number of test scores per student.

#Get the number of students.
num_students = int(input('How many students do you have? '))

#Get the number of test scores per student.
num_test_scores = int(input('How many test scores per student? '))

#Determine each student's average test score.
for student in range(num_students):
    #Initialize an accumulator for test score.
    total=0.0
    #Get a student's test scores
    print('Student number',student+1)
    print('-'*15)
    for test_num in range(num_test_scores):
        print('Test number', test_num+1,end='')
        score = float(input(': '))
        #add the score to the accumulator.
        total+=score
        
    #Calculate the aver test score for this student.
    average = total / num_test_scores
    
    #Display the average.
    print("The average for student number", student +1,\
          'is:',average)
    print()