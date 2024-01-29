import classes
import numpy as np
import math

def wineScoreCalculator(quality, fixAcid, volAcid, citAcid, resSug, chlorides, freeSulDio, totalSulDio, density, pH, sulphates, alcohol):
    GOOD = (quality == 1)
    finalScore = 0 
    if(quality == 1):
        finalScore += 7
    elif(quality == 0):
        finalScore += 4
    else:
        return -1
    
    if(GOOD and fixAcid > 8):
        finalScore += 0.2
    elif(not GOOD and fixAcid < 8):
        finalScore -= 0.2

    if(volAcid > 0.4):
        finalScore -= 0.9
    
    if(citAcid > 0.3):
        finalScore += 0.5

    if(not GOOD and resSug > 3):
        finalScore -= 0.2

    if(not GOOD and chlorides > 0.1):
        finalScore -= 0.2
    
    if(not GOOD and freeSulDio < 10):
        finalScore -= 0.4
    elif(GOOD and freeSulDio > 15):
        finalScore -= 0.4
    
    if(totalSulDio > 50):
        finalscore -= 0.5

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
    
    if(alcohol > 12):
        finalScore += 0.7
    elif(alcohol < 10.8):
        finalScore -= 0.5
    
    if(finalScore > 10):
        print("Your wine is too good")
        print(finalScore, end = ' ') 
        finalScore = 10
    elif(finalScore < 1):
        print("Your wine is too bad")
        print(finalScore, end = ' ') 
        finalScore = 1
    return finalScore

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
# alcohol = alcTol - alcTol * e ^ -(sqrt(fermPower) / 5 / tempIndex) * time
    
def calcFixAcid(grape, timePassed):
# fixed acidity = 8 + max(0, TitrativeAcidity * NormalDistribution(center = 4, S.D. = 0.5)) - time/10
    return 8 + max(0, grape.rTA * np.random.normal(4, 0.5)) - timePassed / 10

def calcVolAcid(addedSO2, timePassed, tempIndex): 
# Volatile acidity = 2 over (1 + e^-(1/2)(x - SO2added^2 / 60))
    return 2 / (1 + (1 / tempIndex) * math.exp(-1/2*(timePassed - (addedSO2 * addedSO2) / 60)))

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
# alcohol = alcTol - alcTol * e ^ -(sqrt(fermPower) / 5 / tempIndex) * time
    return yeast.alcTol - yeast.alcTol * math.exp(math.sqrt(yeast.speed) / -5 * tempIndex * timePassed)

def ferment(grape, yeast, addedSO2, addedSugar, addedCitrAcid, timePassed, tempIndex):
    fixAcid = calcFixAcid(grape, timePassed)
    volAcid = calcVolAcid(addedSO2, timePassed, tempIndex) 
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
