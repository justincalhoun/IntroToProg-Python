#!/usr/bin/python3

########################################################################
#
# Name:     Justin Calhoun
# Course:   IT FDN 100 A Au 18
#           Foundations of Programming: Python
# Desc:     Assignment08 - Product Data with Classes
#
########################################################################

# Define Classes
class Product(object):
    """
    Class for instantiating a new Product Object
    """

    # --Constructor--
    def __init__(self, ID = '', Name = '', Price = '0.00'):
        """
        Initialize a new instance of the Product Class.

        :param ID: ID Number of this Product
        :param Name: Name of this Product
        :param Price: Price of this Product
        """
        # Attributes
        self.__ID = ID
        self.__Name = Name
        self.__Price = Price

    # --Properties--
    #ID
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, Value):
        self.__ID = Value

    #Name
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Value):
        self.__Name = Value

    #Price
    @property
    def Price(selfs):
        return self.__Price
    @Price.setter
    def Price(self, Value):
        self.__Price = '{0:.2f}'.format(float(Value))

    # --Methods--
    def ToString(self):
        """
        Returns the Product's properties in a single string.

        :return:
        """

        return '{0},{1},{2}'.format(self.__ID, self.__Name, self.__Price)

    def WriteToFile(self, FileObject):
        """
        Write the Product's properties to an open file.

        :param FileObject: An open file object to write to.
        :return:
        """

        FileObject.write(self.ToString() + '\n')

# --End of Class--

# Stand-Alone Functions
def ReadAllFileData(File, Message='Contents of File'):
    """
    Reads all data from an open file handler.

    :param File: An open File object
    :param Message: Friendly message to display to the user
    :return:
    """

    try:
        print(Message)
        File.seek(0)
        print(File.read())
    except Exception as e:
        print("Error: " + str(e))


# Main Function
def main():
    try:
        # Open the Products.txt file
        objFile = open('Products.txt', 'r+')
        # Display all the current data to the user
        ReadAllFileData(objFile, 'Here is the current data:')
        # Print the instructions
        print('Type in a Product Id, Name, and Price you want to add to '
              'the file')
        print('(Enter "Exit" to quit!)')
        # Start the user input loop
        while(True):
            # Get the new product data from the user
            strUserInput = input('Enter the Id, Name, and Price '\
                                 '(ex. 1,ProductA,9.99): ')
            # If they typed exit, break, otherwise add the new item
            if strUserInput.lower() == "exit": break
            else:
                # Split the string into it's component parts
                lstUserInput = strUserInput.split(',')
                # Create a new Product object
                NewProduct = Product(
                    lstUserInput[0],
                    lstUserInput[1],
                    lstUserInput[2])
                # Write the new product to the file
                NewProduct.WriteToFile(objFile)
        # Now that they've broken the loop, read back all the data again
        ReadAllFileData(objFile, 'Here is the saved data:')
    except FileNotFoundError as e:
        print('Error: ' + str(e) + '\nPlease check the file name')
    #except Exception as e:
    #    print('Error: ' + str(e))
    finally:
        # We're done, close the file
        if(objFile != None): objFile.close()



# Run main function
if __name__ == '__main__':
    main()
