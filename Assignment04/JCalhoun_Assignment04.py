#!/usr/bin/python3

########################################################################
#
# Name:     Justin Calhoun
# Course:   IT FDN 100 A Au 18
#           Foundations of Programming: Python
# Desc:     Assignment04 - Create new program that asks the user for the
#           name of a household item, and then asks for its estimated
#           value. (This project is similar to the last one!)
#           Ask the user for new entries and stores them in the
#           2-dimensional Tuple.
#           Ask the user, when the program exits, if they would like to
#           save/add the data to a text file called, HomeInventory.txt.
#
########################################################################

# Import Modules
#   os      - Using this to clear the terminal
#   re      - Regex, using this to validate the price strings
import os, re

# Main Function
def main():
    ### Setup ###

    # Setup the Price Validation regex up front.
    # In plain English, this regex looks for a string of any number of
    # digits, a decimal point, and then two more digits; or a string
    # which is any number of digits; or a string that is a decimal point
    # and then two digits.
    rgxPrice = re.compile("^([0-9]+\.[0-9]{2}|[0-9]+|\.[0-9]{2})$")

    # Check to see if the HomeInventory file exists, and read it into a
    # 2D tuple.  We'll use this to display a reminder to the user of the
    # last few items added in previous sessions.
    try:
        # Initialize an empty tuple
        tplPrevData = ()
        # Read the file
        with open("HomeInventory.txt", "r") as f:
            # Iterate over the lines
            for line in f:
                # Strip and split into a list, convert to tuple
                tplTemp = tuple(line.strip().split(', '))
                # If it's the header, ignore it, otherwise, add to the
                # 2D tuple
                if (tplTemp != ('Name', 'Price')):
                    tplPrevData += (tplTemp),
    except FileNotFoundError:
        # If the file didn't exist, create it and add the header row
        f = open("HomeInventory.txt", "a")
        f.write("Name, Price\n")

    ### Introduction ###

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

    ### Main Interactive Loop.  This is where the work gets done. ###

    # Initialize an empty tuple
    tplNewData = ()
    while (True):
        # Clear the screen.  On Windows, 'cls' will clear the terminal.
        # On Linux/macOS, 'clear'  will do so.
        os.system("cls||clear")

        # Add the old and new data together, but only the last five items.
        tplDisplayData = (tplPrevData + tplNewData)[-5:]

        # Find out if we have any items to display.  If not, we'll
        # inform the user of such.
        if (len(tplDisplayData) == 0):
            # If there is no data to display yet, say so
            print("HomeInventory.txt has no data yet.")
        else:
            # This occurs if there is any data, and we'll display it all.
            print("Latest Entries:\n")
            # Loop through all items
            for i in tplDisplayData:
                # Unpack the tuple and print
                strName, strPrice = i
                print("{0}, {1}".format(strName, strPrice))

        # Inform the user how many items they've added this session
        print("\nItems added this session: {0}\n".format(len(tplNewData)))

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
                    "\nI'm sorry, that doesn't seem like a valid price. Price "
                    "should be in standard two-decimal format with no "
                    "currency symbols.\n"
                )
        # It's a double-check to break, but we'll do it so as not to
        # have to build a separate function for just this right now.
        if (inPrice.lower() == "exit"):
            break

        # Add the new items as a tuple to the New Data tuple
        tplNewData += (inName, inPrice),

    ### Clean Up ###

    # Once the user breaks the main interactive loop, we ask them to
    # save their data.

    while (True):
        # See if there is anything to save.
        if (len(tplNewData) == 0):
            # No new data, just exit
            print("Nothing to save, exiting...")
            return
        else:
            # There's something to save, so ask them to.  Remind them of
            # all the work they might lose.
            inSave = input(
                "You have {0} unsaved items; save to HomeInventory.txt before "
                "closing? (y/n) ".format(len(tplNewData))
            )
            # Check their input and behave appropriately
            if ((inSave.lower() == "y") or (inSave.lower() == "yes")):
                # They said yes, let's save.
                # First, open the file.
                f = open("HomeInventory.txt", "a")

                # Iterate over the new data
                for i in tplNewData:
                    # Unpack the tuple
                    strName, strPrice = i
                    # Write the data to the file
                    f.write("{0}, {1}\n".format(strName, strPrice))

                # Close the file
                f.close()

                # Inform the user we're done and exit
                print("Data saved!  Exiting...")
                return
            elif ((inSave.lower() == "n") or (inSave.lower() == "no")):
                # They said no?  Ok, shut it down.
                print("Exiting without saving...")
                return
            else:
                # Bad input.
                print(
                    "\nI'm sorry, that doesn't seem like a valid response.\n"
                    "Please answer \"Yes\", \"Y\", \"No\", or \"N\".\n"
                )



# Run main function
if __name__ == '__main__':
    main()
