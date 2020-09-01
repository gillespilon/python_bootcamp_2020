#! /usr/bin/env python3

'''
integer_between_1_and_5.py

./integer_between_1_and_5.py
'''


input_value = int(input('Give me a number between 1 and 5, inclusive. > '))
if input_value == 1:
    print('one')
elif input_value == 2:
    print('two')
elif input_value == 3:
    print('three')
elif input_value == 4:
    print('four')
elif input_value == 5:
    print('five')
else:
    print('That is not a number between 1 and 5, inclusive.')
