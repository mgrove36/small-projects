import pygame, time

finished = False

def updateDisplay():
    if finished:
        gameDisplay.blit(buttonReset, buttonResetRect)
    else:
        # Set the background colour
        gameDisplay.fill(black)

        if sortingAlgorithm != 0:
            for loop in range(0,len(numberList)):
                # Place other objects to display below
                pygame.draw.rect(gameDisplay, colourList[numberList[loop]-1], [loop*20, 90, 20, 20])  # rect in [] list   x,y,w,h  0,0 is top left
            # display current time taken
            timeText = font.render("{:.1f} seconds".format(time.time() - startTime), True, white)
            timeTextRect = timeText.get_rect()
            timeTextRect.top = 10
            timeTextRect.left = 10
            gameDisplay.blit(timeText, timeTextRect)
        else:
            gameDisplay.blit(buttonSelective, buttonSelectiveRect)
            gameDisplay.blit(buttonInsertion, buttonInsertionRect)
            gameDisplay.blit(buttonBubble, buttonBubbleRect)

    # redisplay window
    pygame.display.update()
    clock.tick(fps)

def checkQuit():
    for event in pygame.event.get():
        # allow safe exit
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # allow keyboard interrupt (with escape key)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

def checkStartButtons():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # checks if mouse position is over any start buttons
            if buttonSelectiveRect.collidepoint(event.pos):
                # prints current location of mouse
                print('Selective button was pressed at {0}'.format(event.pos))
                return 1
            elif buttonInsertionRect.collidepoint(event.pos):
                # prints current location of mouse
                print('Insertion button was pressed at {0}'.format(event.pos))
                return 2
            elif buttonBubbleRect.collidepoint(event.pos):
                # prints current location of mouse
                print('Bubble button was pressed at {0}'.format(event.pos))
                return 3

def checkResetButton():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # checks if mouse position is over the reset button
            if buttonResetRect.collidepoint(event.pos):
                # prints current location of mouse
                print('Reset button was pressed at {0}'.format(event.pos))
                return False
    return True

def resetGame():
    numberList = originalNumberList

# initialise PyGame
pygame.init()

font = pygame.font.Font("Roboto-Regular.ttf", 32)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# define clock, to allow framerate alteration
clock = pygame.time.Clock()

# list of colours, in colour order
colourList = [(239, 69, 69), (239, 86, 69), (239, 103, 69), (239, 120, 69), (239, 137, 69), (239, 154, 69), (239, 171, 69), (239, 188, 69), (239, 205, 69), (239, 222, 69), (239, 239, 69), (222, 239, 69), (205, 239, 69), (188, 239, 69), (171, 239, 69), (154, 239, 69), (137, 239, 69), (120, 239, 69), (103, 239, 69), (86, 239, 69), (69, 239, 69), (69, 239, 86), (69, 239, 103), (69, 239, 120), (69, 239, 137), (69, 239, 154), (69, 239, 171), (69, 239, 188), (69, 239, 205), (69, 239, 222), (69, 239, 239), (69, 222, 239), (69, 205, 239), (69, 188, 239), (69, 171, 239), (69, 154, 239), (69, 137, 239), (69, 120, 239), (69, 103, 239), (69, 86, 239), (69, 69, 239), (86, 69, 239), (103, 69, 239), (120, 69, 239), (137, 69, 239), (154, 69, 239), (171, 69, 239), (188, 69, 239), (205, 69, 239), (222, 69, 239), (239, 69, 239), (239, 69, 222), (239, 69, 205), (239, 69, 188), (239, 69, 171), (239, 69, 154), (239, 69, 137), (239, 69, 120), (239, 69, 103), (239, 69, 86)]
# list of numbers to be sorted
originalNumberList = [30,4,5,6,36,38,37,32,17,19,8,10,56,50,20,13,14,40,58,21,43,51,1,31,41,16,60,22,34,28,9,12,42,2,27,18,26,47,39,24,57,23,46,53,15,25,7,33,49,59,35,44,45,11,54,29,55,52,3,48]
numberList = originalNumberList.copy()

# frame rate of sorting visualisation
fps = 25

sortingAlgorithm = 0


# define height and width of display
display_width = len(numberList)*20
display_height = 200

# define surface
gameDisplay = pygame.display.set_mode((display_width,display_height))

# set window title
pygame.display.set_caption("Sorting Algorithms")

# define buttons for choosing sorting algorithm
# selective sort button
buttonSelective = font.render("Selective", True, white)
buttonSelectiveRect = buttonSelective.get_rect()
buttonSelectiveRect.center = (display_width / 2 - 200, display_height / 2)
# insertion sort button
buttonInsertion = font.render("Insertion", True, white)
buttonInsertionRect = buttonInsertion.get_rect()
buttonInsertionRect.center = (display_width / 2, display_height / 2)
# bubble sort button
buttonBubble = font.render("Bubble", True, white)
buttonBubbleRect = buttonBubble.get_rect()
buttonBubbleRect.center = (display_width / 2 + 200, display_height / 2)

# define button for resetting the program
buttonReset = font.render("Reset", True, white)
buttonResetRect = buttonBubble.get_rect()
buttonResetRect.center = (display_width / 2, display_height / 2 + 60)

updateDisplay()

while True:
    if sortingAlgorithm == 1:
        startTime = time.time()
        # selection sort
        swapPosition = 0
        swapData = 0
        for i in range(0, len(numberList)):
            swapPosition = i
            for j in range(i, len(numberList)):
                # find the smallest number
                if numberList[j] < numberList[swapPosition]:
                    swapPosition = j

            swapData = numberList[i]
            numberList[i] = numberList[swapPosition]
            numberList[swapPosition] = swapData            

            checkQuit()
            updateDisplay()
        finished = True
        sortingAlgorithm = 0
    elif sortingAlgorithm == 2:
        startTime = time.time()
        # insertion sort
        for i in range(0, len(numberList)):
            j = 0
            while numberList[i] > numberList[j]:
                j += 1
            numberList.insert(j, numberList.pop(i))
            checkQuit()
            updateDisplay()
        finished = True
        sortingAlgorithm = 0
    elif sortingAlgorithm == 3:
        startTime = time.time()
        swapped = True
        while swapped:
            swapped = False
            for index, item in enumerate(numberList):
                swappedInternal = False
                if index != len(numberList) - 1 and item > numberList[index + 1]:
                    numberList[index] = numberList[index + 1]
                    numberList[index + 1] = item
                    swapped = True
                    swappedInternal = True
                checkQuit()
                if swappedInternal:
                    updateDisplay()
        finished = True
        sortingAlgorithm = 0
    elif finished:
        updateDisplay()
        finished = checkResetButton()
        if not finished:
            numberList = originalNumberList.copy()
            updateDisplay()
        checkQuit()
    else:
        checkQuit()
        sortingAlgorithm = checkStartButtons()