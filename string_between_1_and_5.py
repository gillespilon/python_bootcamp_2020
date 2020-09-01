#! /usr/bin/env python3

'''
string_between_1_and_5.py

./string_between_1_and_5.py
'''


input_value = input('Give me a number between 1-5, inclusive, as string > ')
if input_value == 'one':
    print(1)
elif input_value == 'two':
    print(2)
elif input_value == 'three':
    print(3)
elif input_value == 'four':
    print(4)
elif input_value == 'five':
    print(5)
else:
    print('That is not a number between 1 and 5, inclusive.')
