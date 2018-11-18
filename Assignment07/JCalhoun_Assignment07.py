#!/usr/bin/python3

########################################################################
#
# Name:     Justin Calhoun
# Course:   IT FDN 100 A Au 18
#           Foundations of Programming: Python
# Desc:     Assignment07 - Simple Examples, Error Handling and Pickling
#
########################################################################

# Imports here
import pickle

# Main Function
def main():
    # Infinite Loop
    while True:
        # Ask the user which example they want to play with
        inFunction = ValidateInput(
            'Which example would you like to try? \n'
            '1 - Error Handling\n'
            '2 - Pickling\n'
            'x - Exit\n'
            'Please select one: ',
            ['1','2','x'])

        if inFunction == '1':
            # Explain to the user the purpose of this exercise
            print('\n'
                  'Welcome to the Error Handling Example!\n'
                  'In this example, you may enter any file name, and if it '
                  'both exists and is a text file, the script will count the '
                  'number of characters in the file.\n\n'
                  'Try the provided "example.txt" file to see how it works '
                  'normally, then try it again with a file that doesn\'t '
                  'exist to see how that error is handled, as well as with '
                  'a binary file like the included "example.tgz".\n\n'
                  'When you\'re done, type "x" to exit this example.\n')

            # Start another loop
            testingloop = True
            while testingloop:
                # Ask them for a file name
                inFilename = input('What file would you like counted? ')
                # Did they ask to stop?
                if inFilename == 'x':
                    # Set the flag to false, and this loop will end.
                    print('OK, leaving this exercise.\n')
                    testingloop = False
                else:
                    # They did not, so let's try it
                    count, err = CharacterCounter(inFilename)
                    # Was an error returned?
                    if err:
                        # Print the error information
                        print('{}\n'.format(err))
                    else:
                        # No error, return the character count
                        print('That file contains {} characters!\n'.format(
                                str(count)))

        elif inFunction == '2':
            # Explain to the user the purpose of this exercise
            print('\n'
                  'Welcome to the Pickling Example!\n'
                  'In this example, you can keep adding elements to a list '
                  'for as long as you like.  When you are done, the list '
                  'will be pickled and dumped to a file, so that when you '
                  'come back to this example, you can continue to add to '
                  'the length of the list.\n\n'
                  'Enter a number to grow the list by that many elements.\n'
                  'Enter "x" to exit this example, but be sure to come '
                  'back later when you want to add more!\n')

            # See if the pickle file is there
            try:
                # Open the file in Binary mode
                f = open('longlist.pkl', 'rb')
                # Retrieve the stored list variable
                longlist = pickle.load(f)
                # Close the file
                f.close()
                print('Found and loaded a list in progress!\n')
            except FileNotFoundError:
                # The file didn't exist, start with an empty list
                print('No list in progress, starting a fresh one.\n')
                longlist = []

            # Start up a loop
            testingloop = True
            while testingloop:
                # Report how big the list is
                print('The list is currently {} elements long.'.format(
                    len(longlist)))
                # Ask for input
                inAction = input('How many elements would you like to add '
                                 'to the list? ')
                # Find out what they entered
                if inAction == 'x':
                    # They are done for now, end the loop.
                    print('Ok, leaving this exercise.\n')
                    testingloop = False
                    # Pickle and save
                    f = open('longlist.pkl', 'wb')
                    pickle.dump(longlist, f)
                    f.close()
                else:
                    # Let's see if it was an integer and grow the list
                    try:
                        # Run the Grower function and add the new
                        # elements to the longlist
                        longlist += Grower(int(inAction))
                        print('Added {} new elements!\n'.format(inAction))
                    except ValueError:
                        # Must not be an integer
                        print('Invalid input, please enter an integer or '
                              '"x" to exit for now.\n')

        elif inFunction == 'x':
            # They have chosen to exit the program.
            print('Ok, exiting!')
            return



# Error Handling Example Function
def CharacterCounter(filename):
    # This is a simple function for demonstrating Error Handling.
    # When called it tries to open the file name provided and read data
    # from it, and in the event there is no file, instead of erroring
    # out, we'll handle it and inform the user.

    try:
        # Attempt to open the given file name.
        f = open(filename, 'r')
        # Read the entire file into a string.
        contents = f.read()
        # Store the length of the string.
        length = len(contents)
        # Return the length and a None
        return length, None

    except FileNotFoundError:
        # This exception means we wouldn't find the file specified.
        # Here's our sanatized error message to display
        errorstring = 'Could not find the file "{}", please check the '\
                      'file name and try again.'.format(filename)
        # Return None for the length, and the Error
        return None, errorstring

    except UnicodeDecodeError:
        # This exception means we couldn't read the file: it contains
        # non-unicode characters.  Most likely, it's a binary file.
        errorstring = 'An error attempting to read the file "{}"; are '\
                      'you sure this is a text file?'.format(filename)
        # Return None for the length, and the Error
        return None, errorstring

    except Exception as e:
        # Here's where we catch whatever else might come up that we
        # haven't specifically accounted for.
        errorstring = 'Huh, you\'ve found a strange error: {}'.format(e)
        # Return None for the length, and the Error
        return None, errorstring



# Pickling Example Helper Function
def Grower(count):
    # This function just adds a bunch of 'a' characters to a list.
    lstA = []
    for i in range(count):
        lstA.append('a')
    return lstA



# Supporting functions
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


if __name__ == '__main__':
    main()
