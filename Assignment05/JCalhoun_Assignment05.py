#!/usr/bin/python3

########################################################################
#
# Name:     Justin Calhoun
# Course:   IT FDN 100 A Au 18
#           Foundations of Programming: Python
# Desc:     Assignment05 - Create a new script that manages a "ToDo list"
#
########################################################################

# Main Function
def main():
    ### Initial Setup ###
    lstToDo = []                        # The ToDo List
    lstYesNo = ['y','yes','no','n']     # Common yes/no
    # User actions menu items
    lstMenu = [
        {'ID' : 1, 'Option' : 'Show current data.'},
        {'ID' : 2, 'Option' : 'Add a new item.'},
        {'ID' : 3, 'Option' : 'Remove an existing item.'},
        {'ID' : 4, 'Option' : 'Save Data to File.'},
        {'ID' : 5, 'Option' : 'Exit Program.'}
    ]
    # Flag: Save Status.  Are we in sync with the text file?
    blSaveStatus = False

    # Attempt to open the file.  If it doesn't exist, create it.
    try:
        # Open the file.
        f = open('ToDo.txt', 'r')
        for line in f:
            # Split each line into a list.
            lstRow = line.split(',')
            # Construct a dictionary with the elements.
            dctRow = {
                'Action' : lstRow[0].strip(),
                'Priority' : lstRow[1].strip()
            }
            # Append the new row to the ToDo list.
            lstToDo.append(dctRow)
        # Close the file.
        f.close()
        # Data is current with the file, so flag it as such.
        blSaveStatus = True
    except FileNotFoundError:
        # The file didn't exist for some reason. No biggie.  Inform the
        # user and move on.
        print('No "ToDo.txt" file was found.\n')


    ### Processing and Presentation ###
    # Display whatever data we've loaded, if there is anything.
    if len(lstToDo) > 0:
        DisplayToDo(lstToDo)

    # Begin the main user loop.
    while True:
        # Display the menu.
        print('Menu of Options')
        for row in lstMenu:
            print('{0}) {1}'.format(row['ID'], row['Option']))
        print()
        # Ask the user to select an item.
        strChoice = ValidateInput(
            "What would you like to do?",
            [str(dct['ID']) for dct in lstMenu]
        )

        # Conditional Block to do as the user asked.
        if strChoice == '1':
            # Display the current data
            DisplayToDo(lstToDo)
        elif strChoice == '2':
            # Add a new item
            print()
            print('Adding a new item!')
            # Ask the user for the new action item.  No validation,
            # any string is acceptable.
            strAction = input("What's the new action item? ")
            # Ask the user for the priority.
            strPriority = ValidateInput(
                "What's the Priority?",
                ['low', 'med', 'high']
            )
            # Create a dictionary of the user's input
            dctRow = {
                'Action' : strAction.capitalize(),
                'Priority' : strPriority.lower()
            }
            # Append the item to the ToDo list.
            lstToDo.append(dctRow)
            print('{0}, {1} Added!'.format(strAction, strPriority))
            print()
            # We're no longer in sync with the file, flag as such.
            blSaveStatus = False
        elif strChoice == '3':
            # Remove an item.
            # Build a list of valid answers.
            lstIndexes = [str(index) for index,row in enumerate(lstToDo)]
            # Add options to back out.
            lstIndexes += ['c', 'cancel']
            # Ask the question.
            strRemove = ValidateInput(
                "Which item would you like to delete?",
                lstIndexes
            )
            # Conditional to do as they asked.
            if strRemove in ['c', 'cancel']:
                # They changed their mind, remove nothing.
                print('Cancelled!  No items removed.')
                print()
            else:
                # They want to remove something.
                print()
                print('About to remove "{0}, {1}".'.format(
                    lstToDo[int(strRemove)]['Action'],
                    lstToDo[int(strRemove)]['Priority'])
                )
                # Ask them to confirm the deletion.
                strConfirm = ValidateInput(
                    "Are you sure?",
                    lstYesNo
                )
                # Confirmation Conditional.
                if strConfirm in ['y', 'yes']:
                    del lstToDo[int(strRemove)]
                    print('Action removed!')
                    print()
                    # We're no longer in sync with the file, flag as such.
                    blSaveStatus = False
                else:
                    print('Cancelled!  No items removed.')
                    print()
        elif strChoice == '4':
            # Save Data to the file.
            # Confirm the action.
            strConfirm = ValidateInput(
                "Save now?",
                lstYesNo
            )
            # Confirmation Conditional.
            if strConfirm in ['y', 'yes']:
                # Save the file, update the SaveStatus flag to True.
                blSaveStatus = SaveFile('ToDo.txt', lstToDo)
            else:
                # They changed their mind.
                print('Save Canceled.')
                print()
        elif strChoice == '5':
            # Exit the program.
            # Confirm the action.
            strConfirm = ValidateInput(
                "Are you sure you want to exit?",
                lstYesNo
            )
            # Confirmation Conditional.
            if strConfirm in ['y', 'yes']:
                # Do they need to save?
                if blSaveStatus == False:
                    # We're not in sync, ask them to save first.
                    strSave = ValidateInput(
                        'Save now?',
                        lstYesNo
                    )
                    # Conditional for save.
                    if strSave in ['y', 'yes']:
                        # They want to save.
                        SaveFile('ToDo.txt', lstToDo)
                # Now exit!
                print('Exiting!')
                return
        else:
            print("I don't know how you got here.  This should be impossible."
                  "\nHuh..."
            )



def SaveFile(filename, table):
    ####################################################################
    # Desc:         Save the file
    # Parameters:
    #   filename    File to save
    #   table       List of Dictionaries to parse
    # Returns:      True
    ####################################################################
    # Open the file
    f = open(filename, 'w')
    # Loop through the list, write the data to the file.
    for row in table:
        f.write('{0}, {1}\n'.format(
            row['Action'],
            row['Priority'])
        )
    # Close the file.
    f.close()
    # Report to the user that the operation is complete.
    print('File Saved to "{0}"!'.format(filename))
    print()
    return True



def DisplayToDo(todo):
    ####################################################################
    # Desc:         Display the current ToDo list
    # Parameters:
    #   todo        The ToDo list
    # Returns:      Nothing
    ####################################################################

    # Nicely Formatted Header
    print()
    print('{:<79}'.format('ToDo List:'))
    print('{:-<79}'.format('-'))
    print('{0:<20}{1:<40}{2:<19}'.format('ID', 'Action', 'Priority'))

    # Loop over the ToDo list and print it.
    for index, row in enumerate(todo):
        # Check if the Action is too long.  If so, we'll truncate it.
        if len(row['Action']) > 39:
            # Slice the first 36 characters, add elipsis.
            strAction = row['Action'][:36] + '...'
        else:
            # It's short enough to use as-is.
            strAction = row['Action']
        # Print out the row
        print('{0:<20}{1:<40}{2:<19}'.format(
            index,
            strAction,
            row['Priority'])
        )
    print()
    return



def ValidateInput(question, answers):
    ####################################################################
    # Desc:         Validate user input
    # Parameters:
    #   question    String, the question we ask the user
    #   answers     List, valid answers, lowercase
    # Returns:      The user's input
    ####################################################################

    # Loop endlessly until we have a valid answer.
    while True:
        # Ask the question.
        strInput = input('{0} {1} '.format(question, str(answers)))
        # Is the answer legit?
        if strInput in answers:
            # We can use this, return it.
            return strInput
        else:
            # We can't use this, try again.
            print('"{0}" is not a valid answer.'.format(strInput))



# Run main function
if __name__ == '__main__':
    main()
