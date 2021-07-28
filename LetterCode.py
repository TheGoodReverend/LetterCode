#! /user/bin/env python3
#Letter Code by KBowen

from LetterCodeLogic import LetterCodeLogic
#from filename       import  class




def getChoice():
    choice = -1
    #while (choice > 0 and choice <3)
    while (choice!=0):
        try:
            choice = int(input("Choice? (1=Encode, 2=Decode, 0=Quit): "))
            if (choice <0 or choice >2):
                print("Illegal input: 1, 2, or 0 please")
                choice = -1
            elif choice ==1: #encode
                msg = str(input("Plese enter the message you wish to encode: "))
                result = LetterCodeLogic.Encode(msg)
                print("Your encoded message is: \n " + result)
            elif choice ==2: #decode
                msg = str(input("Plese enter the message you wish to decode.\nPlease seperate by commas: "))
                result = LetterCodeLogic.Decode(msg)
                print("Your decoded message is: \n " + result)
            elif choice ==0:
                return choice
            else:
                print("You're traveling through another dimension --"
                      "a dimension not only of sight and sound but of mind."
                      "A journey into a wondrous land whose boundaries are that of imagination."
                      "That's a signpost up ahead: your next stop: the Twilight Zone!")
        except ValueError:
             print("Illegal input: 1, 2, or 0 please")



def main():
    print("Welcome to LetterCode program")
    print()
    getChoice()
    print("Thanks for using the program")

if __name__ == "__main__":
    main()
