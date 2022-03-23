#  Is the String Odd or Even?

# odd_or_even("apples") ➞ True
# # The word "apples" has 6 characters.
# # 6 is an even number, so the program outputs True.

# odd_or_even("pears") ➞ False
# # "pears" has 5 letters, and 5 is odd.
# # Therefore the program outputs False.

# odd_or_even("cherry") ➞ True



# def odd_or_even(var):
#     var=input(str("enter your input: "))
#     length=len(var)
#     if (length % 2)==0:
#         print ('True')
#     else:
#         print('False')

# odd_or_even('')


# Front 3 - Slice Check Repeat Concatenate

# Create a function that takes a string; 
# we'll say that the front is the first three characters of the string.
#  If the string length is less than three characters, the front is whatever is there. 
# Return a new string, which is three copies of the front.

# front3("Python") ➞ "PytPytPyt"
# front3("Cucumber") ➞ "CucCucCuc"
# front3("bioshock") ➞ "biobiobio"

# def front3(txt):
#     txt=input('enter your input: ')
#     var=(txt[:3])
#     print(str(var*3))

# front3('')





[Incomplete]
# Convert Number to String of Dashes
# Create a function that takes a number (from 1 - 60) and returns a corresponding string of hyphens.

def num_to_dashes(num):
    num = input('Enter the num: ')
    var=int('-')
    print(num*var)
    
num_to_dashes(2)


# var = '-'
# num = 2

# print(num*var)

