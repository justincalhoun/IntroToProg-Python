#!/usr/bin/python3

########################################################################
#
# Name:     Justin Calhoun
# Course:   IT FDN 100 A Au 18
#           Foundations of Programming: Python
# Project:  Assignment09 - New Customer App
# Desc:     Classes for reading and writing data
#
########################################################################

# Do not run this stand-alone
if __name__ == '__main__':
    raise Exception("This file is not meant to be ran by itself.")

class File(object):
    """
    Class for processing data using files
    """

    #--Constructor--
    def __init__(self, FileName = "SavedData.txt", TextData = ""):
        """
        Initialize a new instance of the File class.

        :param FileName: Name of the file
        :param TextData: Data read from or written to the file
        """
        #Attributes
        self.__FileName = FileName
        self.__TextData = TextData

    #--Properties--

    #FileName
    @property
    def FileName(self):
        return self.__FileName

    @FileName.setter
    def FileName(self, Value):
        self.__FileName = Value

    #TextData
    @property
    def TextData(self):
        return self.__TextData

    @TextData.setter
    def TextData(self, Value):
        self.__TextData = Value

    #--Methods--
    def SaveData(self):
        """
        Writes data to the file

        :returns: The string 'Data Saved'
        """
        try:
            objFile = open(self.__FileName, "w")
            objFile.write(self.__TextData)
            objFile.close()
        except Exception as e:
            print("Python reported the following error: " + str(e))
        return "Data Saved"

    def GetData(self):
        """
        Reads data from the file

        :returns: The data from the file.
        """
        try:
            objFile = open(self.__FileName, "r")
            self.__TextData = objFile.read()
            objFile.close()
        except FileNotFoundError:
            self.__TextData = ''
        except Exception as e:
            print("Python reported the following error: " + str(e))
        return self.__TextData

    def ToString(self):
        """
        Explictly returns field data

        :returns: The name of the file and the data within as a string.
        """
        return self.__FileName + "," + self.__TextData

#--End of class--
