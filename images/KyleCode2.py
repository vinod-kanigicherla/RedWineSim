#import pygame
import pygame
import pygame_widgets
from sys import exit
import button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import time as delay

#variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
TITLE_FONT = "oldenglishtext"

triggerGrapeAnimation = False
grapeAnimationX = 130
grapeAnimationY = 80

triggerYeastAnimation = False
yeastAnimationX = 125
yeastAnimationY = 80

grapeSelected = ''
grapePh = 0
grapeAcidity = 0
grapeSugar = 0
grapeCheck = False

yeastSelected = ''
yeastTemp = 0
yeastAlc = 0
yeastSpeed = 0
yeastCheck = False
temperature = 0

isFermenting = False
hasTime = False
gameDone = False
wineLevel = 0
wineDone = False

#initialize
pygame.init
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#set header
pygame.display.set_caption("Red Wine Simulator")

#create clock
clock = pygame.time.Clock()
    
#backgrounds
background = pygame.image.load("background.jpeg")

#barrel
barrelImage = pygame.image.load('barrel.png')
barrelImage = pygame.transform.smoothscale(barrelImage, (240, 300))

#title
title = pygame.font.SysFont(TITLE_FONT, 50)
titleSurface = title.render('Red Wine Making Simulator', True, 'white')

#create stats header
card = pygame.font.SysFont("oldenglishtext", 40)
cardSurface = card.render('Wine Content', True, 'white')

#create stats
grapeType = pygame.font.SysFont("timesnewroman", 20)
yeastType = pygame.font.SysFont("timesnewroman", 20)
sugarLevel = pygame.font.SysFont('timesnewroman', 20)
sulfurLevel = pygame.font.SysFont('timesnewroman', 20)
citricLevel = pygame.font.SysFont('timesnewroman', 20)

#create grape buttons
merlot_img = pygame.image.load('merlot.png').convert_alpha()
merlot_button = button.Button(320, 100, merlot_img, .1)

cabSau_img = pygame.image.load('cabSau.png').convert_alpha()
cabSau_button = button.Button(420, 100, cabSau_img, .1)

pinot_img = pygame.image.load('pinot.png').convert_alpha()
pinot__button = button.Button(520, 100, pinot_img, .1)

check_img = pygame.image.load('check.png').convert_alpha()
check_button = button.Button(620, 102, check_img, .05)

#create yeast buttons
cerev_img = pygame.image.load('cerev.png').convert_alpha()
cerev_button = button.Button(320, 200, cerev_img, .13)

montra_img = pygame.image.load('montra.png').convert_alpha()
montra_button = button.Button(420, 200, montra_img, .13)

prise_img = pygame.image.load('prise.png').convert_alpha()
prise_button = button.Button(520, 200, prise_img, .13)

check_img2 = pygame.image.load('check.png').convert_alpha()
check_button2 = button.Button(620, 202, check_img2, .05)

#create sugar button
sugar_img = pygame.image.load('add.png').convert_alpha()
sugar_button = button.Button(620, 400, sugar_img, .12)
sugarLevelInt = 0

#create sulfur dioxide button
sulfur_img = pygame.image.load('add.png').convert_alpha()
sulfur_button = button.Button(620, 300, sulfur_img, .12)
sulfurLevelInt = 0

#create citric acid button
citric_img = pygame.image.load('add.png').convert_alpha()
citric_button = button.Button(620, 500, citric_img, .12)
citricLevelInt = 0

#create ferment button
fermentBackground = pygame.image.load("ferment.jpg")
fermentBackground = pygame.transform.smoothscale(fermentBackground, (300, 150))
ferment_button = button.Button(754, 510, fermentBackground, 1)

#create temperature slider
temperatureSlider = Slider(screen, 470, 340, 20, 20, min=0, max=99, step=1)
temperatureText = TextBox(screen, 440, 450, 20, 20, fontSize=12)
temperatureText.disable()
temperatureSlider.vertical = True
temperatureSlider._height = 240

while True:

    #refresh temperature slider text
    temperature = temperatureSlider.getValue()
    temperatureText.setText(temperature)
    temperatureSlider.value = temperature

    #load background, barrel, and title
    screen.fill((165,42,42))
    screen.blit(background, (0, 0))
    pygame.draw.line(screen, '#CD7F32', (250, 360), (300, 390), 15)
    screen.blit(barrelImage, (30, 290))
    screen.blit(titleSurface, (72, 30))

    #if game is done
    if wineDone == True:
        pygame.draw.rect(screen, 'white', (0, 100, 300, 175))
        screen.blit(pygame.font.SysFont('timesnewroman', 50).render('TADA', True, 'black'), ((75, 150)))

    #load wine glass
    if gameDone == True:

        wineImage = pygame.image.load('wine.png')
        wineImage = pygame.transform.smoothscale(wineImage, (85, 85))
        wineImage = wineImage.subsurface(0, 85-wineLevel, 85, wineLevel)
        screen.blit(wineImage, (287, 510 - wineLevel))
        if wineLevel < 55:
            wineLevel += .7
            pygame.draw.line(screen, '#700a00', (300, 390), (300, 425), 5)
            pygame.draw.line(screen, '#CD7F32', (250, 360), (300, 390), 15)

        if wineLevel > 53:
            wineDone = True
            print('y')

        glassImage = pygame.image.load('glass.png')
        glassImage = pygame.transform.smoothscale(glassImage, (180, 220))
        screen.blit(glassImage, (240, 400))



    #load lines on card
    pygame.draw.line(screen, 'white', (750,0), (750,600), 5)
    pygame.draw.line(screen, 'white', (750,75), (1000,75), 5)
    pygame.draw.line(screen, 'white', (750,225), (1000,225), 5)
    pygame.draw.line(screen, 'white', (750,375), (1000,375), 5)

    #load and refresh stats
    grapeSurface = grapeType.render("Grape Type: " + grapeSelected, True, 'white')
    grapePhSurface = pygame.font.SysFont('timesnewroman', 15).render("PH Level:" + str(grapePh), True, 'white')
    grapeSugarSurface = pygame.font.SysFont('timesnewroman', 15).render("Sugar Index: " + str(grapeSugar), True, 'white')
    grapeAciditySurface = pygame.font.SysFont('timesnewroman', 15).render("Fixed Acidity: " + str(grapeAcidity), True, 'white')

    yeastSurface = yeastType.render("Yeast Type: " + yeastSelected, True, 'white')
    yeastTempSurface = pygame.font.SysFont('timesnewroman', 15).render("Ideal Temperature:" + str(yeastTemp), True, 'white')
    yeastAlcSurface = pygame.font.SysFont('timesnewroman', 15).render("Alcohol Tolerance:" + str(yeastAlc), True, 'white')
    yeastSpeedSurface = pygame.font.SysFont('timesnewroman', 15).render("Fermentation Speed:" + str(yeastSpeed), True, 'white')

    sugarSurface = sugarLevel.render("Sugar Level: " + str(sugarLevelInt), True, 'white')

    sulfurSurface = sulfurLevel.render("Sulfur Dioxide Level: " + str(sulfurLevelInt), True, 'white')

    citricSurface = citricLevel.render("Citric Acid Level: " + str(citricLevelInt), True, 'white')

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

    #create instructions
    instructionsSurface = pygame.font.SysFont('timesnewroman', 15).render("instructions", True, 'white')
    screen.blit(instructionsSurface, (30, 100))
    instructionsSurface = pygame.font.SysFont('timesnewroman', 15).render("instructions", True, 'white')
    screen.blit(instructionsSurface, (30, 115))

    #load grape buttons
    if grapeCheck == False or grapeSelected == "Merlot":
        if merlot_button.draw(screen):
            if grapeSelected != "Merlot" and grapeCheck == False:
                grapeSelected = 'Merlot'
                grapePh = 1
                grapeSugar = 1
                grapeAcidity = 1
            print(grapeSelected)

    if grapeCheck == False or grapeSelected == "Cabernet":
        if cabSau_button.draw(screen):
            if grapeSelected != "Cabernet" and grapeCheck == False:
                grapeSelected = 'Cabernet'
                grapePh = 2
                grapeSugar = 2
                grapeAcidity = 2
            print(grapeSelected)

    if grapeCheck == False or grapeSelected == "Pinot Noir":
        if pinot__button.draw(screen):
            if grapeSelected != "Pinot Noir" and grapeCheck == False:
                grapeSelected = 'Pinot Noir'
                grapePh = 3
                grapeSugar = 3
                grapeAcidity = 3
            print(grapeSelected)

    if check_button.draw(screen):
        if grapeSelected != '' and grapeCheck == False:
            grapeCheck = True
            #animate grape selection
            if grapeSelected == "Merlot":
                animatedGrape = 'merlot.png'
            if grapeSelected == "Cabernet":
                animatedGrape = 'cabSau.png'
            if grapeSelected == "Pinot Noir":
                animatedGrape = 'pinot.png'
            triggerGrapeAnimation = True
            print('yup')
            animatedGrapeImage = pygame.transform.smoothscale(pygame.image.load(animatedGrape), (40, 40))
    
    #animate grape
    if grapeAnimationY < 270 and triggerGrapeAnimation:
        screen.blit(animatedGrapeImage, (grapeAnimationX, grapeAnimationY))
        grapeAnimationY += 3

    #load yeast buttons
    if yeastCheck == False or yeastSelected == "S. Cerevisiae":
        if cerev_button.draw(screen):
            if yeastSelected != "S. Cerevisiae" and yeastCheck == False:
                yeastSelected = 'S. Cerevisiae'
                yeastTemp = 1
                yeastAlc = 1
                yeastSpeed = 1
            print(yeastSelected)

    if yeastCheck == False or yeastSelected == "Montrachet":
        if montra_button.draw(screen):
            if yeastSelected != "Montrachet" and yeastCheck == False:
                yeastSelected = 'Montrachet'
                yeastTemp = 2
                yeastAlc = 2
                yeastSpeed = 2
            print(yeastSelected)

    if yeastCheck == False or yeastSelected == "Prise de Mousse":
        if prise_button.draw(screen):
            if yeastSelected != "Prise de Mousse" and yeastCheck == False:
                yeastSelected = 'Prise de Mousse'
                yeastTemp = 3
                yeastAlc = 3
                yeastSpeed = 3
            print(yeastSelected)

    if check_button2.draw(screen):
        if yeastSelected != '':
            yeastCheck = True
            #animate yeast selection
            if yeastSelected == "S. Cerevisiae":
                animatedYeast = 'cerev.png'
            if yeastSelected == "Montrachet":
                animatedYeast = 'montra.png'
            if yeastSelected == "Prise de Mousse":
                animatedYeast = 'prise.png'
            triggerYeastAnimation = True
            print('yup')
            animatedYeastImage = pygame.transform.smoothscale(pygame.image.load(animatedYeast), (50, 50))
    
    #animate yeast
    if yeastAnimationY < 270 and triggerYeastAnimation:
        screen.blit(animatedYeastImage, (yeastAnimationX, yeastAnimationY))
        yeastAnimationY += 3

    #load sugar button
    if sugar_button.draw(screen):
        sugarLevelInt += 1
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render("Add Sugar", True, 'white'), (515, 418))

    #load sulfur button
    if sulfur_button.draw(screen):
        sulfurLevelInt += 1
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render("Add Sulfur", True, 'white'), (515, 310))
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render("Dioxide", True, 'white'), (527, 332))

    #load citric button
    if citric_button.draw(screen):
        citricLevelInt += 1
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render("Add Citric", True, 'white'), (515, 510))
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render("Acid", True, 'white'), (540, 532))

    #load ferment button
    if ferment_button.draw(screen):
        if isFermenting == False:
            print('buh')
            isFermenting = True
        else:
            isFermenting = False
            finalTime = pygame.time.get_ticks() - firstTime
            print(finalTime)
            gameDone = True

    if isFermenting:
        if hasTime == False:
            firstTime = pygame.time.get_ticks()
            hasTime = True
        time = int((pygame.time.get_ticks() - firstTime) / 1000)

    if isFermenting == False:
        screen.blit(pygame.font.SysFont('oldenglishtext', 50).render("Ferment", True, '#DAA520'), (786, 527))
    else:
        screen.blit(pygame.font.SysFont('oldenglishtext', 50).render("Stop(" + str(time) + 's)', True, '#DAA520'), (786, 527))

    #load temperature label
    screen.blit(pygame.font.SysFont('timesnewroman', 20).render("Temperature", True, 'white'), (425, 275))

    #check quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #update elements
    pygame_widgets.update(pygame.event.get())
    pygame.display.update()
    clock.tick(60)
