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
    # Set operation to True
    operation = True

    # Attempt to open the file
    # lstToDo is whatever data we could read.
    # blSaveStatus is True if the file loaded, or False if it could not
    # be found.
    lstToDo,blSaveStatus = ToDo.OpenFile('ToDo.txt')

    ### Presentation ###
    # Display whatever data we've loaded, if there is anything.
    if blSaveStatus:
        ToDo.Display(lstToDo)
    else:
        print('Could not open ToDo.txt.')

    # Begin the main user loop.
    while operation:
        # Display the menu and do as the user asked.
        # Return the operation flag and save status flag
        operation, blSaveStatus = ToDo.Menu(lstToDo, blSaveStatus)

    # Operation has concluded, exit!
    print('Exiting!')
    return

class ToDo(object):

    @staticmethod
    def OpenFile(filename):
        ################################################################
        # Desc:         Open the file
        # Parameters:
        #   filename    File to save
        # Returns:      List, potentially of Dictionaries
        ################################################################

        # Create an empty List
        lstToDo = []
        # Attempt to open the file
        try:
            # Open the file.
            f = open(filename, 'r')
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
            # Return the list and True flag
            return lstToDo, True
        except FileNotFoundError:
            # The file wasn't there, return the list and False flag
            return lstToDo, False

    @staticmethod
    def SaveFile(filename, table, savestatus):
        ####################################################################
        # Desc:         Save the file
        # Parameters:
        #   filename    File to save
        #   table       List of Dictionaries to parse
        #   savestatus  The blSaveStatus flag
        # Returns:      True
        ####################################################################

        # Confirm the action.
        strConfirm = ToDo.ValidateInput(
            "Save now?",
            ['y','yes','n','no']
        )
        # Confirmation Conditional.
        if strConfirm in ['y', 'yes']:
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
        else:
            # They changed their mind.
            print('Save Canceled.')
            print()
            return savestatus


    @staticmethod
    def Display(todo):
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

    @staticmethod
    def Menu(todo, savestatus):
        ####################################################################
        # Desc:         Display the Menu and perform functions
        # Parameters:
        #   todo        The ToDo list
        #   savestatus  The blSaveStatus
        # Returns:      True or False, savestatus
        ####################################################################

        # Define the menu
        lstMenu = [
            {'ID' : 1, 'Option' : 'Show current data.'},
            {'ID' : 2, 'Option' : 'Add a new item.'},
            {'ID' : 3, 'Option' : 'Remove an existing item.'},
            {'ID' : 4, 'Option' : 'Save Data to File.'},
            {'ID' : 5, 'Option' : 'Exit Program.'}
        ]

        # Display the menu.
        print('Menu of Options')
        for row in lstMenu:
            print('{0}) {1}'.format(row['ID'], row['Option']))
        print()
        # Ask the user to select an item.
        strChoice = ToDo.ValidateInput(
            "What would you like to do?",
            [str(dct['ID']) for dct in lstMenu]
        )

        # Conditional Block to do as the user asked.
        if strChoice == '1':
            # Display the current data
            ToDo.Display(todo)
        elif strChoice == '2':
            # Add an item to the list
            # Save the new list and update the save status
            todo, savestatus = ToDo.AddDel(todo, savestatus, 'add')
        elif strChoice == '3':
            # Del an item to the list
            # Save the new list and update the save status
            todo, savestatus = ToDo.AddDel(todo, savestatus, 'del')
        elif strChoice == '4':
            # Save Data to the file.
            savestatus = ToDo.SaveFile('ToDo.txt', todo, savestatus)
        elif strChoice == '5':
            # Exit the program.
            # Confirm the action.
            strConfirm = ToDo.ValidateInput(
                "Are you sure you want to exit?",
                ['y','yes','n','no']
            )
            # Confirmation Conditional.
            if strConfirm in ['y', 'yes']:
                # Do they need to save?
                if savestatus == False:
                    # We're not in sync, attempt to save first.
                    ToDo.SaveFile('ToDo.txt', todo, savestatus)
                # Return the exit flag
                return False, savestatus
        # We're not exiting, return the continue flag and save status
        return True, savestatus

    @staticmethod
    def AddDel(todo, savestatus, op):
        ####################################################################
        # Desc:         Add or Remove items from the ToDo list
        # Parameters:
        #   todo        The ToDo list
        #   savestatus  blSaveStatus flag
        #   op          Operaion: 'add' or 'del'
        # Returns:      Nothing
        ####################################################################

        # Adding an item
        if op == 'add':
            # Add a new item
            print()
            print('Adding a new item!')
            # Ask the user for the new action item.  No validation,
            # any string is acceptable.
            strAction = input("What's the new action item? ")
            # Ask the user for the priority.
            strPriority = ToDo.ValidateInput(
                "What's the Priority?",
                ['low', 'med', 'high']
            )
            # Create a dictionary of the user's input
            dctRow = {
                'Action' : strAction.capitalize(),
                'Priority' : strPriority.lower()
            }
            # Append the item to the ToDo list.
            todo.append(dctRow)
            print('{0}, {1} Added!'.format(strAction, strPriority))
            print()
            # Return the list and the new blSaveStatus
            return todo, False

        # Deleting an item
        elif op == 'del':
            # Remove an item.
            # Build a list of valid answers.
            lstIndexes = [str(index) for index,row in enumerate(todo)]
            # Add options to back out.
            lstIndexes += ['c', 'cancel']
            # Ask the question.
            strRemove = ToDo.ValidateInput(
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
                    todo[int(strRemove)]['Action'],
                    todo[int(strRemove)]['Priority'])
                )
                # Ask them to confirm the deletion.
                strConfirm = ToDo.ValidateInput(
                    "Are you sure?",
                    ['y','yes','n','no']
                )
                # Confirmation Conditional.
                if strConfirm in ['y', 'yes']:
                    del todo[int(strRemove)]
                    print('Action removed!')
                    print()
                    # Return the list and the new blSaveStatus
                    return todo, False
                else:
                    print('Cancelled!  No items removed.')
                    print()

        # If we fell through the conditional, nothing changed.
        # Return the unaltered list and save status
        return todo, savestatus

    @staticmethod
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
