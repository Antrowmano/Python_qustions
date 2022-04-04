# Get the Area of a Country

# Create a function that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.

# Examples
# area_of_country("Russia", 17098242) ➞ "Russia is 11.48% of the total world's landmass"
# area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass"
# area_of_country("Iran", 1648195) ➞ "Iran is 1.11% of the total world's landmass"



# def area_of_country(name, area):
#     total=148940000
#     var=round(area*(100/total))
#     return(f"{name} is {var}% of the total world's landmass")

# print(area_of_country('india', 9372610))


# Check If It's a Title String    

# Check if a string txt is a title text or not. A title text is one which has all the words in the text start with an upper case letter.

# Examples
# check_title("A Mind Boggling Achievement") ➞ True
# check_title("A Simple Python Program!") ➞ True
# check_title("Water is transparent") ➞ False



def check_title(txt):
    for i in txt:
        if i[0].upper():
            return True
        else:
            return False

print(check_title('Water is transparent'))


