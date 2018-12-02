#!/usr/bin/python3

########################################################################
#
# Name:     Justin Calhoun
# Course:   IT FDN 100 A Au 18
#           Foundations of Programming: Python
# Project:  Assignment09 - New Customer App
# Desc:     Classes for storing customer data
#
########################################################################

# Imports
import Persons

# Do not run this stand-alone:
if __name__ == '__main__':
    raise Exception("This file is not meant to be ran by itself.")

class Customer(Persons.Person):
    """
    Base Class for Customer Data
    """

    #--Constructor--
    def __init__(self, Phone = '', CC = ''):
        # Init from the parent class
        # This is required to get the UID working
        Persons.Person.__init__(self)
        #Attributes
        self.__Phone = Phone
        self.__CC = CC

    #--Properties--
    #Phone
    @property
    def Phone(self):
        return self.__Phone

    @Phone.setter
    def Phone(self, Value):
        self.__Phone = Value

    #CC
    @property
    def CC(self):
        return self.__CC

    @CC.setter
    def CC(self, Value):
        self.__CC = Value

    #--Methods--
    def ToString(self):
        """
        Explicitly returns field data

        :returns: String in the format of 'UID,LastName,FirstName,Phone,CC'
        """
        strReturn = '{0},{1},{2}'.format(
                super().ToString(),
                self.__Phone,
                self.__CC)
        return strReturn

#--End of Class--


class CustomerList(object):
    """
    Static Class for holding a list of Customer data
    """

    #--Constructor--
    def __init__(self, lstCustomers = []):
        self.__lstCustomers = lstCustomers

    #--Methods--
    def AddCustomer(self, Customer):
        """
        Adds a customer to the Customer List, if it's a valid object

        :param Customer: Customer object instance
        """
        if str(Customer.__class__) == "<class 'Customers.Customer'>":
            self.__lstCustomers.append(Customer)
        else:
            raise Exception('Only Customer objects can be added to this list.')

    def ToString(self):
        """
        Explicitly returns all customer data

        :returns: All data in csv format with heading
        """
        strData = 'UID,LastName,FirstName,Phone,CC\n'
        for item in self.__lstCustomers:
            strData += '{}\n'.format(item.ToString())
        return strData

    def BulkAdd(self, TextData):
        """
        Method for populating the list with data loaded from a file

        :param TextData: TextData Property of DataProcessor.File object
        """
        # Split the data into a list of entries
        lstData = TextData.strip().split('\n')

        # Turn it into customer objects in the list
        for row in lstData:
            # Skip the header row
            if row != 'UID,LastName,FirstName,Phone,CC':
                # Split the row into fields
                elements = row.split(',')
                # Build a temp instance of Customer and populate it with
                # the data
                tempCustomer = Customer()
                tempCustomer.UID = elements[0]
                tempCustomer.LastName = elements[1]
                tempCustomer.FirstName = elements[2]
                tempCustomer.Phone = elements[3]
                tempCustomer.CC = elements[4]
                # Add the object to the list
                self.AddCustomer(tempCustomer)

    def SyncLastUID(self):
        """
        Method for getting the UID ever used and continuing from there

        :returns: The highest UID stored in the customer list
        """
        # Get every UID and put them in a list
        lstUIDs = [int(x.UID) for x in self.__lstCustomers]
        # Set the Persons counter
        Persons.Person.SetUIDCounter(sorted(lstUIDs)[-1])

