import pygame,sys
import time
import random

#initializing the game
pygame.init()


#set the colors and dimensions for the window
white = (255,255,255)
black = (100,0,0)
red = (255,0,0)
green = (0, 255, 0)
yellow=(255, 165, 0)

window_width = 800
window_height = 650

#display the screen
gameDisplay = pygame.display.set_mode((window_width,window_height))

#name the screen
pygame.display.set_caption('slither snake game')

#clock helps to keep track of events based on timing
clock = pygame.time.Clock()


score_font = pygame.font.SysFont("bahnschrift", 25)

#(Frames Per Second) screen gets refreshed 5 times persecond
FPS = 8
blockSize = 20
noPixel = 0

def myquit():

    pygame.quit()
    sys.exit(0)

	

font = pygame.font.SysFont(None, 25, bold=True)
def Your_score(score):
    value = score_font.render("Your Score is: " + str(score), True, black)
    gameDisplay.blit(value, [0, 0])

def drawGrid():
	sizeGrd = window_width // blockSize

#draw the snake in rectangular shape
def snake(blockSize, snakelist):
    for size in snakelist:

        pygame.draw.rect(gameDisplay, black,[size[0]+5,size[1],blockSize,blockSize],2)


#display message on screen
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)

    #displays the message at the centre of screen
    gameDisplay.blit(screen_text, [window_width/6, window_height/3])

    

def gameLoop():
    gameExit = False
    gameOver = False


    lead_x = window_width/2
    lead_y = window_height/2



    change_pixels_of_x = 0
    change_pixels_of_y = 0



    snakelist = []
    snakeLength = 1


    #fruits are randomly set for the snake to eat along x and y axis
    randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
    randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0

    
    #Until the game is exit the loop keeps running
    while not gameExit:
        
        #gives another chance to play the game
        while gameOver == True:
            
            gameDisplay.fill(green)
            message_to_screen("Game over! Press C-play Again or Q-quit", red)
            Your_score(snakeLength- 1)
            pygame.display.update()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True


                if event.type == pygame.KEYDOWN:
                    #when q is pressed exit the game
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    #when c is pressed game starts again  

                    if event.key == pygame.K_c:
                        gameLoop()

            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    myquit()

                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN

                

                if leftArrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel

                elif rightArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel

                elif upArrow:
                    change_pixels_of_y = -blockSize
                    change_pixels_of_x = noPixel

                elif downArrow:
                    change_pixels_of_y = blockSize
                    change_pixels_of_x = noPixel

            #check boundaries ,if the snake hits borders of the window then gameover


            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                gameOver = True

                   

        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y

        

        gameDisplay.fill(yellow)

        AppleThickness = 20

        #apples are created with some thickness and randomly placed on screen


        #print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])
        print("snake is moving")
        pygame.draw.rect(gameDisplay, red, [randomAppleX,randomAppleY,AppleThickness,AppleThickness])



        allspriteslist = []
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)



        if len(snakelist) > snakeLength:
            del snakelist[0]

            

        for eachSegment in snakelist [:-1]:
            if eachSegment == allspriteslist:
                gameOver = True

                

        snake(blockSize, snakelist)
        Your_score(snakeLength - 1)

        pygame.display.update()

        

        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:

                randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
                randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0
                snakeLength += 1



             

        clock.tick(FPS)
    pygame.quit()

    quit()
gameLoop()
