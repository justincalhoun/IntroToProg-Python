#!/usr/bin/python3

########################################################################
#
# Name:     Justin Calhoun
# Course:   IT FDN 100 A Au 18
#           Foundations of Programming: Python
# Project:  Assignment09 - New Customer App
# Desc:     Main module for interactive use
#
########################################################################

# Imports here
import Customers, DataProcessor

# Main Function
def main():
    #--Setup--

    # Instantiate our data and customerlist objects
    myFile = DataProcessor.File()
    myCustomers = Customers.CustomerList()

    # Fill our list if the file isn't blank
    loadedData = myFile.GetData()
    if loadedData != '':
        # Load the data
        myCustomers.BulkAdd(loadedData)
        # Sync the UID to prevent ID Duplicates
        myCustomers.SyncLastUID()

    #--Interaction--
    # Introduction Text
    print('Welcome to the New Customer Application!\n'
          'You can use this to view and add new customers to a '
          '"customer db" object.\n')

    while True:
        # Begin the data entry loop
        print('Select an action:')
        strAction = input(' [A]dd a new customer (default)\n' \
                          ' [V]iew current data\n' \
                          ' e[X]it and save\n' \
                          'Selection? ')
        if strAction.lower() == 'x':
            print('Saving data to "SavedData.txt"...')
            # Add the current customer data to myFile
            myFile.TextData = myCustomers.ToString()
            # Save the data to disk
            myFile.SaveData()
            print('Saved!  Exiting...')
            break

        elif strAction.lower() in ['a', '']:
            print('Adding new customer!')
            # Get customer info from user
            strFirstName = input('First Name: ')
            strLastName = input('Last Name: ')
            strPhone = input('Phone Number: ')
            strCC = input('Credit Card Number: ')

            # Create a new customer object
            newCustomer = Customers.Customer()
            newCustomer.FirstName = strFirstName
            newCustomer.LastName = strLastName
            newCustomer.Phone = strPhone
            newCustomer.CC = strCC

            # Confirm the new record
            print('\nAbout to add the following customer:')
            print(newCustomer.ToString())
            strConfirmation = input('Is this all correct (y/n)? ')
            if strConfirmation.lower() == 'y':
                # Add the customer to myCustomers
                myCustomers.AddCustomer(newCustomer)
            else:
                print('Operation cancelled!')

        elif strAction.lower() == 'v':
            print('Current customers:')
            print(myCustomers.ToString())


# Run main function
if __name__ == '__main__':
    main()
