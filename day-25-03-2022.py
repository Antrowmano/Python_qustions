# Luke, I Am Your ...

# Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, 
# return the relation of that person to Luke.

# Person	    Relation
# Darth Vader	father
# Leia	        sister
# Han	        brother in law
# R2D2	        droid

# relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
# relation_to_luke("Leia") ➞ "Luke, I am your sister."
# relation_to_luke("Han") ➞ "Luke, I am your brother in law."

# def relation_to_luke(name):
#     name=input("Enter your number: ")
#     if name == 'Darth Vader':
#         print("Luke, I am your father.")
#     elif name == 'Leia':
#         print("Luke, I am your sister.")
#     elif name == 'Han':
#         print("Luke, I am your brother in law")
#     else:
#         print("worng")
# relation_to_luke('')

# Default Mood

# Create a function that takes in a current mood and return a sentence in the following format: 
# "Today, I am feeling {mood}". However, if no argument is passed, return "Today, I am feeling neutral".

# Examples
# mood_today("happy") ➞ "Today, I am feeling happy"
# mood_today("sad") ➞ "Today, I am feeling sad"
# mood_today() ➞ "Today, I am feeling neutral"

# def mood_today(mood,msg="neutral"):
#     mood=input("Enter your input: ")
#     if mood:
#         print(f"Today, I am feeling {mood}")
#     else:
#         print("Today, I am feeling " + msg)

# mood_today('happy')

print 
    


