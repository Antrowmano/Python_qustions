# Pluralize!


# Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

# Examples
# pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
# pluralize(["table", "table", "table"]) ➞ { "tables" }
# pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

import collections

def pluralize(lst):
    c = sorted(lst)
    d = collections.Counter(c)
    print(d)

print(pluralize(["cow", "pig", "cow", "cow"]))



# Sum of Resistance in Series Circuits

# When resistors are connected together in series, the same current passes through each resistor in the chain and the total resistance, RT, of the circuit must be equal to the sum of all the individual resistors added together. That is:
# RT = R1 + R2 + R3 ...
# Create a function that takes an array of values resistance that are connected in series, and calculates the total resistance of the circuit in ohms. The ohm is the standard unit of electrical resistance in the International System of Units ( SI ).

# Examples
# series_resistance([1, 5, 6, 3]) ➞ "15 ohms"
# series_resistance([16, 3.5, 6]) ➞ "25.5 ohms"
# series_resistance([0.5, 0.5]) ➞ "1.0 ohm"

def series_resistance(lst):
    total = sum(lst)
    if total >= 1:
        return(f"{total} ohms")
    else:
        return(f"{total} ohm")
print(series_resistance([16, 3.5, 6]))



