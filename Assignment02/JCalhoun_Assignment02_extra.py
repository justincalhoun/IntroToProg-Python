#!/usr/bin/python3

"""
Name:       Justin Calhoun
Course:     IT FDN 100 A Au 18
            Foundations of Programming: Python
Desc:       Assignment02 - Create a script that asks the user to input
            two numbers, then prints out the sum, difference, product,
            and quotient.
            This is the "extra" version, which splits out input
            validation to a separate function and uses an OrderedDict to
            allow looping of the output text.
"""

# Imports
#   operator - used to make it easier to put the math and output in a
#       function.
#   collections.OrderedDict - because I'm using Python 3.5, dicts do not
#       maintain their order; that feature was introduced in 3.6 and
#       became a language specification in 3.7.  So I'm using this to
#       force it.
import operator
from collections import OrderedDict as odict

def main():
    # Introduce the script and it's purpose.
    print("Simple Numerical Operations Script\n")
    print(
        "This python script takes two numbers, provided by you, and outputs a "
        "variety of mathematical comparisons between them.\n"
    )

    # Ask the user for two values and validate the input.
    # If what we get back isn't a number, the function will ask again.
    valueOne = InputValidation("first")
    valueTwo = InputValidation("second")

    # Just print a space, it looks nicer.
    print()

    # Create an orderd dictionary of operators.
    odOpers = odict()
    odOpers['sum'] = operator.add
    odOpers['difference'] = operator.sub
    odOpers['product'] = operator.mul
    odOpers['quotient'] = operator.truediv

    # Now, we iterate over the Ordered Dictionary.  For each key/value
    # pair, we have both the printed name of the operation and an easy
    # way to do the math.  By separating out the operators like this, we
    # can iterate instead of typing out four different operations, or a
    # big conditional that determines which math to do.  We do, however,
    # still have to check for valueTwo being zero and behave differently
    # for division.
    for label, oper in odOpers.items():
        if label == 'quotient' and valueTwo == 0:
            print("Sadly, {0} cannot be divided by {1}...".format(
                valueOne,
                valueTwo
                )
            )
        else:
            print("The {0} of {1} and {2} is {3}".format(
                label,
                valueOne,
                valueTwo,
                oper(valueOne, valueTwo)
                )
            )

    # Inform the user we're done
    print("\nScript Complete!\n")



# This is our function for validating the user's input.  It takes in a
# string for the name of the ordinal (first, second) so we can
# appropriately prompt the user, and returns a float.
def InputValidation(strOrdinal):
    # This while loop will keep asking the user for input until we get
    # back a string we can turn into a float.  It will remain True
    # forever, but upon successful input from the user, we'll break it.
    while True:
        # Use try and except to validate the user's input.  If they give
        # us something that can't be typed as a float, Python will
        # return a ValueError exception.  We'll use that opportunity to
        # inform the user that we need a number, and the loop will
        # continue until fltInput has the type of data we're looking for.
        try:
            fltInput = float(
                input("Please provide the {0} number: ".format(strOrdinal))
            )
        except ValueError:
            # This happens if they put in something that's not a number.
            # The continue statement returns us to the top of the loop.
            print("That was not recognized as a number.  Please try again.\n")
            continue
        else:
            # No exception, so we can break the loop and return the data.
            break
    return(fltInput)



#Run main function
if __name__ == '__main__':
    main()
