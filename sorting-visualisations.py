import pygame, time

finished = False

# define function for updating the display contents
def updateDisplay():
    # show the reset button if the sorting has completed
    if finished:
        gameDisplay.blit(buttonReset, buttonResetRect)
    # if the sorting hasn't completed
    else:
        # wipe the screen
        gameDisplay.fill(black)

        # if the sorting algorithm to be used has been been defined as 1, 2 or 3
        if sortingAlgorithm != 0:
            # draw one rect object for each item in the list
            for loop in range(0,len(numberList)):
                pygame.draw.rect(gameDisplay, colourList[numberList[loop]-1], [loop*20, 90, 20, 20])
            # display current time taken in top left
            timeText = font.render("{:.1f} seconds".format(time.time() - startTime), True, white)
            timeTextRect = timeText.get_rect()
            timeTextRect.top = 10
            timeTextRect.left = 10
            gameDisplay.blit(timeText, timeTextRect)
        # if the sorting algorithm hasn't yet been chosen, show the buttons for doing so
        else:
            gameDisplay.blit(buttonSelective, buttonSelectiveRect)
            gameDisplay.blit(buttonInsertion, buttonInsertionRect)
            gameDisplay.blit(buttonBubble, buttonBubbleRect)

    # redisplay window
    pygame.display.update()
    
    # adjust for desired framerate
    clock.tick(fps)

# define function for checking whether the user wants to exit the program
def checkQuit():
    for event in pygame.event.get():
        # allow exit using window exit button (the red cross)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # allow keyboard interrupt (with escape key)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

# define function for checking if any start buttons have been pressed
def checkStartButtons():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # checks if mouse position is over selective sort button
            if buttonSelectiveRect.collidepoint(event.pos):
                # prints current location of mouse
                print('Selective button was pressed at {0}'.format(event.pos))
                return 1
            # checks if mouse position is over insertion sort button
            elif buttonInsertionRect.collidepoint(event.pos):
                # prints current location of mouse
                print('Insertion button was pressed at {0}'.format(event.pos))
                return 2
            # checks if mouse position is over bubble sort button
            elif buttonBubbleRect.collidepoint(event.pos):
                # prints current location of mouse
                print('Bubble button was pressed at {0}'.format(event.pos))
                return 3

# define function for checking if the reset button has been pressed
def checkResetButton():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # checks if mouse position is over the reset button
            if buttonResetRect.collidepoint(event.pos):
                # prints current location of mouse
                print('Reset button was pressed at {0}'.format(event.pos))
                # returns value for use in the variable finished
                return False
    # returns value for use in the variable finished
    return True

# initialise PyGame
pygame.init()

# define font for usage with text
font = pygame.font.Font("Roboto-Regular.ttf", 32)
# define some basic colours, for easier referencing later on
black = (0, 0, 0)
white = (255, 255, 255)

# define clock, to allow framerate alteration
clock = pygame.time.Clock()

# list of colours, in colour order
colourList = [(239, 69, 69), (239, 86, 69), (239, 103, 69), (239, 120, 69), (239, 137, 69), (239, 154, 69), (239, 171, 69), (239, 188, 69), (239, 205, 69), (239, 222, 69), (239, 239, 69), (222, 239, 69), (205, 239, 69), (188, 239, 69), (171, 239, 69), (154, 239, 69), (137, 239, 69), (120, 239, 69), (103, 239, 69), (86, 239, 69), (69, 239, 69), (69, 239, 86), (69, 239, 103), (69, 239, 120), (69, 239, 137), (69, 239, 154), (69, 239, 171), (69, 239, 188), (69, 239, 205), (69, 239, 222), (69, 239, 239), (69, 222, 239), (69, 205, 239), (69, 188, 239), (69, 171, 239), (69, 154, 239), (69, 137, 239), (69, 120, 239), (69, 103, 239), (69, 86, 239), (69, 69, 239), (86, 69, 239), (103, 69, 239), (120, 69, 239), (137, 69, 239), (154, 69, 239), (171, 69, 239), (188, 69, 239), (205, 69, 239), (222, 69, 239), (239, 69, 239), (239, 69, 222), (239, 69, 205), (239, 69, 188), (239, 69, 171), (239, 69, 154), (239, 69, 137), (239, 69, 120), (239, 69, 103), (239, 69, 86)]
# list of numbers to be sorted
# two lists are used so that the original one is retained whilst the other is altered, allowing resetting at the end of the program
originalNumberList = [30,4,5,6,36,38,37,32,17,19,8,10,56,50,20,13,14,40,58,21,43,51,1,31,41,16,60,22,34,28,9,12,42,2,27,18,26,47,39,24,57,23,46,53,15,25,7,33,49,59,35,44,45,11,54,29,55,52,3,48]
numberList = originalNumberList.copy()

# frame rate of sorting visualisation
fps = 25

# define which sorting algorithm to use (1, 2 and 3 are the only valid options, for selective, insertion and bubble, respectively)
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

# update display contents
updateDisplay()

# run until manual exit
while True:
    # selection sort
    if sortingAlgorithm == 1:
        # set start time, for use with on-screen timer
        startTime = time.time()
        swapPosition = 0
        swapData = 0
        # find the smallest number in the list until it is fully sorted
        for i in range(0, len(numberList)):
            swapPosition = i
            for j in range(i, len(numberList)):
                # find the smallest number
                if numberList[j] < numberList[swapPosition]:
                    swapPosition = j
            # swap the smallest number with the number in its new position
            swapData = numberList[i]
            numberList[i] = numberList[swapPosition]
            numberList[swapPosition] = swapData            

            # check if the user wants to quit
            checkQuit()
            # update display contents
            updateDisplay()
        # record that the sorting has completed
        finished = True
        sortingAlgorithm = 0
    # insertion sort
    elif sortingAlgorithm == 2:
        # set start time, for use with on-screen timer
        startTime = time.time()
        # for each item in the list
        for i in range(0, len(numberList)):
            j = 0
            # find its correct position
            while numberList[i] > numberList[j]:
                j += 1
            # put it in its correct position in the list
            numberList.insert(j, numberList.pop(i))
            # check if the user wants to quit
            checkQuit()
            # update display contents
            updateDisplay()
        # record that the sorting has completed
        finished = True
        sortingAlgorithm = 0
    elif sortingAlgorithm == 3:
        # set start time, for use with on-screen timer
        startTime = time.time()
        swapped = True
        while swapped:
            swapped = False
            # for each item in the list
            for index, item in enumerate(numberList):
                swappedInternal = False
                # if the numbers are in the wrong position, swap them around
                if index != len(numberList) - 1 and item > numberList[index + 1]:
                    numberList[index] = numberList[index + 1]
                    numberList[index + 1] = item
                    swapped = True
                    swappedInternal = True
                # check if the user wants to quit
                checkQuit()
                # if items have been swapped, update display contents
                if swappedInternal:
                    updateDisplay()
        # record that the sorting has completed
        finished = True
        sortingAlgorithm = 0
    # if sorting has completed
    elif finished:
        # update display contents
        updateDisplay()
        # check if the reset button has been pressed
        finished = checkResetButton()
        # ensure reset button and exiting are both enabled
        clock.tick(fps)
        # check if the user wants to quit
        checkQuit()
        # ensure reset button and exiting are both enabled
        clock.tick(fps)
        # if reset button has been pressed, reset the list
        if not finished:
            numberList = originalNumberList.copy()
            # update display contents
            updateDisplay()
    else:
        #check if the user wants to quit
        checkQuit()
        # check if any of the start buttons have been pressed
        sortingAlgorithm = checkStartButtons()