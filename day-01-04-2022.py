# Return the Sum of Two Numbers

# Create a function that takes two numbers as arguments and returns their sum.

# Examples
# addition(3, 2) ➞ 5
# addition(-3, -6) ➞ -9
# addition(7, 3) ➞ 10

def addition(a, b):
	return(a+b)

print(addition(-2,-4))

# Return the Next Number from the Integer Passed

# Create a function that takes a number as an argument, increments the number by +1 and returns the result.

# Examples
# addition(0) ➞ 1
# addition(9) ➞ 10
# addition(-3) ➞ -2

def addition(num):
    return(num+1)
print(addition(9))


# Convert Minutes into Seconds

# Write a function that takes an integer minutes and converts it to seconds.

# Examples
# convert(5) ➞ 300
# convert(3) ➞ 180
# convert(2) ➞ 120

def convert(minutes):
    return(minutes*60)

print(convert(2))

# Area of a Triangle

# Write a function that takes the base and height of a triangle and return its area.

# Examples
# tri_area(3, 2) ➞ 3
# tri_area(7, 4) ➞ 14
# tri_area(10, 10) ➞ 50

def tri_area(base, height):
    return(int((base*height)/2))

print(tri_area(7,4))


# Buggy Code (Part 1)
# Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.

# Examples
# cubes(3) ➞ 27
# cubes(5) ➞ 125
# cubes(10) ➞ 1000

# They gave like is find it the bug
# def cubes(a):
#     	retunr a ** 3

def cubes(a):
	return(a ** 3)

print(cubes(3))


# Convert Hours into Seconds

# Write a function that converts hours into seconds.

# Examples
# how_many_seconds(2) ➞ 7200
# how_many_seconds(10) ➞ 36000
# how_many_seconds(24) ➞ 86400


def how_many_seconds(hours):
    return(hours *3600)

print(how_many_seconds(10))

# Return the Remainder from Two Numbers

# There is a single operator in Python, capable of providing the remainder of a division operation. 
# Two numbers are passed as parameters. 
# The first parameter divided by the second parameter will have a remainder, possibly zero. 
# Return that value.

# Examples
# remainder(1, 3) ➞ 1
# remainder(3, 4) ➞ 3
# remainder(5, 5) ➞ 0
# remainder(7, 2) ➞ 1

def remainder(x, y):
    return(x%y)
print(remainder(1,3))



# Convert Age to Days
# Create a function that takes the age in years and returns the age in days.

# Examples
# calc_age(65) ➞ 23725
# calc_age(0) ➞ 0
# calc_age(20) ➞ 7300

def calc_age(age):
    return(age*365)
print(calc_age(29))
