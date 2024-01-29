import numpy as np

class Yeast: 
    def __init__(self, name, alcTol, temp, speed, tempRange): 
        self.name = name
        self.alcTol = alcTol
        self.temp = temp
        self.speed = speed
        self.tempRange = tempRange
    def isGoodTemp(self, target):
        return (target >= (self.temp - self.tempRange)) and (target <= (self.temp + self.tempRange))
    def printInfo(self):
        print(self.name + ": ")
        print("Alcohol tolerance: " + str(self.alcTol))
        print("Functional temperature range: " + str(round((self.temp - self.tempRange), 2)) + " - " + str(round((self.temp + self.tempRange), 2)))
        print("Fermentation power factor: " + str(self.speed))

class Grape: 
    #Brix: A measurement of the sugar content of grapes, must and wine, 
    #indicating the degree of the grapes' ripeness (meaning sugar level) at harvest. 
    #Most table-wine grapes are harvested at between 21 and 25 Brix. 
    #To get an alcohol conversion level, multiply the stated Brix by .55.
    def __init__(self, name, pH, pHrange, brix, brixRange, TA, TArange, finalpH, finalpHrange): 
        self.name = name
        self.pH = pH
        self.pHrange = pHrange
        self.brix = brix
        self.brixRange = brixRange
        self.TA = TA
        self.TArange = TArange
        self.finalpH = finalpH
        self.finalpHrange = finalpHrange
        self.rTA = self.generateTA()
        self.rBrix = self.generateBrix()
        self.rFinalpH = self.generateFinalpH()
    def isGoodTemp(self, target): 
        return (target >= (self.temp - self.tempRange)) and (target <= (self.temp + self.tempRange))
    def getAlcoholLevel(self):
        return (self.brix) * 0.55
    def printInfo(self):
        print(self.name + ": ")
        print("pH range: " + str(round((self.pH - self.pHrange), 2)) + " - " + str(round((self.pH + self.pHrange), 2)))
        print("Brix index: " + str(round((self.brix - self.brixRange), 2)) + " - " + str(round((self.brix + self.brixRange), 2)))
        print("Titratable Acidity: " + str(round((self.TA - self.TArange), 2)) + " - " + str(round((self.TA + self.TArange), 2)))
        print("Final pH range: " + str(round((self.finalpH - self.finalpHrange), 2)) + " - " + str(round((self.finalpH + self.finalpHrange), 2)))
    def generateBrix(self):
        return np.random.normal(self.brix, self.brixRange/3)
    def generateTA(self):
        return np.random.normal(self.TA, self.TArange/3)
    def generateFinalpH(self):
        return np.random.normal(self.finalpH, self.finalpHrange/3)
    def generateInitialPH(self):
        return np.random.normal(self.pH, self.pHrange/3)

#prise = cl.Yeast("Prise de Mousse", 18, 21, 3, 14)
# #A very good fermenter with regular kinetics. 
# #Good alcohol tolerance that is useful in producing dry, full-bodied red and white wines. 
# #Excellent choice for oak barrel fermentation.
# montrachet = cl.Yeast("Montrachet", 15, 23.5, 1, 11.5)

# #Ideal for light, fruity red wines for early consumption
# Cerev = cl.Yeast("S. Cerevisiae", 13.5, 26, 2, 4)

# #The Grapes 
# #Unique oak aroma and mild acidity
# CabSau = cl.Grape("Cabernet Sauvignon", 3.35, 0.05, 25.25, 1.25, 0.65, 0.05, 3.65, 0.05)

# #Fruity flavor and lower acidity
# Merlot = cl.Grape("Merlot", 3.3, 0.1, 24.25, 1.25, 0.725, 0.075, 3.6, 0.05)

# #Lush and velvety texture with higher acidity 
# PinNoi = cl.Grape("Pinot Noir", 3.25, 0.05, 23.5, 1.5, 0.725, 0.075, 3.525, 0.025)

# PinNoi.printInfo()
    
# prise = Yeast("Prise de Mousse", 18, 21, 3, 14)

# #A very good fermenter with regular kinetics. 
# #Good alcohol tolerance that is useful in producing dry, full-bodied red and white wines. 
# #Excellent choice for oak barrel fermentation.
# montrachet = Yeast("Montrachet", 15, 23.5, 1, 11.5)

# #Ideal for light, fruity red wines for early consumption
# Cerev = Yeast("S. Cerevisiae", 13.5, 26, 2, 4)

# #The Grapes 
# #Unique oak aroma and mild acidity
# CabSau = Grape("Cabernet Sauvignon", 3.35, 0.05, 25.25, 1.25, 0.65, 0.05, 3.65, 0.05)

# #Fruity flavor and lower acidity
# Merlot = Grape("Merlot", 3.3, 0.1, 24.25, 1.25, 0.725, 0.075, 3.6, 0.05)

# #Lush and velvety texture with higher acidity 
# PinNoi = Grape("Pinot Noir", 3.25, 0.05, 23.5, 1.5, 0.725, 0.075, 3.525, 0.025)