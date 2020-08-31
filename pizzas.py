#! /usr/bin/env python3

'''
pizzas.py

./pizzas.py
'''


pieces_per_pizza = int(input('How many pieces in a pizza? > '))
number_people = int(input('How many people want pizza? > '))
number_pieces_per_person = int(input('How many pieces per person? > '))
total_number_pieces = number_people * number_pieces_per_person
number_whole_pizzas = (total_number_pieces + 5) // pieces_per_pizza
pieces_extra = number_whole_pizzas * 6 - total_number_pieces
print(
    'Number of pizzas to order = ', number_whole_pizzas,
    'and ', pieces_extra, 'remaining pieces.'
)
