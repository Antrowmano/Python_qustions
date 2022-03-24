# Is the Word Singular or Plural?

# Create a function that takes in a word and determines whether or not it is plural.
# A plural word is one that ends in "s".

# Example
# is_plural("changes") ➞ True
# is_plural("change") ➞ False
# is_plural("dudes") ➞ True
# is_plural("magic") ➞ False

def is_plural(word):
    word=input("Enter your input: ")
    print(word.endswith('s'))
is_plural('')

# Is the Last Character an "N"?

# Create a function that takes a string (a random name). 
# If the last character of the name is an "n", return True, otherwise return False.

# is_last_character_n("Aiden") ➞ True
# is_last_character_n("Piet") ➞ False
# is_last_character_n("Bert") ➞ False
# is_last_character_n("Dean") ➞ True

def is_last_character_n(word):

    word=input("Enter your input: ")
    print(word.endswith('n'))

is_last_character_n('')


# Burrrrrrrp

# Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function.

# long_burp(3) ➞ "Burrrp"
# long_burp(5) ➞ "Burrrrrp"
# long_burp(9) ➞ "Burrrrrrrrrp"

def long_burp(num):
    num=int(input("enter the num: "))
    var = (num*'r')
    print(f"Bu{var}p")
long_burp('')

# Char-to-ASCII

# Create a function that returns the ASCII value of the passed in character.

# ctoa("A") ➞ 65
# ctoa("m") ➞ 109
# ctoa("[") ➞ 91
# ctoa("\") ➞ 92

def ctoa(char):
    char=input("enter your input: ")
    var= ord(char)      ------------------>ord is used for char to ASCII value
    print(var)
ctoa('')

# Stuttering Function

# Write a function that stutters a word as if someone is struggling to read it. 
# The first two letters are repeated twice with an ellipsis ... 
# and space after each, and then the word is pronounced with a question mark ?.

# stutter("incredible") ➞ "in... in... incredible?"
# stutter("enthusiastic") ➞ "en... en... enthusiastic?"
# stutter("outstanding") ➞ "ou... ou... outstanding?"

def stutter(word):
    word=input("Enter your input: ")
    var=word[:2]
    print(f"{var}... {var}... {word}?")
stutter('')