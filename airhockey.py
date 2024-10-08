from turtledemo.nim import SCREENWIDTH, SCREENHEIGHT

import pygame
import self
from pygame import mixer

#Initialize the game
pygame.init()

#create screen
SCREENWIDTH = 900
SCREENHEIGHT = int(SCREENWIDTH * 0.8)
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

#sources: ice.jpg, HandelGothic Regular.ttf. puck.png

#Title
pygame.display.set_caption("Air Pong Hockey")

#STATE
state = 0

#Text
font = pygame.font.Font('HandelGothic Regular.ttf', 32)
fontSmaller = pygame.font.Font('HandelGothic Regular.ttf', 24)

#Sounds
clicked_sound = mixer.Sound('mouse-click-sound-233951.mp3')
applause_sound = mixer.Sound('short-crowd-cheer-236776.mp3')
boo_sound = mixer.Sound('aww-8277.mp3')
clack_sound = mixer.Sound('clack-85854.mp3')

#Scores
p1_score = 0
p2_score = 0
win_score = 10

#Buttons
one_player_game = pygame.Rect((0, 150, SCREENWIDTH, 50))
button1txt = font.render("1 PLAYER GAME" ,True,(0,0,0))

two_player_game = pygame.Rect((0, 250, SCREENWIDTH, 50))
button2txt = font.render("2 PLAYER GAME" ,True,(0,0,0))

help_button = pygame.Rect((0, 350, SCREENWIDTH, 50))
helptxt = font.render("HOW TO PLAY" ,True,(0,0,0))
helpInfo1 = fontSmaller.render("- Move your character around so that they hit the puck",True,(0,0,0))
helpInfo2 = fontSmaller.render("- Player 1 uses WASD to move and Player 2 uses the arrow keys.",True,(0,0,0))
helpInfo3 = fontSmaller.render( "- The more the puck is hit, the faster it moves." ,True,(0,0,0))
helpInfo4 = fontSmaller.render( "- Get the puck into the opponents goal to score a point." ,True,(0,0,0))

options = pygame.Rect((0, 450, SCREENWIDTH, 50))
optionstxt = font.render("OPTIONS" ,True,(0,0,0))
optInfo1 = fontSmaller.render("Powerups: ",True,(0,0,0))
optInfo2 = fontSmaller.render("Number of points to win: ",True,(0,0,0))
optInfo3 = fontSmaller.render(str(win_score),True,(0,0,0))
less = pygame.Rect((355, 350, 30, 30))
lesstxt = fontSmaller.render("-",True,(0,0,0))
more = pygame.Rect((450, 350, 30, 30))
moretxt = fontSmaller.render("+",True,(0,0,0))
switchImg = pygame.image.load('switch.png')
switchImg = pygame.transform.scale(switchImg,(50,50))


credits = pygame.Rect((0, 550, SCREENWIDTH, 50))
credtxt = font.render("CREDITS" ,True,(0,0,0))
credInfo1 = fontSmaller.render("Created By: Me",True,(0,0,0))
credInfo2 = fontSmaller.render("Artwork By: Me & various sources",True,(0,0,0))
credInfo3 = fontSmaller.render("Programming By: Me",True,(0,0,0))
credInfo4 = fontSmaller.render("Music & Sounds By: Pixaby.com &",True,(0,0,0))
credInfo5 = fontSmaller.render("Project Created: October 7th, 2024",True,(0,0,0))


back = pygame.Rect((0, SCREENHEIGHT - 100, SCREENWIDTH, 50))
backtxt = font.render("BACK" ,True,(0,0,0))

quit_button = pygame.Rect((SCREENWIDTH - 110, SCREENHEIGHT - 75, 100, 50))
quittxt = font.render("QUIT" ,True,(0,0,0))

#Players
player1 = pygame.Rect((75, 350, 30, 100))
player2 = pygame.Rect((725, 350, 30, 100))

p2_is_human = True

#Puck
puck_size = 50
puckImg = pygame.image.load('puck.png')
puckImg = pygame.transform.scale(puckImg,(puck_size,puck_size)) #resize puck
puckXSpeed = -0.1
puckYSpeed = -0.05
puckX = SCREENWIDTH / 2 - puck_size/2
puckY = SCREENHEIGHT / 2 - puck_size/2
def place_puck(x,y):
    screen.blit(puckImg, (puckX,puckY))



def show_score1(x,y):
    p1score_text = font.render("P1: " + str(p1_score),True,(200,0,0))
    screen.blit(p1score_text, (x,y))

def show_score2(x,y):
    p2score_text = font.render("P2: " + str(p2_score), True, (0, 0, 200))
    screen.blit(p2score_text, (x, y))

#Goal
p1goal = pygame.Rect((0, 0, 30, SCREENHEIGHT))
p2goal = pygame.Rect((SCREENWIDTH-30, 0, 30, SCREENHEIGHT))



#Surface
surface_image = pygame.image.load('ice.jpg').convert()
surface_image = pygame.transform.scale(surface_image, (SCREENWIDTH, SCREENHEIGHT))
seperation = pygame.Rect((SCREENWIDTH/2 -5, 0, 10, SCREENHEIGHT))


                               #### RUNNING CODE STARTS HERE ####

run = True
while run:

    mouse_pos = pygame.mouse.get_pos()

    if state == 0: #main menu
        screen.fill((0, 0, 255))  # screen resets each time
        pygame.draw.rect(screen, (255, 0, 0), one_player_game)
        screen.blit(button1txt, (15, 160))
        pygame.draw.rect(screen, (0, 255, 255), two_player_game)
        screen.blit(button2txt, (15, 260))
        pygame.draw.rect(screen, (0, 255, 0), help_button)
        screen.blit(helptxt, (15, 360))
        pygame.draw.rect(screen, (255, 255, 0), options)
        screen.blit(optionstxt, (15, 460))
        pygame.draw.rect(screen, (128, 0, 255), credits)
        screen.blit(credtxt, (15, 560))

        puckXSpeed = -0.1
        puckYSpeed = -0.05
        puckX = SCREENWIDTH / 2 - 50
        puckY = SCREENHEIGHT / 2 - 50
        p1_score = 0
        p2_score = 0

        if one_player_game.collidepoint(mouse_pos):
            #one_player_game.Color(100,0,0)
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 1
                p2_is_human = False

        if two_player_game.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 1
                p2_is_human = True

        if help_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 2

        if options.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 3

        if credits.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 4

    elif state == 1: #The game
        #Load the players, goal and puck
        screen.blit(surface_image, (0, 0))
        pygame.draw.rect(screen, (255, 0, 0), player1)
        pygame.draw.rect(screen, (0, 0, 0), p1goal)
        pygame.draw.rect(screen, (0, 0, 255), player2)
        pygame.draw.rect(screen, (0, 0, 0), p2goal)
        pygame.draw.rect(screen, (0, 0, 0), seperation)
        show_score1(SCREENWIDTH/2 - 150,10)
        show_score2(SCREENWIDTH/2 + 60, 10)
        pygame.draw.rect(screen, (70, 0, 70), quit_button)
        screen.blit(quittxt, (SCREENWIDTH - 95, SCREENHEIGHT - 70))
        place_puck(puckX,puckY)

        #Puck Movement
        puckX += puckXSpeed
        puckY += puckYSpeed

        #puck hits player 1, it changes direction and goes faster
        if (((player1.x - puckX < 25) & (player1.x - puckX > -25)) &
                ((player1.y - puckY < puck_size) & (player1.y - puckY > -puck_size))):
            clack_sound.play()
            puckXSpeed *= -1.5

        if (((player2.x - puckX < puck_size) & (player2.x - puckX > -puck_size)) &
                ((player2.y - puckY < puck_size) & (player2.y - puckY > -puck_size))):
            clack_sound.play()
            puckXSpeed *= -1.5

        if (puckY < 0) | (puckY > SCREENHEIGHT - puck_size):
            clack_sound.play()
            puckYSpeed *= -1.5


        #if player 2 scores on player 1
        if (puckX - p1goal.x < 10) | (p1goal.x - puckX > -10):
            boo_sound.play()
            puckX = SCREENWIDTH/ 2 - puck_size/2
            puckY = SCREENHEIGHT/ 2 - puck_size/2
            p2_score += 1
            puckXSpeed = -0.1
            puckYSpeed = -0.05

        #if player 1 scores on player 2
        if (puckX - p2goal.x > -10) | (p2goal.x - puckX < 10):
            applause_sound.play()
            puckX = SCREENWIDTH/ 2 - puck_size/2
            puckY = SCREENHEIGHT/ 2 - puck_size/2
            p1_score += 1
            puckXSpeed = 0.1
            puckYSpeed = 0.05

        #Set a max speed for the puck so it doesnt move too fast
        if puckXSpeed > 1:
            puckXSpeed = 1
        elif puckXSpeed < -1:
            puckXSpeed = -1

        if puckYSpeed > 1:
            puckYSpeed = 1
        elif puckYSpeed < -1:
            puckYSpeed = -1

        key = pygame.key.get_pressed()

        #Player 1 controls
        if key[pygame.K_a]:
            player1.move_ip(-1,0)
        elif key[pygame.K_d]:
            player1.move_ip(1, 0)
        elif key[pygame.K_w]:
            player1.move_ip(0, -1)
        elif key[pygame.K_s]:
            player1.move_ip(0, 1)

        if player1.x > SCREENWIDTH/2 - 60:
            player1.x = SCREENWIDTH/2 - 60
        elif player1.x < 30:
            player1.x = 30

        if player1.y > SCREENHEIGHT - 100:
            player1.y = SCREENHEIGHT - 100
        elif player1.y < 0:
            player1.y = 0


        #Player 2 controls (if human)

        if p2_is_human:
            if key[pygame.K_LEFT]:
                player2.move_ip(-1, 0)
            elif key[pygame.K_RIGHT]:
                player2.move_ip(1, 0)
            elif key[pygame.K_UP]:
                player2.move_ip(0, -1)
            elif key[pygame.K_DOWN]:
                player2.move_ip(0, 1)

            if player2.x > SCREENWIDTH - 60:
                player2.x = SCREENWIDTH - 60
            elif player2.x < SCREENWIDTH/2 + 30:
                player2.x = SCREENWIDTH/2 + 30

            if player2.y > SCREENHEIGHT - 100:
                player2.y = SCREENHEIGHT - 100
            elif player2.y < 0:
                player2.y = 0
        else:
            player2.y = puckY

        #Return to menu if quit button is pressed
        if quit_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 0

    elif state == 2: #how to play
        screen.fill((70, 150, 0))
        pygame.draw.rect(screen, (255, 255, 255), back)
        screen.blit(backtxt, (15, SCREENHEIGHT - 95))
        screen.blit(helpInfo1, (15, 100))
        screen.blit(helpInfo2, (15, 150))
        screen.blit(helpInfo3, (15, 200))
        screen.blit(helpInfo4, (15, 250))


        if back.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 0

    elif state == 3: #options
        screen.fill((70, 70, 70))
        pygame.draw.rect(screen, (255, 255, 255), back)
        screen.blit(backtxt, (15, SCREENHEIGHT - 95))
        screen.blit(optInfo1, (15, 100))
        screen.blit(optInfo2, (15, 350))
        screen.blit(optInfo3, (400, 350))
        pygame.draw.rect(screen, (255, 255, 255), less)
        screen.blit(lesstxt, (367, 350))
        pygame.draw.rect(screen, (255, 255, 255), more)
        screen.blit(moretxt, (457, 350))


        if back.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 0

    elif state == 4: #credits
        screen.fill((150, 70, 0))
        pygame.draw.rect(screen, (255, 255, 255), back)
        screen.blit(backtxt, (15, SCREENHEIGHT - 95))
        screen.blit(credInfo1, (15, 100))
        screen.blit(credInfo2, (15, 150))
        screen.blit(credInfo3, (15, 200))
        screen.blit(credInfo4, (15, 250))
        screen.blit(credInfo5, (15, 300))
        if back.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
