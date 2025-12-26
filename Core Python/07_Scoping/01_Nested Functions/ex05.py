#!python3

import os
os.system("cls")

def downCounter(inStartValue) :
    print(f"\nInitiating the count down process beginning from : {inStartValue}", end="\n")
    
    def executeCounter() :
        for countDownIndex in range(inStartValue, 0, -1) :
            print(f"{countDownIndex}, ", end="")
        print(f"Hey! You reached the ground floor...", end="\n")
        return
    executeCounter()
    return
    
def main() :
    print("\nImplementing the count down process..", end="\n")
    activeFloor = int(input("\nPlease enter the floor number you are in: "))
    downCounter(activeFloor)
    return

if __name__ == "__main__" :
    main()
    

"""
Output:
-------
Implementing the count down process..

Please enter the floor number you are in: 5

Initiating the count down process beginning from : 5
5, 4, 3, 2, 1, Hey! You reached the ground floor...
"""  