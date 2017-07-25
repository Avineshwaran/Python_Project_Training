#!/usr/bin/env python
# input if types int equality comparison numbers mod 
# Ask the user for a number. Depending on whether the
# number is even or odd, print out an appropriate message
# to the user. 
# Hint: how does an even / odd number react differently when divided by 2?
#  


a = int(input("Enter the Number :") )

if (a != 0):
	if (a%2 == 0):
		print (a , "This is an Even number")
	else:
		print (a , "This is an Odd number")
