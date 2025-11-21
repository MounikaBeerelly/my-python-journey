#!python3

import os
os.system("cls")

def buildProfile(**kwargs) :
    profileData = {}
    profileData["FirstName"] = kwargs.get("FirstName", "Not Given")
    profileData["LastName"] = kwargs.get("LastName", "Not Given")    
    profileData["Age"] = kwargs.get("Age", "Not Given")
    profileData["Height"] = kwargs.get("Height", "Not Given")
    profileData["Place"] = kwargs.get("Place", "Not Given")
    profileData["Phone"] = kwargs.get("Phone", "Not Given")
    profileData["Email"] = kwargs.get("Email", "Not Given")
    
    print("\nThe registered profile of the end user is...", end="\n")
    for outKey, outValue in profileData.items() :
        print(f"{outKey} : {outValue}")
        
buildProfile(FirstName = "Smith", LastName = "Roy", Age = 31, Height = 135.23, Place = "Hyderabad", Phone = 2324327689, Email = "Smith@gmail.com")
buildProfile(FirstName = "John", LastName = "Doe", Age = 27, Height = 130.10, Email = "John@gmail.com")
buildProfile(FirstName = "Sachin", LastName = "Tendulkar", Age = 40, Height = 110.50, Place = "Hyderabad")

"""
Output:
------

The registered profile of the end user is...
FirstName : Smith
LastName : Roy
Age : 31
Height : 135.23
Place : Hyderabad
Phone : 2324327689
Email : Smith@gmail.com

The registered profile of the end user is...
FirstName : John
LastName : Doe
Age : 27
Height : 130.1
Place : Not Given
Phone : Not Given
Email : John@gmail.com

The registered profile of the end user is...
FirstName : Sachin
LastName : Tendulkar
Age : 40
Height : 110.5
Place : Hyderabad
Phone : Not Given
Email : Not Given

"""