#import pygame
import pygame
import pygame_widgets
from sys import exit
import button
import classes as cl
import calculations as calc
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from WineModel import wineEvaluator

#Global Game variables
pygame.font.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
TITLE_FONT = "./images+fonts/OLDENGL.TTF"

hasTime = False
gameDone = False
wineResult = None
wineDone = False
wineLevel = 0 
tempIndex = 1
temperature = 0
finalScore = -1
realFinalScore = -1

texts = ["Welcome! Click on an ingredient to start", #0
        "Click on check mark to confirm your selection", #1
        "Oops~ You need to choose a type of grape first", #2
        "Great! You have picked the grape!",            #3
        "Oops~ You need to choose a type of yeast first", #4
        "Great! You have picked the yeast!",                #5
        "Add additional ingredients before fermenting", #6
        "Congratulations! Your wine is finished!", #7
        "Fermenting ------ ",                   #8
        "You need to adjust your temperature!",#9
        ""                                      #-1
]
textIndex = 0

#For animation of dropping grape
triggerGrapeAnimation = False
grapeAnimationX = 130
grapeAnimationY = 80

#For animation of dropping yeast
triggerYeastAnimation = False
yeastAnimationX = 125
yeastAnimationY = 80

#Grape info
grapeSelected = ''
grapePh = 0
grapeAcidity = 0
grapeSugar = 0
grapeCheck = False
grapeUsed = None

#yeasr info 
yeastSelected = ''
yeastTemp = 0
yeastAlc = 0
yeastSpeed = 0
yeastCheck = False
yeastUsed = None

#wine variables 
sugarLevel = 0
SO2Level = 0
citrAcidLevel = 0

#fermenting info
isFermenting = False
fermentTime = 0

#initialize
pygame.init
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#set header
pygame.display.set_caption("Red Wine Simulator")

#create clock
clock = pygame.time.Clock()
    
#backgrounds
background = pygame.image.load("./images+fonts/background.jpeg")

#barrel
barrelImage = pygame.image.load('./images+fonts/barrel.png')
barrelImage = pygame.transform.smoothscale(barrelImage, (240, 300))

#title
title = pygame.font.Font(TITLE_FONT, 50)
titleSurface = title.render('Red Wine Making Simulator', True, 'white')

#create stats header
card = pygame.font.Font(TITLE_FONT, 40)
cardSurface = card.render('Wine Content', True, 'white')

#create stats
grapeType = pygame.font.SysFont("timesnewroman", 20)
yeastType = pygame.font.SysFont("timesnewroman", 20)
sugLevel = pygame.font.SysFont('timesnewroman', 20)
sulfurLevel = pygame.font.SysFont('timesnewroman', 20)
citricLevel = pygame.font.SysFont('timesnewroman', 20)

#create grape buttons
merlot_img = pygame.image.load('./images+fonts/merlot.png').convert_alpha()
merlot_button = button.Button(320, 100, merlot_img, .1)

cabSau_img = pygame.image.load('./images+fonts/cabSau.png').convert_alpha()
cabSau_button = button.Button(420, 100, cabSau_img, .1)

pinot_img = pygame.image.load('./images+fonts/pinot.png').convert_alpha()
pinot__button = button.Button(520, 100, pinot_img, .1)

check_img = pygame.image.load('./images+fonts/check.png').convert_alpha()
check_button = button.Button(620, 102, check_img, .05)

#create yeast buttons
cerev_img = pygame.image.load('./images+fonts/cerev.png').convert_alpha()
cerev_button = button.Button(320, 200, cerev_img, .13)

montra_img = pygame.image.load('./images+fonts/montra.png').convert_alpha()
montra_button = button.Button(420, 200, montra_img, .13)

prise_img = pygame.image.load('./images+fonts/prise.png').convert_alpha()
prise_button = button.Button(520, 200, prise_img, .13)

check_img2 = pygame.image.load('./images+fonts/check.png').convert_alpha()
check_button2 = button.Button(620, 202, check_img2, .05)

#create sugar button
sugar_img = pygame.image.load('./images+fonts/add.png').convert_alpha()
sugar_button = button.Button(620, 400, sugar_img, .12)


#create sulfur dioxide button
sulfur_img = pygame.image.load('./images+fonts/add.png').convert_alpha()
sulfur_button = button.Button(620, 300, sulfur_img, .12)

#create citric acid button
citric_img = pygame.image.load('./images+fonts/add.png').convert_alpha()
citric_button = button.Button(620, 500, citric_img, .12)

#create ferment button
fermentBackground = pygame.image.load("./images+fonts/ferment.jpg")
fermentBackground = pygame.transform.smoothscale(fermentBackground, (300, 150))
ferment_button = button.Button(754, 510, fermentBackground, 1)

#create temperature slider
# temperatureSlider = Slider(screen, 320, 325, 150, 20, min=10.0, max=40.0, step=0.5)
# temperatureText = TextBox(screen, 375, 350, 50, 25, fontSize=13)
# temperatureText.disable()
temperatureSlider = Slider(screen, 470, 330, 20, 20, min=0.0, max=40.0, step=0.5, initial = 0.0)
temperatureText = TextBox(screen, 420, 440, 43, 20, fontSize=12, radius = 5)
temperatureText.disable()
temperatureSlider.vertical = True
temperatureSlider._height = 240

while True:
    #check quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #refresh temperature slider text
    if not(isFermenting or gameDone):
        temperature = temperatureSlider.getValue()
    #temperatureText.setText(temperature)
    temperatureSlider.value = temperature
    temperatureText.setText(str(round(temperatureSlider.getValue(), 1)) + " ˚C")

    #load background, barrel, and title
    screen.fill((165,42,42))
    screen.blit(background, (0, 0))
    screen.blit(barrelImage, (30, 290))
    screen.blit(titleSurface, (72, 30))
    pygame.draw.line(screen, '#c88949', (250, 360), (300, 390), 15)

    #load and fill wine glass once finished fermenting
    if gameDone == True:

        wineImage = pygame.image.load('./images+fonts/wine.png')
        wineImage = pygame.transform.smoothscale(wineImage, (85, 85))
        wineImage = wineImage.subsurface(0, 85-wineLevel, 85, wineLevel)
        screen.blit(wineImage, (287, 510 - wineLevel))
        if wineLevel < 55:
            wineLevel += .7
            pygame.draw.line(screen, '#700a00', (300, 390), (300, 425), 5)
            pygame.draw.line(screen, '#CD7F32', (250, 360), (300, 390), 15)

        if wineLevel > 53:
            wineDone = True

        glassImage = pygame.image.load('./images+fonts/glass.png')
        glassImage = pygame.transform.smoothscale(glassImage, (180, 220))
        screen.blit(glassImage, (240, 400))

    #load lines on card
    pygame.draw.line(screen, 'white', (750,0), (750,600), 5)
    pygame.draw.line(screen, 'white', (750,75), (1000,75), 5)
    pygame.draw.line(screen, 'white', (750,225), (1000,225), 5)
    pygame.draw.line(screen, 'white', (750,375), (1000,375), 5)

    #load and refresh stats
    grapeSurface = grapeType.render("Grape Type: " + grapeSelected, True, 'white')
    grapePhSurface = pygame.font.SysFont('timesnewroman', 15).render("PH Level: " + str(grapePh), True, 'white')
    grapeSugarSurface = pygame.font.SysFont('timesnewroman', 15).render("Sugar Index: " + str(grapeSugar), True, 'white')
    grapeAciditySurface = pygame.font.SysFont('timesnewroman', 15).render("Fixed Acidity: " + str(grapeAcidity), True, 'white')

    yeastSurface = yeastType.render("Yeast Type: " + yeastSelected, True, 'white')
    yeastTempSurface = pygame.font.SysFont('timesnewroman', 15).render("Ideal Temperature: " + str(yeastTemp), True, 'white')
    yeastAlcSurface = pygame.font.SysFont('timesnewroman', 15).render("Alcohol Tolerance: " + str(yeastAlc), True, 'white')
    yeastSpeedSurface = pygame.font.SysFont('timesnewroman', 15).render("Fermentation Speed: " + str(yeastSpeed), True, 'white')

    sugarSurface = sugLevel.render("Sugar Level: " + str(sugarLevel), True, 'white')

    sulfurSurface = sulfurLevel.render("Sulfur Dioxide Level: " + str(SO2Level), True, 'white')

    citricSurface = citricLevel.render("Citric Acid Level: " + str(round(citrAcidLevel, 1)), True, 'white')

    screen.blit(cardSurface, (765, 20))

    screen.blit(grapeSurface, (765, 90))
    screen.blit(grapePhSurface, (765, 130))
    screen.blit(grapeSugarSurface, (765, 160))
    screen.blit(grapeAciditySurface, (765, 190))

    screen.blit(yeastSurface, (765, 240))
    screen.blit(yeastTempSurface, (765, 280))
    screen.blit(yeastAlcSurface, (765, 310))
    screen.blit(yeastSpeedSurface, (765, 340))

    screen.blit(sulfurSurface, (765, 390))
    screen.blit(sugarSurface, (765, 430))
    screen.blit(citricSurface, (765, 470))

    #create instructions words
    instructionsSurface = pygame.font.SysFont('timesnewroman', 15).render(texts[textIndex], True, 'white')
    screen.blit(instructionsSurface, (30, 100))
    # instructionsSurface = pygame.font.SysFont('timesnewroman', 15).render("instructions", True, 'white')
    # screen.blit(instructionsSurface, (30, 115))

    #Click grape buttons to update info card
    if grapeCheck == False or grapeSelected == "Merlot":
        if merlot_button.draw(screen):
            if(not grapeCheck): 
                textIndex = 1
            if grapeSelected != "Merlot" and grapeCheck == False:
                grapeSelected = 'Merlot'
                grapePh = 3.3
                grapeSugar = 24.25
                grapeAcidity = 0.725

    if grapeCheck == False or grapeSelected == "Cabernet":
        if cabSau_button.draw(screen):
            if(not grapeCheck):
                textIndex = 1
            if grapeSelected != "Cabernet" and grapeCheck == False:
                grapeSelected = 'Cabernet'
                grapePh = 3.35
                grapeSugar = 25.25
                grapeAcidity = 0.65

    if grapeCheck == False or grapeSelected == "Pinot Noir":
        if pinot__button.draw(screen):
            if(not grapeCheck):
                textIndex = 1
            if grapeSelected != "Pinot Noir" and grapeCheck == False:
                grapeSelected = 'Pinot Noir'
                grapePh = 3.25
                grapeSugar = 23.5
                grapeAcidity = 0.725

    #drop the grape into the barrel
    #only if one grape is selected
    if check_button.draw(screen):
        if grapeSelected == '':
            textIndex = 2
        if grapeSelected != '' and grapeCheck == False:
            textIndex = 3
            grapeCheck = True
            #animate grape selection
            if grapeSelected == "Merlot":
                animatedGrape = './images+fonts/merlot.png'
                grapeUsed = cl.Grape("Merlot", 3.3, 0.1, 24.25, 1.25, 0.725, 0.075, 3.6, 0.05)
            if grapeSelected == "Cabernet":
                animatedGrape = './images+fonts/cabSau.png'
                grapeUsed = cl.Grape("Cabernet Sauvignon", 3.35, 0.05, 25.25, 1.25, 0.65, 0.05, 3.65, 0.05)
            if grapeSelected == "Pinot Noir":
                animatedGrape = './images+fonts/pinot.png'
                grapeUsed = PinNoi = cl.Grape("Pinot Noir", 3.25, 0.05, 23.5, 1.5, 0.725, 0.075, 3.525, 0.025)
            triggerGrapeAnimation = True
    
    #animate grape dropping
    if triggerGrapeAnimation and grapeAnimationY < 270:
        animatedGrapeImage = pygame.transform.smoothscale(pygame.image.load(animatedGrape), (40, 40))
        screen.blit(animatedGrapeImage, (grapeAnimationX, grapeAnimationY))
        grapeAnimationY += 4

    #Click yeast buttons to update info card 
    if yeastCheck == False or yeastSelected == "S. Cerevisiae":
        if cerev_button.draw(screen):
            if(not yeastCheck):
                textIndex = 1
            if yeastSelected != "S. Cerevisiae" and yeastCheck == False:
                yeastSelected = 'S. Cerevisiae'
                yeastTemp = "22 - 30 ˚C"
                yeastAlc = "13.5%"
                yeastSpeed = 2

    if yeastCheck == False or yeastSelected == "Montrachet":
        if montra_button.draw(screen):
            if(not yeastCheck):
                textIndex = 1
            if yeastSelected != "Montrachet" and yeastCheck == False:
                yeastSelected = 'Montrachet'
                yeastTemp = "12 - 35 ˚C"
                yeastAlc = "15%"
                yeastSpeed = 1

    if yeastCheck == False or yeastSelected == "Prise de Mousse":
        if prise_button.draw(screen):
            if(not yeastCheck):
                textIndex = 1
            if yeastSelected != "Prise de Mousse" and yeastCheck == False:
                yeastSelected = 'Prise de Mousse'
                yeastTemp = "7 - 35 ˚C"
                yeastAlc = "18%"
                yeastSpeed = 3

    #drop the yeast into the barrel 
    #only if one yeast is selected
    if check_button2.draw(screen):
        if yeastSelected != '':
            if not yeastCheck: 
                yeastCheck = True
                textIndex = 5
                #animate yeast selection
                if yeastSelected == "S. Cerevisiae":
                    yeastUsed = cl.Yeast("S. Cerevisiae", 13.5, 26, 2, 4)
                    animatedYeast = './images+fonts/cerev.png'
                if yeastSelected == "Montrachet":
                    yeastUsed = cl.Yeast("Montrachet", 15, 23.5, 1, 11.5)
                    animatedYeast = './images+fonts/montra.png'
                if yeastSelected == "Prise de Mousse":
                    yeastUsed = cl.Yeast("Prise de Mousse", 18, 21, 3, 14)
                    animatedYeast = './images+fonts/prise.png'
                triggerYeastAnimation = True
        else:
            textIndex = 4
    
    #animate yeast dropping
    if triggerYeastAnimation and yeastAnimationY < 270:
        animatedYeastImage = pygame.transform.smoothscale(pygame.image.load(animatedYeast), (50, 50))
        screen.blit(animatedYeastImage, (yeastAnimationX, yeastAnimationY))
        yeastAnimationY += 4

    #next step/add additional ingredients instructions 
    if(yeastCheck and grapeCheck and not isFermenting and not gameDone and not textIndex == 9):
        textIndex = 6

    #load sugar button
    if sugar_button.draw(screen) and (not gameDone) and (not isFermenting):
        sugarLevel += 1
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render("Add Sugar", True, 'white'), (515, 418))

    #load sulfur button
    if sulfur_button.draw(screen) and (not gameDone) and (not isFermenting):
        SO2Level += 5
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render("Add Sulfur", True, 'white'), (515, 310))
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render("Dioxide", True, 'white'), (527, 332))

    #load citric button
    if citric_button.draw(screen) and (not gameDone) and (not isFermenting):
        citrAcidLevel += 0.1
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render("Add Citric", True, 'white'), (515, 510))
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render("Acid", True, 'white'), (540, 532))

    #load and update ferment button and its function 
    if ferment_button.draw(screen):
        if(not gameDone):
            if(grapeCheck): 
                if(yeastCheck): 
                    if(yeastUsed.isGoodTemp(temperature)):
                        if isFermenting == False:
                            isFermenting = True
                        else:
                            isFermenting = False
                            fermentTime = (pygame.time.get_ticks() - firstTime) / 1000
                            wineResult = calc.ferment(grapeUsed, yeastUsed, SO2Level, sugarLevel, citrAcidLevel, fermentTime, tempIndex)
                            print("Loading...")
                            screen.blit(pygame.font.Font(TITLE_FONT, 60).render("Loading", True, '#DAA520'), (54, 158))
                            pygame.display.update()
                            finalScore = wineEvaluator(wineResult)
                            finalArray = calc.wineScoreCalculator(finalScore, wineResult, fermentTime)
                            realFinalScore = round(finalArray[0], 1)
                            gameDone = True
                            textIndex = 7
                    else:
                        textIndex = 9 #not within temp range
                else:
                    textIndex = 4 #no yeast added
            else:
                textIndex = 2 #no grape added
    
    #start the timer when fermentation starts
    if isFermenting and (not gameDone):
        if hasTime == False:
            firstTime = pygame.time.get_ticks()
            hasTime = True
        time = int (2 * int((pygame.time.get_ticks() - firstTime) / 100) / 10)

    #Texts on ferment button 
    if isFermenting == False and gameDone == False:
        screen.blit(pygame.font.Font(TITLE_FONT, 50).render("Ferment", True, '#DAA520'), (786, 527))
    elif(isFermenting == False and gameDone == True):
        textIndex = -1
        screen.blit(pygame.font.Font(TITLE_FONT, 35).render("Completed", True, '#DAA520'), (800, 515))
        screen.blit(pygame.font.Font(TITLE_FONT, 35).render("Day " + str(time), True, '#DAA520'), (830, 555))
    else:
        textIndex = 8
        screen.blit(pygame.font.Font(TITLE_FONT, 35).render("Click to Stop", True, '#DAA520'), (780, 515))
        screen.blit(pygame.font.Font(TITLE_FONT, 35).render("Day " + str(time), True, '#DAA520'), (830, 555))

    #load temperature label
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render("Temperature", True, 'white'), (425, 275))
    pygame_widgets.update(pygame.event.get())

    #if game is done
    if wineDone == True:
        pygame.draw.line(screen, '#DAA520', (20, 100), (300, 100), 5)
        pygame.draw.line(screen, '#DAA520', (300, 100), (300, 275), 5)
        pygame.draw.line(screen, '#DAA520', (20, 275), (300, 275), 5)
        pygame.draw.line(screen, '#DAA520', (20, 100), (20, 275), 5)
        j = 0
        for i in range(1, len(finalArray)):
            if finalArray[i] != '':       
                screen.blit(pygame.font.SysFont('timesnewroman', 15).render(finalArray[i], True, 'white'), (30, 110+j))
                j = j + 20
        
        finalBackground = pygame.image.load('./images+fonts/ferment.jpg')
        finalBackground = pygame.transform.smoothscale(finalBackground, (300, 150))
        screen.blit(finalBackground, (350, 200))
        pygame.draw.line(screen, '#DAA520', (350, 200), (350, 350), 5)
        pygame.draw.line(screen, '#DAA520', (350, 350), (650, 350), 5)
        pygame.draw.line(screen, '#DAA520', (650, 350), (650, 200), 5)
        pygame.draw.line(screen, '#DAA520', (350, 200), (650, 200), 5)
        screen.blit(pygame.font.Font(TITLE_FONT, 30).render("Final wine's rating: " + str(round(realFinalScore, 1)), True, '#DAA520'), (358, 232))
        if realFinalScore <= 3.5:
            screen.blit(pygame.font.Font(TITLE_FONT, 25).render("The wine may be poisonous...", True, 'green'), (355, 288))
        elif realFinalScore <= 7.5:
            screen.blit(pygame.font.Font(TITLE_FONT, 25).render("The wine is decent.", True, 'white'), (405, 288))
        elif realFinalScore <= 10:
            screen.blit(pygame.font.Font(TITLE_FONT, 25).render("The wine is excellent!", True, '#DAA520'), (392, 288))
        else:
            screen.blit(pygame.font.Font(TITLE_FONT, 25).render("...", True, 'black'), (355, 280))


    #update elements
    pygame.display.update()
    clock.tick(60)
