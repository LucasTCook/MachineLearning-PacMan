import pygame
from pygame.locals import * 
from random import randint

class Maze():
    def __init__(self):
	self.BLACK = (0,0,0)
	self.GOLD = (246,253,49)
	self.GREY = (50,50,50)
	self.RED = (255,0,0)
	self.BLUE = (20,27,229)
	self.WHITE = (255,255,255)	
	self.GREEN = (0,255,0)
	self.width  = 20
	self.height = 20
	self.margin = 1	
	self.score = 0
	self.level = 1	
	self.grid = []
	self.walls = []
	self.countfinal = 0
	self.make()
	self.size = [400, 600]
	self.screen = pygame.display.set_mode(self.size)

    def make(self):
        
	for row in range(22):
            self.grid.append([])
            for column in range(19):
                self.grid[row].append(0)

        for i in range(0,4):
            for j in range(8,14):
                self.grid[j][i] = 1

        for i in range(15,19):
            for j in range(8,14):
                self.grid[j][i] = 1

	#top wall
        for i in range(0,19):
            for j in range(0,1):
                self.walls.append([i,j])
    
        #right wall
        for i in range(18,19):
            for j in range(0,7):
                self.walls.append([i,j])
        for i in range(15,19):
            for j in range(7,8):
                self.walls.append([i,j])
        for i in range(15,16):
            for j in range(7,9):
                self.walls.append([i,j])
        for i in range(15,19):
            for j in range(9,10):
                self.walls.append([i,j])
        for i in range(18,19):
            for j in range(13,22):
                self.walls.append([i,j])
        for i in range(15,19):
            for j in range(13,14):
                self.walls.append([i,j])
        for i in range(15,16):
            for j in range(11,13):
                self.walls.append([i,j])
        for i in range(15,19):
            for j in range(11,12):
                self.walls.append([i,j])

        #bottom wall
        for i in range(0,18):
            for j in range(21,22):
                self.walls.append([i,j])

        #left wall
        for i in range(0,1):
            for j in range(0,7):
                self.walls.append([i,j])
        for i in range(0,4):
            for j in range(7,8):
                self.walls.append([i,j])
        for i in range(3,4):
            for j in range(7,10):
                self.walls.append([i,j])
        for i in range(0,4):
            for j in range(9,10):
                self.walls.append([i,j])
        for i in range(0,4):
            for j in range(13,14):
                self.walls.append([i,j])
        for i in range(3,4):
            for j in range(11,13):
                self.walls.append([i,j])
        for i in range(0,4):
            for j in range(11,12):
                self.walls.append([i,j])
        for i in range(0,1):
            for j in range(13,22):
                self.walls.append([i,j])
	
	#middle wall
	for i in range(7,8):
            for j in range(9,12):
                self.walls.append([i,j])
        for i in range(11,12):
            for j in range(9,12):
                self.walls.append([i,j])
	for i in range(7,9):
            for j in range(9,10):
                self.walls.append([i,j])
        for i in range(10,11):
            for j in range(9,10):
                self.walls.append([i,j])
	for i in range(7,11):
            for j in range(11,12):
                self.walls.append([i,j])

	for wall in self.walls:
    	    self.grid[wall[1]][wall[0]] = 1

        return self
            
    def reset(self):
        self.grid = []
        self.walls = []
        self.countfinal = 0
        self.make()
        return self

    def scoredisp(self):
        scoretext=self.scorefont.render("Score: "+(str)(self.score), 1,self.WHITE)
        self.screen.blit(scoretext, (30, 560))

    def leveldisp(self):
        leveltext=self.scorefont.render("Level: "+(str)(self.level), 1,self.RED)
        self.screen.blit(leveltext, (30, 530))

    def dispmaze(self):
        olor = self.GREY
        for row in range(22):
            for column in range(19):
                color = self.GREY
		pygame.draw.rect(self.screen,color,[(self.margin+self.width)*column+self.margin,(self.margin+self.height)*row+self.margin,self.width,self.height])
                color = self.WHITE
                if self.grid[row][column] == 1:
                    self.countfinal=self.countfinal+1
                else:
                    pygame.draw.circle(self.screen,color,[(self.margin+self.width)*column+self.margin+self.width/2,(self.margin+self.height)*row+self.margin+self.width/2], 2)
		leveltext=self.scorefont.render(str(row), 1,self.BLACK)
        	self.screen.blit(leveltext, ((self.margin+self.width)*column+self.margin, (self.margin+self.height)*row+self.margin))
    
    def drawwalls(self):
        for wall in self.walls:
            pygame.draw.rect(self.screen,self.BLUE,[(self.margin+self.width)*wall[0]+self.margin,(self.margin+self.height)*wall[1]+self.margin,self.width,self.height])

class Person(Maze):

	def __init__(self,x,y):
	    self.x = x	
	    self.y = y
	    self.totalMoves = 0
	    self.stalls = 0

	def checkWall(self,x,y,W):
	    if [x,y] in W:
		return True
	    else:
		return False

	def moveleft(self,W):
            if self.x <= 0: self.x = 19
            
            if self.checkWall(self.x-1,self.y,W): 
		self.x=self.x
	    else: self.x=(self.x)-1
	    return self		

	def moveright(self,W):
            if self.x >= 18: self.x = -1
    
            if self.checkWall(self.x+1,self.y,W): self.x=self.x
            else: self.x=(self.x)+1
	    return self

	def moveup(self,W):
            if self.y > 0:
                if self.checkWall(self.x,self.y-1,W):
                    self.y=self.y
	        else:
                    self.y=(self.y)-1
	        return self

	def movedown(self,W):
            if self.y < 21:
                if self.checkWall(self.x,self.y+1,W):
                    self.y=self.y
	        else:
                    self.y=(self.y)+1
            return self

class Pacman(Person):

	def __init__(self):
	    x = 9
	    y = 20
	    totalMoves = 0
	    stalls = 0
	    Person.__init__(self,x,y)
	
	def resetpacman(self):
	    x = randint(0,6)
	    y = randint(0,4)
	    Person.__init__(self,x,y)
	
	def collectCoin(self,Wa):
	    if Wa.grid[self.y][self.x] == 0:
		return True
	    else:
		return False

	def pacleft(self,Wa):
	    x = self.x
	    Person.moveleft(self,Wa.walls)
	    self.totalMoves = self.totalMoves + 1
	    print("Total moves: " + str(self.totalMoves))
	    if x == self.x:
		self.stalls = self.stalls + 1
		print("Stall: " + str(self.stalls))
	    if self.collectCoin(Wa):	    
		Wa.grid[self.y][self.x]=1
		Wa.score += 1
	    return self

	def pacright(self,Wa):
	    x = self.x
	    Person.moveright(self,Wa.walls)
	    self.totalMoves = self.totalMoves + 1
	    print("Total moves: " + str(self.totalMoves))
	    if x == self.x:
		self.stalls = self.stalls + 1
		print("Stall: " + str(self.stalls))
	    if self.collectCoin(Wa):	    
		Wa.grid[self.y][self.x]=1
		Wa.score += 1
	    return self

	def pacup(self,Wa):
	    x = self.x
            Person.moveup(self,Wa.walls)
            self.totalMoves = self.totalMoves + 1
            print("Total moves: " + str(self.totalMoves))
            if x == self.x:
                self.stalls = self.stalls + 1
                print("Stall: " + str(self.stalls))
	    if self.collectCoin(Wa):	    
		Wa.grid[self.y][self.x]=1
		Wa.score += 1
	    return self

	def pacdown(self,Wa):
	    x = self.x
            Person.movedown(self,Wa.walls)
            self.totalMoves = self.totalMoves + 1
            print("Total moves: " + str(self.totalMoves))
            if x == self.x:
                self.stalls = self.stalls + 1
                print("Stall: " + str(self.stalls))
	    if self.collectCoin(Wa):	    
		Wa.grid[self.y][self.x]=1
		Wa.score += 1
	    return self

        def pos(self,G):
	    pygame.draw.rect(G.screen,G.GREEN,[(G.margin+G.width)*self.x+G.margin,(G.margin+G.height)*self.y+G.margin,G.width,G.height])

	def checkGhost(self,V):
	    if [self.x,self.y] == [V.x,V.y]:
		return True
	    else:
		return False
	
	def pacPosition(self,G):
	    keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            	self.pacleft(G)
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            	self.pacright(G)
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
            	self.pacup(G)
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            	self.pacdown(G)

class Ghost(Person):

	def __init__(self,newx,newy):
	    x = newx
	    y = newy
	    Person.__init__(self,x,y)
	
	def resetghost(self):
	    x = 9
	    y = 10
	    Person.__init__(self,x,y)
	    return self

	def ghleft(self,Wa):
	    Person.moveleft(self,Wa.walls)
	    return self

	def ghright(self,Wa):
	    Person.moveright(self,Wa.walls)
	    return self

	def ghup(self,Wa):
	    Person.moveup(self,Wa.walls)
	    return self

	def ghdown(self,Wa):
	    Person.movedown(self,Wa.walls)
	    return self

	def pos(self,G):
	    myimage = pygame.image.load('ghostieR.jpg')
	    G.screen.blit(myimage,((G.margin+G.width)*self.x+G.margin,(G.margin+G.height)*self.y+G.margin))
	    #pygame.draw.rect(G.screen,G.RED,[(G.margin+G.width)*self.x+G.margin,(G.margin+G.height)*self.y+G.margin,G.width,G.height])
 
	def ghostPosition(self,G):
	    while 1 == 1:
		move = randint(0,3)
            	if move == 0:
			if self.checkWall(self.x-1,self.y,G.walls):
				print("WALL! " + str(self.x) + str(self.y))
				continue
			else:
	        		self.ghleft(G)
				break
            	elif move == 1:
			if self.checkWall(self.x+1,self.y,G.walls):
                                print("WALL! " + str(self.x) + str(self.y))
                                continue
                        else:
                                self.ghright(G)
                                break
            	elif move == 2:
			if self.checkWall(self.x,self.y+1,G.walls):
                                print("WALL! " + str(self.x) + str(self.y))
                                continue
                        else:
                                self.ghup(G)
                                break
            	elif move == 3:
			if self.checkWall(self.x,self.y-1,G.walls):
                                print("WALL! " + str(self.x) + str(self.y))
                                continue
                        else:
                                self.ghdown(G)
                                break
