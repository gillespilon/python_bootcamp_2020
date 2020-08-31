#! /usr/bin/env python3

'''
product_of_two_integers.py

./product_of_two_integers.py
'''


# Ask the user for two integers and print their sum
integer_one = int(input('What is your first integer? > '))
integer_two = int(input('What is your second integer? > '))
product_of_two_integers = integer_one * integer_two
print(
    'Sum of', integer_one,
    'and', integer_two,
    'is', product_of_two_integers
)
print(
    'The product of ' + str(integer_one) + ' plus ' + str(integer_two) + ' is '
    + str(product_of_two_integers) + '.'
)
