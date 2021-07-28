#Converter by kBowen
#globes
values = ["Miles", "Ounces", "Meters", "Liters", "Degress F", "Degrees C"]
            #0       1          2            3             4       5
class Conversions:
    """Conversion Algorithms"""

    @staticmethod
    def valcheck(checker, arval):
        if not isinstance(checker, (int, float)):
            try:
                checker = float(checker)
                return checker
            except ValueError:
                raise Exception(values[arval] + " was not numeric")

    @staticmethod
    def valcheck2(checker, arval):
        if (arval <4):
            if(checker<=0.0):
                raise ValueError(values[arval] + " cannot be negative")
        elif(arval ==4):
            if(checker< -459.67):
                raise ValueError(values[arval] + " is below 0 K")
        elif(arval ==5):
            if(checker < -273.15):
                raise ValueError(values[arval] + " is below 0 K")
        else:
            raise Exception("Error in value check")


    @staticmethod
    def MitoKm(mi):
        arval = 0
        checker = mi
        Conversions.valcheck(checker, arval)
        Conversions.valcheck2(float(checker), arval)
        km = float(checker) * 1.60934
        return km

    @staticmethod
    def OztoGr(oz):
        arval = 1
        checker = oz
        Conversions.valcheck(checker, arval)
        Conversions.valcheck2(float(checker), arval)
        gr = 28.3495 * float(checker)
        return gr

    @staticmethod
    def FatoCe(fa):
        arval = 4
        checker = fa
        Conversions.valcheck(checker, arval)
        Conversions.valcheck2(float(checker), arval)
        ce = (5/9)*(float(checker)-32)
        return ce

    @staticmethod
    def CetoFa(ce):
        arval = 5
        checker = ce
        Conversions.valcheck(checker, arval)
        Conversions.valcheck2(float(checker), arval)
        fa = (9/5 * float(checker)) +32
        return fa

    @staticmethod
    def MetoFt(me):
        arval = 2
        checker = me
        Conversions.valcheck(checker, arval)
        Conversions.valcheck2(float(checker), arval)
        ft = float(checker) * 3.2808
        return ft

    @staticmethod
    def LitoGa(li):
        arval = 3
        checker = li
        Conversions.valcheck(checker, arval)
        Conversions.valcheck2(float(checker), arval)
        ga = 2.6417 * float(checker)
        return ga
    
    @staticmethod
    def getK(ce):
        K = float(ce) + 273.15
        return K

    
