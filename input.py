#!/usr/bin/env python
# Create a program that asks the user to enter their name
# and their age. Print out a message addressed to them that
# tells them the year that they will turn 100 years old 


name = input("Give Your Name: ")
age =int( input("How old are You: "))
year = ((2017 - age) + 55)

print(name + " will be 55 years old in the year " + str(year))
