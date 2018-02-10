import pygame
from pygame.locals import * 
from random import randint
from classes import *
from time import sleep

if __name__ == "__main__" or __name__ == "pacman" :

    GAME = Maze()
    HERO = Pacman()
    VILLIAN = Ghost(9,4)
    VILLIAN2 = Ghost(4,10)
    VILLIAN3 = Ghost(14,10)
    VILLIAN4 = Ghost(9,16)
    pygame.init()
    GAME.scorefont = pygame.font.Font(None,30)
    done = False
    clock = pygame.time.Clock()

    while done == False:
    	for event in pygame.event.get():
            if event.type == pygame.QUIT:
    	        done = True
    	    if event.type == KEYDOWN:
		if event.key == K_q:
	            done = True

	HERO.pacPosition(GAME)        
	GAME.screen.fill(GAME.BLACK)
	sleep(.1)
	VILLIAN.ghostPosition(GAME)
	VILLIAN2.ghostPosition(GAME)        
	VILLIAN3.ghostPosition(GAME)
	VILLIAN4.ghostPosition(GAME)
	move = randint(0,3)
        GAME.countfinal=0
        GAME.dispmaze()
        GAME.drawwalls() 
        HERO.pos(GAME)
        VILLIAN.pos(GAME)
        VILLIAN2.pos(GAME) 
        VILLIAN3.pos(GAME)
        VILLIAN4.pos(GAME)

        if HERO.checkGhost(VILLIAN) or HERO.checkGhost(VILLIAN2) or HERO.checkGhost(VILLIAN3) or HERO.checkGhost(VILLIAN4):
            done = True 
   	    print "Final Score = "+(str)(GAME.score)
        elif GAME.countfinal == 1200:
	    GAME.reset()
            HERO.resetpacman()
            VILLIAN.resetghost()
            VILLIAN2.resetghost()
            VILLIAN3.resetghost()
            VILLIAN4.resetghost()
            GAME.level += 1
	
	GAME.scoredisp()
	GAME.leveldisp()        
	clock.tick(10)
        pygame.display.flip()
    
    pygame.quit()
