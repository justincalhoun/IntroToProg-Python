#!/usr/bin/python3
"""
Name:       Justin Calhoun
Course:     IT FDN 100 A Au 18
            Foundations of Programming: Python
Desc:       Assignment02 - Create a script that asks the user to input
            two numbers, then prints out the sum, difference, product,
            and quotient.
"""

def main():
    # Introduce the script and it's purpose
    print("Simple Numerical Operations Script\n")
    print(
        "This python script takes two numbers, provided by you, and outputs a "
        "variety of mathematical comparisons between them.\n"
    )

    # These while loops will keep asking the user for input until we
    # get back something we can turn into a float.  This loop is always
    # TRUE, and will continue until we get valid input to break it.
    while True:
        # Here, we use try and except to validate the user's input.  If
        # they give us something that can't be stored as a float,
        # Python will return a ValueError exception.  We'll use that
        # opportunity to inform them that we need a number, and the loop
        # will continue until valueOne has the type of data we're
        # looking for.
        try:
            valueOne = float(input("Please provide the first number: "))
        except ValueError:
            # This happens if they put in something that's not a number.
            print("That was not recognized as a number.  Please try again.\n")
            continue
        else:
            break

    # Second verse, same as the first!
    while True:
        try:
            valueTwo = float(input("Please provide the second number: "))
        except ValueError:
            print("That was not recognized as a number.  Please try again.\n")
            continue
        else:
            break

    # Now that we have two float values, we can perform all of the math
    # and display the results to the user.

    # First, the sum
    print("The sum of {0} and {1} is {2}".format(
        valueOne,
        valueTwo,
        valueOne + valueTwo
        )
    )

    # Second, the difference
    print("The difference of {0} and {1} is {2}".format(
        valueOne,
        valueTwo,
        (valueOne - valueTwo)
        )
    )

    # Third, the product
    print("The product of {0} and {1} is {2}".format(
        valueOne,
        valueTwo,
        (valueOne * valueTwo)
        )
    )

    # Finally, the quotient
    # We need to make sure valueTwo isn't a zero here, or we'll get an
    # error.
    if valueTwo == 0:
        print("Sadly, {0} cannot be divided by {1}...".format(
            valueOne,
            valueTwo
            )
           )
    else:
        print("The quotient of {0} and {1} is {2}".format(
            valueOne,
            valueTwo,
            (valueOne / valueTwo)
            )
        )



#Run main function
if __name__ == '__main__':
    main()
