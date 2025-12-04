#!python3

import os
os.system("cls")

def removeDuplicates(inList):
    uniqueList = []
    for listElement in inList :
        if listElement not in uniqueList :
            uniqueList.append(listElement)
    return uniqueList
    
def main() :
    os.system("cls")
    
    sportsList = ["Chess", "FootBall", "Shuttle", "Cricket", "FootBall", "Carroms", "Tennis", "FootBall", "Shuttle", "Swimmming", "Volley Ball", "Badminton", "Chess"]
    
    print("\nThe original list is: ", list(sportsList), end="\n")
    
    uniqueData = removeDuplicates(sportsList)
    
    print("\nThe final list with unique elements are...", end="\n\n")
    
    for listElement in uniqueData :
        print(listElement)
        
if __name__ == "__main__" :
    main()
    
"""
Output:
-------

The original list is:  ['Chess', 'FootBall', 'Shuttle', 'Cricket', 'FootBall', 'Carroms', 'Tennis', 'FootBall', 'Shuttle', 'Swimmming', 'Volley Ball', 'Badminton', 'Chess']

The final list with unique elements are...

Chess
FootBall
Shuttle
Cricket
Carroms
Tennis
Swimmming
Volley Ball
Badminton
"""