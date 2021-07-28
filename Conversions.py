#! /user/bin/env python3
#Conversions by KBowen

from Converter import Conversions
#from filename       import  class

#globes
validator = -1

def kCon():
    print()
    global validator
    while(validator < 0):
        try:
            kCon = input("On Temp conversions, would you also like to see degrees Kelvin (K) in the results? (Y/N): ")
            if(kCon=="N" or kCon=="n"):
                print("Kelvin is disabled")
                validator = 0
            elif(kCon=="y" or kCon=="Y"):
                print("Kelvin is enabled")
                validator = 1
            else:
                print("Illegal input: Y or N only please.")
        except ValueError:
            print("Illegal input: Y or N only please.")
    
def getChoice():
    global validator
    choice = -1
    while(choice!=0):
        try:
            choice = int(input("Conversion? (1=Mi-to-Km, 2=Oz-to-Gr, 3=F-to-C, 4=C-to-F, 5=M-to-Ft, 6=Li-to-Gal, 0=end): "))
            if(choice <0 or choice > 6):
                print("Illegal input: 0-6 only please.")
                choice = -1
            elif choice==0: #kill instance
                return choice
            elif choice==1: #miles to kilometers
                mi = input("Please input miles: ")
                km = Conversions.MitoKm(mi)
                print(mi + " miles = " + str(km) + " kilmoters.")
            elif choice==2: #ounces to grams
                oz = input("Please input ounces: ")
                gr = Conversions.OztoGr(oz)
                print(oz + " ounces = " + str(gr) + " grames.")
            elif choice==3:#F to C
                fa = input("Please input Fahrenheit Temp: ")
                ce = Conversions.FatoCe(fa)
                print(fa + " degrees F = " + str(ce) + " degrees C.")
                if(validator==1): #K option
                    K = Conversions.getK(ce)
                    print(" And: " + str(K) + " Kelvin")
            elif choice==4: #C to F
                ce = input("Please input Celsius: ")
                fa = Conversions.CetoFa(ce)
                print(ce + " degrees C = " + str(fa) + " degrees F.")
                if(validator==1): #K option
                    K = Conversions.getK(ce)
                    print(" And: " + str(K) + " Kelvin")
            elif choice==5: #meters to feet
                me = input("Please input meters: ")
                ft = Conversions.MetoFt(me)
                print(me + " meters = " + str(ft) + " feet.")
            elif choice==6: #liters to gallons
                li = input("Please input miles: ")
                ga = Conversions.LitoGa(li)
                print(li + " liters = " + str(ga) + " gallons.")
            else:
                print("Unknown choice.  How did we get here?")
                choice = -1
        except ValueError as e:
            print("Data Error: " + str(e))
            print()
        except Exception as ex:
            print("General Error: " + str(ex))
            print()
        
def main():
    print("Welcome to the English-Metric Converter!")
    kCon()
    print()
    getChoice()
    print("Thanks for using the converter!")
    
if __name__ == "__main__":
    main()
