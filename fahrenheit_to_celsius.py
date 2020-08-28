#! /usr/bin/env python3

'''
fahrenheit_to_celsius.py
'''


# Ask the user for the radius of a circle and then print the area

temperature_fahrenheit = \
        float(input('What is the temperature in degrees F? > '))
# print(temperature_fahrenheit)
temperature_celsius = (temperature_fahrenheit - 32) * 5 / 9
# print(temperature_celsius)
print('You entered a temperature of ', temperature_fahrenheit, ' degrees F.')
print('The temperature is ', temperature_celsius, ' degrees C.')
