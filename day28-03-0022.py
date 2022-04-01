# Are the Numbers Equal?

# Create a function that returns True when num1 is equal to num2; otherwise return False.     

# Examples
# is_same_num(4, 8) ➞ False
# is_same_num(2, 2) ➞  True
# is_same_num(2, "2") ➞ False

def is_same_num(num1, num2):
    num1=input("Enter your first input: ")
    num2=input("Enter your second input: ")
    if num1 == num2:
        return True
    else:
        return False
is_same_num('','')


# Is the Number Less than or Equal to Zero?

# Create a function that takes a number as its only argument and returns True if it's less than or equal to zero, otherwise return False.
# Examples
# less_than_or_equal_to_zero(5) ➞ False
# less_than_or_equal_to_zero(0) ➞ True
# less_than_or_equal_to_zero(-2) ➞ True

def less_than_or_equal_to_zero(num):
    num=int(input("Enter the input: "))
    if num <=0:
        return True
    else:
        return False

less_than_or_equal_to_zero('')

# Is the Number Less than or Equal to Zero?

# Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.

# Examples
# name_shuffle("Donald Trump") ➞ "Trump Donald"
# name_shuffle("Rosie O'Donnell") ➞ "O'Donnell Rosie"
# name_shuffle("Seymour Butts") ➞ "Butts Seymour"

def name_shuffle(txt):
    txt=input("Enter the txt: ")
    var=(txt.split())
    print(var.index[1])
    
name_shuffle('')