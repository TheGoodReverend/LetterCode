#LetterCodeLogic by KBowen

class LetterCodeLogic:
    """This is the Encode/Decode Methods"""


    @staticmethod
    def Encode(msg):
        result = ""
        
        nums = msg.upper() #up convert
        for x in nums:
            try:
                n = (ord(x) - 64)
                if n ==32:
                    n == 0
                elif n == -32:
                    n=0
                elif n<0:
                    n="?"
                
            except ValueError:
                n = "?"
            result += str(n) + ","
        return result


    @staticmethod
    def Decode(msg):
        #method to split msg string and decode numbers inside
        result = ""
        #seperate string such as
        nums = msg.split(",")  #splits string into list by commas

        #walk through element in list nums
        for x in nums:
            #convert string x into numbers
            try:
                n = int(x.strip())
                if n == 0:
                    c = " "
                elif n < 1 or n > 26:
                    c = "?"
                else:
                    c = chr(n+64) #character from unicode value
            except ValueError:
                c = "?"
            result += c
        return result
