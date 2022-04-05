# CAPS LOCK DAY is over!

# October 22nd is CAPS LOCK DAY. Apart from that day, every sentence should be lowercase, so write a function to normalize a sentence.

# Create a function that takes a string. If the string is all uppercase characters, convert it to lowercase and add an exclamation mark at the end.

# Examples
# normalize("CAPS LOCK DAY IS OVER") ➞ "Caps lock day is over!"
# normalize("Today is not caps lock day.") ➞ "Today is not caps lock day."
# normalize("Let us stay calm, no need to panic.") ➞ "Let us stay calm, no need to panic."


def normalize(txt):
    var=txt.capitalize()
    return(var)

print(normalize("Let us stay calm, no need to panic."))

# Emphasise the Words

# The challenge is to recreate the functionality of the title() method into a function called emphasise(). The title() method capitalises the first letter of every word and lowercases all of the other letters in the word.

# Examples
# emphasise("hello world") ➞ "Hello World"
# emphasise("GOOD MORNING") ➞ "Good Morning"
# emphasise("99 red balloons!") ➞ "99 Red Balloons!"

def emphasise(txt):
    var=txt.title()
    return(var)
print(emphasise("GOOD MORNING"))


