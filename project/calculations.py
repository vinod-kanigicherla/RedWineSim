import classes
import numpy as np
import math

def wineScoreCalculator(quality, wineResult, timePassed):
    GOOD = (quality == 1)
    #wineResult = [fixAcid, volAcid, citrAcid, resSug, chlorides, freeSO2, totSO2, density, pH, sulphate, alcohol]
    fixAcid = wineResult[0]
    volAcid = wineResult[1]
    citAcid = wineResult[2]
    resSug = wineResult[3]
    chlorides = wineResult[4]
    freeSulDio = wineResult[5]
    totalSulDio  = wineResult[6] 
    density = wineResult[7]
    pH = wineResult[8]
    sulphates = wineResult[9]
    alcohol = wineResult[10]
    finalScore = 0 
    if(quality == 1):
        finalScore += 7
    elif(quality == 0):
        finalScore += 4
    else:
        return -1
    
    message1 = ""
    message2 = ""
    message3 = ""
    message4 = ""
    message5 = ""
    message6 = ""
    message7 = ""
    message8 = ""
    message9 = ""
    message10 = ""
    message11 = ""
    if(quality == 1):
        finalScore += 7
    elif(quality == 0):
        finalScore += 4
    else:
        return -1
    if(timePassed < 4.5):
        finalScore -= 4
        message11 = "You should ferment for longer!"
    if(GOOD and fixAcid > 8):
        finalScore += 0.2
    elif(not GOOD and fixAcid < 8):
        finalScore -= 0.2
        message1 = "Your wine is not sour enough!"
        message2 = "- Try different grape or less fermenting time."

    if(volAcid > 0.4):
        finalScore -= 0.9
        message3 = "Your wine contains too much bacteria!"
        message4 = "- Try faster yeast, less time or more SO2."
    
    if(citAcid > 0.3 and citAcid < 0.6):
        finalScore += 0.5
        message5 = "Good citric acid amount!"

    if(not GOOD and resSug > 3):
        finalScore -= 0.2
        message6 = "Your wine is too sweet. "
        message7 = "- Try ferment more or less sugar."

    if(not GOOD and chlorides > 0.1):
        finalScore -= 0.2
    
    if(not GOOD and freeSulDio < 10):
        finalScore -= 0.4
        message8 = "You may have added too little SO2."

    elif(GOOD and freeSulDio > 30):
        finalScore -= 0.4
        message8 = "You may have added too much SO2."
    
    if(totalSulDio > 60):
        finalScore -= 0.5
        message8 = "You may have added too much SO2."

    if(density > 0.9975):
        finalScore -= 0.5
    elif(density < 0.9955):
        finalScore += 0.5

    if(pH > 3.45):
        finalScore -= 0.3
    elif(pH < 3.3):
        finalScore += 0.3
    
    if(sulphates > 0.7):
        finalScore += 0.6
    elif(sulphates < 0.6):
        finalScore -= 0.4
    
    if(alcohol > 12 and alcohol < 15):
        finalScore += 0.7
        message9 = "Your alcohol content is excellent!"

    elif(alcohol < 10.8):
        finalScore -= 0.5
        message10 = "Your alcohol content is low."
        message11 = "- Try fermenting longer or another yeast!"
    
    if(finalScore > 10):
        #print("Your wine is too good")
        print(finalScore, end = ' ') 
        finalScore = 10.0
    elif(finalScore < 1):
        #print("Your wine is too bad")
        print(finalScore, end = ' ') 
        finalScore = 1.0
    return [finalScore, message1, message2, message3, message4, message5, message6, message7, message8, message9, message10, message11]

# print(wineScoreCalculator(1, 9, 0.7, 0.4, 2, 0.1, 10, 30, 0.997, 3.3, 0.7, 11)) #6.8
# print(wineScoreCalculator(0, 9, 0.7, 0.4, 2, 0.1, 10, 30, 0.997, 3.3, 0.7, 11)) #3.6
# print(wineScoreCalculator(1, 9, 0.4, 0.4, 2, 0.09, 8, 20, 0.995, 3.3, 0.9, 12.5)) #9.5

# 1 - fixed acidity (tartaric acid - g / dm^3) 6 - 16
# 2 - volatile acidity (acetic acid - g / dm^3) 0.2 - 1.6
# 3 - citric acid (g / dm^3) 0 - 1.0 
# 4 - residual sugar (g / dm^3) 1 - 5 5 ~ 16
# 5 - chlorides (sodium chloride - g / dm^3 0.09 - 0.15 ~ 0.6
# 6 - free sulfur dioxide (mg / dm^3) 5 - 25 ~ 70
# 7 - total sulfur dioxide (mg / dm^3) 10 - 90 ~ 300
# 8 - density (g / cm^3) 0.990 ~ 0.994 - 0.999 ~ 1.004
# 9 - pH 2.8 ~ 3.2 - 3.5 ~ 4.0
# 10 - sulphates (potassium sulphate - g / dm3) 0.3 - 0.85 ~ 2.000
# 11 - alcohol (% by volume) 8 ~ 9 - 13 ~ 15

# fixed acidity = 8 + max(0, TitrativeAcidity * NormalDistribution(center = 4, S.D. = 0.5)) - time/10
# Volatile acidity = 2 over (1 + e^-(1/2)(x - SO2added^2 / 60))
# citric acid = TitrativeAcidity * 0.1 + addedCitricAcid
# resSugar = max(0, addedSugar * 1.5 + Brix * 0.55 - Alcohol) 
# chlorides = max(0, N.D.(c = 0.09, S.D. = 0.02)) 
# free sulfur dioxide = addedSO2 - t
# total sulfur dioxide = freeSO2 * N.D(c = 3, S.D. = 0.2)
# Density = 1 * (1 - alcohol/100) + alcohol/100 * 0.79 + citricAcid * 0.06 + residualSugar * 0.0015 + fixedAcidity * 0.0015
# pH = Final Ph + 0.5 - fixedAcidity * 0.07 - citric * 0.5 + volatile acidity * 0.1
# Sulphate = (freeSO2 + totSO2) / 150 
# alcohol = alcTol - alcTol * e ^ -(sqrt(fermPower) / 5 * tempIndex) * time
    
def calcFixAcid(grape, timePassed):
# fixed acidity = 8 + max(0, TitrativeAcidity * NormalDistribution(center = 4, S.D. = 0.5)) - time/10
    return 8 + max(0, grape.rTA * np.random.normal(4, 0.5)) - timePassed / 10

def calcVolAcid(addedSO2, timePassed): 
# Volatile acidity = 2 over (1 + e^-(1/2)(x - SO2added^2 / 60))
    return 2 / (1 + math.exp(-1/2*(timePassed - (addedSO2 * addedSO2) / 60)))

def calcCitrAcid(grape, addedCitrAcid):
# citric acid = TitrativeAcidity * 0.1 + addedCitricAcid
    return grape.rTA * 0.1 + addedCitrAcid

def calcResSug(grape, addedSugar, alcohol):
# resSugar = max(0, addedSugar * 1.5 + Brix * 0.55 - Alcohol) 
    return max(0, addedSugar * 1.5 + grape.rBrix * 0.55 - alcohol)

def calcChlorides():
# chlorides = max(0, N.D.(c = 0.09, S.D. = 0.02)) 
    return max(0, np.random.normal(0.09, 0.02))

def calcFreeSO2(addedSO2, timePassed):
# free sulfur dioxide = addedSO2 - t
    return max(0, addedSO2 - timePassed)

def calcTotSO2(freeSO2): 
# total sulfur dioxide = freeSO2 * N.D(c = 3, S.D. = 0.2)
    return max(0, freeSO2 * np.random.normal(3, 0.2)) 

def calcDensity(alcohol, citrAcid, resSug, fixAcid):
# Density = 1 * (1 - alcohol/100) + alcohol/100 * 0.79 + citricAcid * 0.06 + residualSugar * 0.0015 + fixedAcidity * 0.0015
    return (1 - alcohol / 100 * 0.21) + (citrAcid * 0.06) + (resSug * 0.0015) + (fixAcid * 0.0015)

def calcPH(grape, fixAcid, citrAcid, volAcid):
# pH = Final Ph + 0.5 - fixedAcidity * 0.07 - citric * 0.5 + volatile acidity * 0.1
    return (grape.rFinalpH + 0.5) - (fixAcid * 0.07) - (citrAcid * 0.5) + (volAcid * 0.1)

def calcSulphate(freeSO2, TotSO2):
# Sulphate = (freeSO2 + totSO2) / 150 
    return (freeSO2 + TotSO2) / 150 

def calcAlcohol(yeast, tempIndex, timePassed): 
# alcohol = alcTol - alcTol * e ^ -(sqrt(fermPower) / 5 * tempIndex) * time
    return yeast.alcTol - yeast.alcTol * math.exp(math.sqrt(yeast.speed) / -5 * tempIndex * timePassed)

def ferment(grape, yeast, addedSO2, addedSugar, addedCitrAcid, timePassed, tempIndex):
    fixAcid = calcFixAcid(grape, timePassed)
    volAcid = calcVolAcid(addedSO2, timePassed) 
    citrAcid = calcCitrAcid(grape, addedCitrAcid)
    alcohol = calcAlcohol(yeast, tempIndex, timePassed)
    resSug = calcResSug(grape, addedSugar, alcohol)
    chlorides = calcChlorides() 
    freeSO2 = calcFreeSO2(addedSO2, timePassed)
    totSO2 = calcTotSO2(freeSO2)
    density = calcDensity(alcohol, citrAcid, resSug, fixAcid)
    pH = calcPH(grape, fixAcid, citrAcid, volAcid)
    sulphate = calcSulphate(freeSO2, totSO2)

    return [fixAcid, volAcid, citrAcid, resSug, chlorides, freeSO2, totSO2, density, pH, sulphate, alcohol]

# texts = ["Welcome! Click on an ingredient to start",
#         "Click on check mark to confirm your selection", 
#         "You need to choose a type of grape first", 
#         "Great! You have picked the grape"
#         "You need to choose a type of yeast first", 
#         "Great! You have picked the yeast"
#         "You can add additional ingredients before fermenting", 
#         "Congratulations! Your wine is finished!", 
#         "Your wine tastes horrible :((", 
#         "Your wine is exceptional :))", 
# ]
