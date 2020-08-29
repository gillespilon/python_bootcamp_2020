#! /usr/bin/env python3

'''
sum_of_two_integers.py

./sum_of_two_integers.py
'''


# Ask the user for two integers and print their sum
integer_one = int(input('What is your first integer? > '))
integer_two = int(input('What is your second integer? > '))
sum_of_two_integers = integer_one + integer_two
print(
    'Sum of', integer_one,
    'and', integer_two,
    'is', sum_of_two_integers
)
print(
    'The sum of ' + str(integer_one) + ' plus ' + str(integer_two) + ' is '
    + str(sum_of_two_integers) + '.'
)
