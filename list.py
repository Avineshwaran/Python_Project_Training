#!/usr/bin/env python
#Take a list, say for example this one:
#	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the 
#list that are less than 5.
#Extras:
#   Instead of printing the elements one by one, make a new list 
#   that has all the elements less than 5 from this list in it 
#   and print out this new list.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list = []

b = int(raw_input("Enter a Number:"))

for i in a:
	if(i<=b):
		new_list.append(i)
print(new_list)
