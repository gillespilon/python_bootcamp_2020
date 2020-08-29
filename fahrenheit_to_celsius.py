#! /usr/bin/env python3

'''
fahrenheit_to_celsius.py

./fahrenheit_to_celsisus.py
'''


# Ask the user for the temperature in Fahrenheit and print this in Celsisu
temperature_fahrenheit = \
        float(input('What is the temperature in degrees F? > '))
# print(temperature_fahrenheit)
temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
# print(temperature_celsius)
print('You entered a temperature of ', temperature_fahrenheit, ' degrees F.')
print('The temperature is ', temperature_celsius, ' degrees C.')
