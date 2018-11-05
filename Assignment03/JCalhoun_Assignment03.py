#!/usr/bin/python3

########################################################################
#
# Name:     Justin Calhoun
# Course:   IT FDN 100 A Au 18
#           Foundations of Programming: Python
# Desc:     Assignment03 - Create a new program that asks the user for
#           the name of a household item, and then asks for its
#           estimated value. Store, both pieces of data in a text file
#           called, HomeInventory.txt
#
########################################################################

# Import Modules
#       sys     - Read arguments
#       os      - Just using it to clear the terminal
#       re      - Validate the price strings
import sys, os, re

# Main Function
def main():
    # Setup the Price Validation regex up front
    rgxPrice = re.compile("^([0-9]+\.[0-9]{2}$|^[0-9]+)$")

    # Check to see if the file exists
    try:
        f = open("HomeInventory.txt", "r")
        f.close()
    except FileNotFoundError:
        # If not, create it and add the headers
        f = open("HomeInventory.txt", "a")
        f.write("Name, Price\n")

    # Determine if any arguments have been passed
    if (len(sys.argv) > 1):
        # If so, work in one-shot mode
        # We're looking for two values only
        if (len(sys.argv) == 3):
            # Store the first arg as the new item name
            inName = sys.argv[1]

            # Store the second arg as the new item price
            inPrice = sys.argv[2]

            # Validate the price
            if (rgxPrice.match(inPrice)):
                # The regex checks out, standardize in two-decimal format
                inPrice = "{0:.2f}".format(float(inPrice))

                # Write the data to the file
                f = open("HomeInventory.txt", "a")
                f.write("{0}, {1}\n".format(inName, inPrice))
                f.close()

                # Inform the user that the data was added and exit
                print("Added ({0}, {1}) to HomeInventory.txt".format(
                        inName,
                        inPrice)
                )
                return

        # We should only end up here if we got args we can't use
        print("Usage: JCalhoun_Assignment03.py <ItemName> <ItemPrice>\n\n"
              "ItemName can be enclosed in quotes for multi-word names.\n"
              "ItemPrice should be in standard two-decimal format with no "
              "currency symbols.\n\n"
              "For interactive mode, run with no arguments."
        )
        return

    else:
        # If not, work in interactive mode

        # Clear the screen
        os.system("cls||clear")

        # Introduce the script to the user
        print(
            "Welcome to the Home Inventory script. This script allows you to "
            "add new items and their prices to the file HomeInventory.txt. "
            "Simply follow the prompts to add as many new items as you like! "
            "\n\n"
            "When you are finished, you can type 'Exit' at any prompt to end "
            "the program."
            "\n\n"
        )
        # Enter to continue, Exit to quit
        inConfirm = input("Press 'Enter' to begin, or type 'Exit' to quit...")
        if (inConfirm.lower() == "exit"):
            print("\n\nThanks for using this program!  Exiting...")
            return

        # Main Interactive Loop. This is where the work gets done.
        newItems = 0
        while (True):
            # Clear the screen
            os.system("cls||clear")

            # Display up to the last 5 items entered
            # Read the current file into a list
            with open('HomeInventory.txt') as f:
                lines = f.read().splitlines()
            f.close()
            # Find out if we have more than 5 items to display. If not,
            # we'll display them all.
            if (len(lines[1:]) > 5):
                # Just get the last 5 items and print them
                print("Latest entries:\n")
                for i in lines[(len(lines) - 5):]:
                    print(i)
            elif (len(lines[1:]) == 0):
                # This occurs when there's just the header.  So, tell
                # the user there's no data.
                print("HomeInventory has no data yet.")
            else:
                # This occurs if there are between 1-5 items, so we'll
                # print them all.
                print("Latest entries:\n")
                for i in lines[1:]:
                  print(i)

            print() # Print a space

            # Ask for the new item name
            inName = input("What's the name of the item? ")
            # If it's 'exit', break the Main Interactive Loop
            if (inName.lower() == "exit"):
                break

            # Ask for and validate the new item price
            while (True):
                inPrice = input("How much does it cost? ")
                if (rgxPrice.match(inPrice)):
                    # The regex checks out, standardize in two-decimal
                    # format.
                    inPrice = "{0:.2f}".format(float(inPrice))
                    break
                elif (inPrice.lower() == "exit"):
                    # Break out of this inner loop. We'll have to do it
                    # again on the outside to actually end for the user.
                    break
                else:
                    print(
                        "\nI'm sorry, that doesn't seem like a valid price. "
                        "Price should be in standard two-decimal format with "
                        "no currency symbols.\n"
                    )
            # It's a double-check to break, but we'll do it so as not to
            # have to build a separate function for just this right now.
            if (inPrice.lower() == "exit"):
                break

            # Write the new data to the file
            f = open("HomeInventory.txt", "a")
            f.write("{0}, {1}\n".format(inName, inPrice))
            f.close()
            newItems += 1

        # Display a summary of the work done and exit
        # Clear the screen
        os.system("cls||clear")

        # Print Summary and exit
        print("Exiting at user request!")
        print("Added {0} new items this session.".format(newItems))
        print()
        return



# Run Main Function
if (__name__ == '__main__'):
    main()
