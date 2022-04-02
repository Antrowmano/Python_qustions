# The Reverser!

# The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.

# Examples
# reverse("Hello World") ➞ "DLROw OLLEh"
# reverse("ReVeRsE") ➞ "eSrEvEr"
# reverse("Radar") ➞ "RADAr"

# def reverse(txt):
#     var=txt.swapcase()
#     return(var[::-1])

# print(reverse("ReVeRsE"))


# Characters in Shapes

# Create a function to calculate how many characters in total are needed to make up the shape. You will be given a list of strings which make up a shape in the compiler (i.e. a square, a rectangle or a line).

# Examples
# count_characters([
#   "###",
#   "###",
#   "###"
# ]) ➞ 9

# count_characters([
#   "22222222",
#   "22222222",
# ]) ➞ 16

# count_characters([
#   "------------------"
# ]) ➞ 18

# count_characters([]) ➞ 0
# count_characters(["", ""]) ➞ 0

# lst =["antrow","mano","tino","allen"]

from ast import Str


def count_characters(*antros):
    a=0
    for i in antros :
        var=(len(i))
        a += var
    return (a)

print(count_characters("antrow","mano","tino","allen"))


def example(*args,**kwargs):
    print(args)
    print(kwargs)
    
example("antrow","mano","tino","allen",a=1,b=2,c=5)

# def double_char(txt):
#     for i in txt:
