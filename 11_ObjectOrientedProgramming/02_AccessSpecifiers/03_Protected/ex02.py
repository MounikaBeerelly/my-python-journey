#!python3

import os
os.system("cls")

class Person :
    __firstName = None
    __middleName = None
    __lastName = None
    __houseNumber = None
    __streetName = None
    __cityName = None
    __stateName = None
    __countryName = None
    __pinCode = None
    __personType = None
    __personGender = None
    __birthDate = None
    __birthMonth = None
    __birthYear = None
    
    def getFullName(self) :
        fullName = self.__firstName + " " + self.__middleName + " " + self.__lastName
        return fullName
    
    def getPersonAddress(self) :
        print("\nThe person\'s address is..", end = "\n")
        print("\n\t%s, %s" %(self.__houseNumber, self.__streetName), end="\n")
        print("\t%s, %s" %(self.__cityName, self.__stateName), end="\n")
        print("\t%s, %s" %(self.__countryName, self.__pinCode), end="\n")
        
    def getFirstName(self) :
        self.__firstName = input()
        
    def getMiddleName(self) :
        self.__middleName = input()
        
    def getLastName(self) :
        self.__lastName = input()
        
    def getHouseNumber(self) :
        self.__houseNumber = input()
        
    def getStreetName(self) :
        self.__streetName = input()
        
    def getCityName(self) :
        self.__cityName = input()
        
    def getStateName(self) :
        self.__stateName = input()
        
    def getCountryName(self) :
        self.__countryName = input()
        
    def getPinCode(self) :
        self.__pinCode = int(input())
        
    def getPersonType(self) :
        self.__personType = input()
        
    def getPersonGender(self) :
        self.__personGender = input()
        
    def getBirthDate(self) :
        self.__birthDate = int(input())
        
    def getBirthMonth(self) :
        self.__birthMonth = int(input())
    
    def getBirthYear(self) :
        self.__birthYear = int(input())
     
    def getPersonData(self) :
        print("\nPlease enter the First Name : ", end="")
        self.getFirstName()
        
        print("\nPlease enter the Middle Name : ", end="")
        self.getMiddleName()

        print("\nPlease enter the Last Name : ", end="")
        self.getLastName()
        
        print("\nCollecting the Address details...")
        print("\n-------------oOo-----------------", end="\n")
        
        print("\nPlease enter the House Number : ", end="")
        self.getHouseNumber()

        print("\nPlease enter the Street Name : ", end="")
        self.getStreetName()

        print("\nPlease enter the City Name : ", end="")
        self.getCityName()

        print("\nPlease enter the State Name : ", end="")
        self.getStateName()

        print("\nPlease enter the Country Name : ", end="")
        self.getCountryName()

        print("\nPlease enter the Pincode : ", end="")
        self.getPinCode()
        
        print("\nPlease enter the Person Type : ", end="")
        self.getPersonType()

        print("\nPlease enter the Person Gender : ", end="")
        self.getPersonGender()

        print("\nPlease enter the Birth Date : ", end="")
        self.getBirthDate()

        print("\nPlease enter the Birth month (MM) : ", end="")
        self.getBirthMonth()

        print("\nPlease enter the Birth Yesr (YYYY) : ", end="")
        self.getBirthYear()
        
    def putPersonData(self) :
        print("\nThe first name is : %s" %self.__firstName, end = "\n")
        print("\nThe middle name is : %s" %self.__middleName, end = "\n")
        print("\nThe last name is : %s" %self.__lastName, end = "\n")
        fullName = self.getFullName()
        
        print("\nThe Full Name of the PErson is : %s" %(fullName), end="\n")
        if(self.__personGender == 'm' or self.__personGender == 'M') :
            print("\nThe Gender of the person is : %c, (Male)" %self.__personGender, end="\n")
        elif(self.__personGender == 'f' or self.__personGender == 'F') :
            print("\nThe Gender of the person is : %c, (Female)" %self.__personGender, end="\n")
        elif(self.__personGender == 't' or self.__personGender == 'T') :
            print("\nThe Gender of the person is : %c, (Trans Gender)" %self.__personGender, end="\n")
        else :    
            print("\nThe Gender of the person is : %c, (Un-Recognized)" %self.__personGender, end="\n")
            
        self.getPersonAddress()
        
        if(self.__personType == 't' or self.__personType == 'T') :
            print("\nPerson Type is : %c, (Technical Professional)" %self.__personType, end="\n")
        elif(self.__personType == 'n' or self.__personType == 'N') :
            print("\nPerson Type is : %c, (Technical Professional)" %self.__personType, end="\n")
        else :
            print("\nThe Person type is : : Un-Recognized")
            
        print("\nThe Person Date of Birth is : %02d-%02d-%4d" %(self.__birthDate, self.__birthMonth, self.__birthYear), end="\n")
        
        
print("\nCreating the object instance of the Person class", end="\n")

personObject = Person()

print("\nInitializing the object \"personObject\" instance with the end users values")

personObject.getPersonData()

print("\nPrinting the values from the Person object instance..", end="\n")
print("----------------------------oOo-----------------------", end="\n")

print("\nPlease press the Enter key to display the data..")
personObject.putPersonData()


"""
Output:
-------

Creating the object instance of the Person class

Initializing the object "personObject" instance with the end users values

Please enter the First Name : John

Please enter the Middle Name : Williams

Please enter the Last Name : Berkely

Collecting the Address details...

-------------oOo-----------------

Please enter the House Number : 1-23/A

Please enter the Street Name : Ravuri Colony

Please enter the City Name : Hyderabad

Please enter the State Name : Telangana

Please enter the Country Name : India

Please enter the Pincode : 500200

Please enter the Person Type : t

Please enter the Person Gender : m

Please enter the Birth Date : 18

Please enter the Birth month (MM) : 12

Please enter the Birth Yesr (YYYY) : 1988

Printing the values from the Person object instance..
----------------------------oOo-----------------------

Please press the Enter key to display the data..

The first name is : John

The middle name is : Williams

The last name is : Berkely

The Full Name of the PErson is : John Williams Berkely

The Gender of the person is : m, (Male)

The person's address is..

        1-23/A, Ravuri Colony
        Hyderabad, Telangana
        India, 500200

Person Type is : t, (Technical Professional)

The Person Date of Birth is : 18-12-1988
"""