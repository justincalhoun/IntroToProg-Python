#!/usr/bin/python3

########################################################################
#
# Name:     Justin Calhoun
# Course:   IT FDN 100 A Au 18
#           Foundations of Programming: Python
# Project:  Assignment09 - New Customer App
# Desc:     Test Harness - Tests the classes to ensure they function
#
########################################################################

# Imports
import DataProcessor, Persons, Customers

# Main Function
def main():
    """
    Main Function
    """
    print('Welcome to the test harness for Assignment 09')

    while True:
        strOption = input('Which class do you want to test?\n' \
                          ' [1] ALL (default)\n' \
                          ' [2] DataProcessor: File Class\n' \
                          ' [3] Persons: Person Class\n' \
                          ' [4] Customers: Customer Class\n' \
                          ' [5] Customers: CustomerList Class\n' \
                          ' [x] Exit\n\n' \
                          'Selction: ')

        if strOption.lower() == 'x':
            # Exit the harness
            print('Nothing to do.')
            break
        elif strOption in ['1', '']:
            # Run all tests
            print('Running all tests!')
            TestDPFile()
            TestPerson()
            TestCustomer()
            TestCustomerList()
        elif strOption == '2':
            # Test DataProcessor::File
            TestDPFile()
        elif strOption =='3':
            TestPerson()
        elif strOption == '4':
            TestCustomer()
        elif strOption == '5':
            TestCustomerList()
        else:
            # No idea what they asked
            print('Sorry, not a valid option.  Please try again.\n')

    print('Exiting!')


def TestDPFile():
    """
    This tests the DataProcessor class and it's methods
    """

    print('\n### TEST: DataProcessor.py, File Class ###')

    print('Creating instance of File with default properties')
    TestFile = DataProcessor.File()

    print('Current FileName,TextData:\n  {}'.format(TestFile.ToString()))

    print('Setting Filename to "testfile.txt"...')
    TestFile.FileName = 'testfile.txt'

    print('Setting Value to "test data!"')
    TestFile.TextData = 'test data!'

    print('Current FileName,TextData:\n  {}'.format(TestFile.ToString()))

    print('Testing SaveData method...')
    TestFile.SaveData()

    print('Removing and re-instantiating...')
    TestFile = None
    TestFile = DataProcessor.File('testfile.txt', '')

    print('Testing GetData method...')
    TestFile.GetData()

    print('Current FileName,TextData:\n  {}'.format(TestFile.ToString()))

    print('### TEST COMPLETE ###\n')


def TestPerson():
    """
    This tests the Person Class
    """

    print('\n### TEST: Persons.py, Person Class ###')

    print('Creating a test individual...')
    testPerson = Persons.Person()
    testPerson.FirstName = 'Alpha'
    testPerson.LastName = 'Beta'

    print('Printing Individual...')
    print('  {}'.format(testPerson.ToString()))

    print('The Current UID is: {}'.format(Persons.Person.GetUIDCounter()))

    print('Setting the UID to 42...')
    Persons.Person.SetUIDCounter(42)

    print('Creating one more individual...')
    testPerson2 = Persons.Person()
    testPerson2.FirstName = 'Gamma'
    testPerson2.LastName = 'Delta'

    print('Printing Individual...')
    print('  {}'.format(testPerson2.ToString()))

    print('### TEST COMPLETE ###\n')


def TestCustomer():
    """
    This tests the Customer Class
    """

    print('\n### TEST: Customers.py, Customer Class ###')

    print('Creating a test individual...')
    testPerson = Customers.Customer()
    testPerson.FirstName = 'Alpha'
    testPerson.LastName = 'Beta'
    testPerson.Phone = '555-555-5555'
    testPerson.CC = '4111-1111-1111-1111'

    print('Printing Individual...')
    print('  {}'.format(testPerson.ToString()))

    print('The Current UID is: {}'.format(Persons.Person.GetUIDCounter()))

    print('Setting the UID to 142...')
    Persons.Person.SetUIDCounter(142)

    print('Creating one more individual...')
    testPerson2 = Customers.Customer()
    testPerson2.FirstName = 'Gamma'
    testPerson2.LastName = 'Delta'
    testPerson2.Phone = '555-555-5556'
    testPerson2.CC = '5111-1111-1111-1111'

    print('Printing Individual...')
    print('  {}'.format(testPerson2.ToString()))

    print('### TEST COMPLETE ###\n')


def TestCustomerList():
    """
    This tests the Customer List
    """

    print('\n### TEST: Customers.py, CustomerList Class ###')

    print('Creating a list...')
    myCustomers = Customers.CustomerList()

    print('Bulk Adding data from "testdata.txt"...')
    myFile = DataProcessor.File('testdata.txt')
    myCustomers.BulkAdd(myFile.GetData())

    print('Printing added data:')
    print(myCustomers.ToString())

    print('Syncing UID...')
    myCustomers.SyncLastUID()

    print('Current UID is now: {}'.format(Persons.Person.GetUIDCounter()))

    print('Adding single customer...')
    testPerson = Customers.Customer()
    testPerson.FirstName = 'Eta'
    testPerson.LastName = 'Theta'
    testPerson.Phone = '555-555-8888'
    testPerson.CC = '5111-1111-1111-1112'
    myCustomers.AddCustomer(testPerson)

    print('Printing all data:')
    print(myCustomers.ToString())

    print('### TEST COMPLETE ###\n')


# Run main function
if __name__ == '__main__':
    main()
