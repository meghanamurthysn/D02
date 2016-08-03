#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def horiz():
	print('+','- '*4, end = '')

def horiz1():
	print('|',' '*8, end = '')

def do_twice(func):
	func()
	func()

def do_four(func):
	do_twice(func)
	do_twice(func)
	
def horiz_first():
	do_twice(horiz)

def horiz_next():
	do_twice(horiz1)
	print("|")

def horiz_next1():
	do_four(horiz1)
	print("|")
	
def two_simp():
	horiz_first()
	print("+")
	do_four(horiz_next)
	
def two_by_two():
	do_twice(two_simp)
	horiz_first()
	print("+")

def four_simp():
	do_four(horiz)
	print("+")
	do_four(horiz_next1)

def four_by_four():
	do_four(four_simp)
	do_four(horiz)
	print("+")
	
# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    two_by_two()
    four_by_four()
if __name__ == "__main__":
    main()