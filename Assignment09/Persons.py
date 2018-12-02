#!/usr/bin/python3

########################################################################
#
# Name:     Justin Calhoun
# Course:   IT FDN 100 A Au 18
#           Foundations of Programming: Python
# Project:  Assignment09 - New Customer App
# Desc:     Classes for storing individual person data
#
########################################################################

# Do not run this stand-alone:
if __name__ == '__main__':
    raise Exception("This file is not meant to be ran by itself.")

class Person(object):
    """
    Base Class for Personal Data
    """

    #--Fields--
    # This will be used to create automatic unique user id numbers
    __UIDCounter = 0

    #--Constructor--
    def __init__(self, FirstName = '', LastName = ''):
        # Increment the UID Counter on each construction
        Person.__IncrementCounter()

        #Attributes
        self.__UID = Person.__UIDCounter
        self.__FirstName = FirstName
        self.__LastName = LastName

    #--Properties--
    #UID
    @property
    def UID(self):
        return self.__UID

    @UID.setter
    def UID(self, Value):
        self.__UID = Value

    #FirstName
    @property
    def FirstName(self):
        return self.__FirstName

    @FirstName.setter
    def FirstName(self, Value):
        self.__FirstName = Value

    #LastName
    @property
    def LastName(self):
        return self.__LastName

    @LastName.setter
    def LastName(self, Value):
        self.__LastName = Value

    #--Methods--
    def ToString(self):
        """
        Explicitly returns field data

        :returns: String in the format of 'UID,LastName,FirstName'
        """
        strReturn = '{0},{1},{2}'.format(
                str(self.__UID),
                self.__LastName,
                self.__FirstName)
        return strReturn

    @staticmethod
    def GetUIDCounter():
        """
        Return the current Person Class UID

        :returns: The UID as an integer
        """
        return Person.__UIDCounter

    @staticmethod
    def SetUIDCounter(Value):
        """
        Set the current value of the UID Counter

        This is to ensure that we don't use the same UID twice on
        subsequent runs of the application.
        """
        Person.__UIDCounter = Value

    @staticmethod
    def __IncrementCounter():
        """
        Increase the internal counter by 1
        """
        Person.__UIDCounter += 1

#--End of Class--
