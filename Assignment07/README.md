# Assignment 07 - Exception Handling and Pickling
For this assignment, we were tasked with providing examples of how one might use Exception Handling and Pickling.  To do this, I created a small “dummy” program that lets a user experiment with the outcomes of these techniques.
## Error Handling
During normal execution, when the Python interpreter runs into some kind of error, it will raise an “exception” and stop processing the script any further.  “Exception handling” is the concept of planning for these exceptions and writing your application to behave in a different way when they occur.  This is accomplished by placing the block of code you believe may encounter an exception into a `try` statement, and then using an `except` to tell the script how to behave when an exception occurs.

In my example, I chose to focus on opening a file, and wrote the following function:
```python
def CharacterCounter(filename):
    # This is a simple function for demonstrating Error Handling.
    # When called it tries to open the file name provided and read data             
    # from it, and in the event there is no file, instead of erroring
    # out, we'll handle it and inform the user.                                                      try:
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
```
This function, `CharacterCount()`, takes a single string as a parameter: a file name.  It then “tries” to open the file, and if successful, it will read the contents of the file into a string, and then check the length of that string, or count how many characters are in the file.  It returns two items: if successful, the first thing returned is the length as an integer, and the second is the special type `None`.  

However, if it is unsuccessful, it will behave differently.  The first `except` block will execute if there is a `FileNotFoundError`.  This occurs any time the user provides a file name/path that does not exist.  Instead of the script ending with the error, though, we “catch” it, and return `None` for the length, and a custom error string to report back to the user.

The second block checks for a `UnicodeDecodeError`.  This exception is raised when the file isn’t a text file, or if it is a text file, but is not encoded in utf-8.  I’m cheating a bit here, because while it’s not exactly correct, my error string asks the user if they’re sure that the file is a text file, implying it’s binary.  This is the most likely case for most users that may run this example.

The last `except` block is a catch-all.  It catches any other exception, stores it in the variable `e`, and then reports it back to the user.

In the `main()` function, if the user chooses to engage with this example, it will be called as such:
```python
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
```
The script asks the user for a file name.  I call the `CharacterCount()` function with their input string as the argument.  If the second variable, `err`, is returned with anything in it (not `None`), then I print my custom error and the loop continues.  If `err` was `None`, we assume that an integer came back, and report the number of characters in the file.

Here are some of the various responses this function can return, as I test it with a text file, a gzipped tar file, and a file that doesn’t exist:
```
Which example would you like to try?                                               
1 - Error Handling
2 - Pickling
x - Exit
Please select one:  ['1', '2', 'x'] 1                                              

Welcome to the Error Handling Example!
In this example, you may enter any file name, and if it both exists and is a text file, the script will count the number of characters in the file.

Try the provided "example.txt" file to see how it works normally, then try it again with a file that doesn't exist to see how that error is handled, as well as with a binary file like the included "example.tgz".

When you're done, type "x" to exit this example.

What file would you like counted? example.txt                                      
That file contains 1509 characters!                                                

What file would you like counted? example.tgz                                      
An error attempting to read the file "example.tgz"; are you sure this is a text file?

What file would you like counted? sandwich                                         
Could not find the file "sandwich", please check the file name and try again.      

What file would you like counted? 
```
## Pickling
Serialization, or “Pickling”, is the process of taking objects in memory and converting them into a “flattened” binary stream, so they can be stored and retrieved later.  This can be handy in some situations.  You can pickle objects to prepare them for transmission over a network, or to pass them between running processes in a multi-threaded application.  Many highly-interactive applications, like games, use pickling (or similar techniques) to store the entire game state to be later picked up where the user left off.  It can also provide very basic obfuscation: instead of storing objects in a human-readable format, if you don’t want your users poking at your stored data in plain text, pickling can “hide” what’s in the file from anyone who might open it and not recognize what it is.  It won’t stop a dedicated programmer (or even power user), as they can just unpickle it, but in many cases it may be enough to stop an average user from manually editing application data that might break your program on next load.

The main benefit of pickling, however, is also it’s main drawback.  With Python’s pickling, you can store almost any object by serializing it.  Importantly, you can pickle functions, classes, or instances of classes.  You can also store self-referential objects, such as a list that contains itself as an element.  While this is powerful, it’s also quite dangerous: loading pickled objects into memory from a source you do not control or trust (in the IT security sense) can lead to loading and executing malicious code.

The Python documentation calls this out at the top of the page describing the pickle module: 
> Warning: The pickle module is not secure against erroneous or maliciously constructed data. Never unpickle data received from an untrusted or unauthenticated source.” 
> (https://docs.python.org/3.6/library/pickle.html)

Use pickling with caution, and never unpickle anything that you did not pickle yourself, and thus fully trust the contents.

For my example, I wrote a small function that appends elements to a list.  It takes an integer as an argument, and then uses a for loop to append that many items onto a list, which it returns:
```python
def Grower(count):
    # This function just adds a bunch of 'a' characters to a list.
    lstA = []
    for i in range(count):
        lstA.append('a')
    return lstA
```
In the `main()` function, if the user chooses to interact with the pickling example, I first check to see if I have a pickled file present or not.  If so, we unpickle it and load it into memory.  If not, we just create a blank list to start growing.  Either way, the variable longlist is created:
```python
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
```
From here, we start a loop.  We ask the user how many elements to add to the list.  `Grower()` is called, and the returned list is added to longlist.  When the user tires of adding elements, they can choose to exit.  Upon exiting the loop, longlist is pickled and saved to the file longlist.pkl.  If they come back later, the pickled list will be opened and loaded back into memory, right where they left off:
```python
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
```
Here's an example of the first time a user runs the pickling example:
```
Welcome to the Pickling Example!
In this example, you can keep adding elements to a list for as long as you like.  When you are done, the list will be pickled and dumped to a file, so that when you come back to this example, you can continue to add to the length of the list.

Enter a number to grow the list by that many elements.
Enter "x" to exit this example, but be sure to come back later when you want to add more!

No list in progress, starting a fresh one.

The list is currently 0 elements long.
How many elements would you like to add to the list? 10000                         
Added 10000 new elements!                                                          

The list is currently 10000 elements long.
How many elements would you like to add to the list? 42                            
Added 42 new elements!                                                             

The list is currently 10042 elements long.
How many elements would you like to add to the list? 
```
Then, when they come back to it later, it picks up where they left off:
```
Welcome to the Pickling Example!
In this example, you can keep adding elements to a list for as long as you like.  When you are done, the list will be pickled and dumped to a file, so that when you come back to this example, you can continue to add to the length of the list.

Enter a number to grow the list by that many elements.
Enter "x" to exit this example, but be sure to come back later when you want to add more!

Found and loaded a list in progress!

The list is currently 10042 elements long.
How many elements would you like to add to the list? 
```
While this isn’t a particularly practical example, hopefully it helps demonstrate the power of directly storing and loading objects.  Just to see, I timed adding 100,000,000 elements to the list, and it took roughly 16 seconds to create and save the file.  I then re-tested, and to load that list from the pickle and re-save it took closer to 6 seconds.  While not a very scientific test, there is value to be had in pickling large objects that require heavy computation to create, so that your application can work with that data set immediately upon next execution, instead of having to re-process your source data every time.