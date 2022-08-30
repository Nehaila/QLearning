import pygame
import sys
import random
import time
import numpy as np
import math

pygame.init() 
ROW,COL = 5,5
width, height = 400,400 #keep width/ROW and height/COL %2 =0 !!!!
clock=pygame.time.Clock()
screen= pygame.display.set_mode((width,height))
class board:
	def __init__(self): 
		self.board = [[],[],[]]
	def draw_squares(self,screenn):
		screen.fill((255,255,255))
		for row in range(0,ROW+1,1):
			for col in range(0,COL+1,1):
				pygame.draw.rect(screen,(0,0,0),(row*(width/ROW),col*(width/ROW),width/ROW,height/COL),1)


def randomcell():
	r=random.randint(1,2*ROW-1)
	while r%2 ==0 and r!=0:
		r=random.randint(1,2*ROW-1)
	c=random.randint(1,2*COL-1)
	while c%2 ==0 and c!=0:
		c=random.randint(1,2*COL-1)
	random1=0.5*r*(width/ROW)
	random2=0.5*c*(height/COL)
	return random1,random2
#ADD CLASS HERE
def cellneighbour(s1,s2):
	#1 for going right, 2 left, 3 up and 4 down
	step=0
	while step!=1:
		step=0
		a=random.randint(1,4)
		if a==1:
			if s1<=width-((3/2)*width)/ROW:
				s1=s1+width/ROW
				step=step+1
				return s1,s2
			# else:
			# 	return s1,s2
		elif a ==2:
			if s1>=((3/2)*width)/ROW:
				s1=s1-width/ROW
				step=step+1
				return s1,s2
			# else:
			# 	return s1,s2
		elif a ==3:
			if s2>= ((3/2)*height)/COL:
				s2=s2-height/COL
				step=step+1
				return s1,s2
			# else:
			# 	return s1,s2
		elif a==4:
			if s2<=height-((3/2)*height)/COL:
				s2=s2+height/COL
				step=step+1
				return s1,s2
			# else:
			# 	return s1,s2

def updatescreen(coord):
	pygame.draw.circle(screen,(255,0,0),coord,10)
	pygame.display.update()
	pygame.draw.circle(screen,(255,255,255),coord,10)
	pygame.display.update()

def drawMaze():
	t=0
	L=[]
	LL=[]
	while len(L)<=ROW*COL-1:
		if t==0:
			n,k= randomcell()
			a,b=cellneighbour(n,k)
			updatescreen((n,k))
			c,d=n,k
			LL.append((n,k))
			LL.append((c,d))
			t=t+1
		elif t>=2:
			c,d=a,b
			a,b=cellneighbour(c,d)
			co1=(a,b)
			o=0
			while (co1 in L or (a==c and b==d)) and o<5:
				a,b=cellneighbour(c,d)
				co1=(a,b)
				o=o+1
			if o>=5:
				a,b=c,d 
		if a==c and b!=d:
			co1=(a,b)
			pygame.draw.line(screen,(255,255,255),(1.5+a-(width/(2*ROW)),((b+d)/2)),(-1.5+c+(width/(2*ROW)),((b+d)/2)),4)
			updatescreen((c,d))
			updatescreen((a,b))
			if len(L)<ROW*COL-1 or len(L)<ROW*COL-2 :
				pygame.draw.circle(screen,(255,255,255),(a,b),10)	
			LL.append((a,b))
			clock.tick(20)
			L.append(co1)
			t=t+1
		elif b==d and a!=c:
			co1=(a,b)
			pygame.draw.line(screen,(255,255,255),(((a+c)/2),1.5+b-(height/(2*COL))),(((a+c)/2),-1.5+b+(height/(2*COL))),4)
			updatescreen((c,d))
			updatescreen((a,b))
			if len(L)==ROW*COL-2:
				pygame.display.update()	
			clock.tick(10)
			L.append(co1)
			LL.append((a,b))
			t=t+1
		else:
			r=len(LL)-1
			if r>0:
				a,b=LL[r]
				LL.remove(LL[r])
	return screen
				

class playmaze:
	def __init__(self): 
		self.end=[width-width/(2*ROW),height-height/(2*COL)]
		self.start=[width/(2*ROW),height/(2*COL)]
	def actionspace(self,coord):
		if coord[0]==width/(2*ROW) and coord[1]!=height/(2*COL) and coord[1]!=height-height/(2*COL):
			actionspace= {1: [width/ROW,0], 3:[0,-height/COL],4:[0,height/COL]}
		elif coord[1]==height/(2*COL) and coord[0]!=width/(2*ROW) and coord[0]!=width-width/(2*ROW):
			actionspace= {1: [width/ROW,0], 2:[-width/ROW,0],4:[0,height/COL]}
		elif coord[0]==width/(2*ROW) and coord[1]==height/(2*COL):
			actionspace= {1: [width/ROW,0], 4:[0,height/COL]}
		elif coord[0]==width-width/(2*ROW) and coord[1]!=height-height/(2*COL) and coord[1]!=height/(2*COL):
			actionspace= {2:[-width/ROW,0],3:[0,-height/COL],4:[0,height/COL]}
		elif coord[1]==height-height/(2*COL) and coord[0]!=width-width/(2*ROW) and coord[0]!=width/(2*ROW):
			actionspace= {1: [width/ROW,0], 2:[-width/ROW,0],3:[0,-height/COL]}
		elif coord[1]==height-height/(2*COL) and coord[0]==width-width/(2*ROW):
			actionspace= {2:[-width/ROW,0],3:[0,-height/COL]}
		elif coord[0]==width/(2*ROW) and coord[1]==height-height/(2*COL):
			actionspace= {1: [width/ROW,0], 3:[0,-height/COL]}
		elif coord[0]== width-width/(2*ROW) and coord[1]==height/(2*COL):
			actionspace= {2:[-width/ROW,0],4:[0,height/COL]}
		else:
			actionspace= {1: [width/ROW,0], 2:[-width/ROW,0],3:[0,-height/COL],4:[0,height/COL]}
		return actionspace
	def States(self):
		S=[]
		for i in range(1,2*ROW,2):
			for j in range(1,2*COL,2):
				S.append((i*(width/(2*ROW)),j*(height/(2*COL))))
		return S
	def reward(self,coord):
		#Reward 10 vs 1 makes a big difference on how fast the algorithm learns.
		if coord==self.end:
			reward= 10
			return reward
		else:
			reward=-1
			return reward
	def policy(self,coord):
		prob={}
		for j in self.actionspace(coord).keys():
			prob[j]=1/len(self.actionspace(coord).keys())
		return prob
	def IsMoveValid(self,coord,i):
		if i in self.actionspace(coord).keys():
			new_coord=[n1+n2 for n1,n2 in zip(coord,self.actionspace(coord)[i])]
			if i in (1,2):
				test_coord=[int((coord[0]+new_coord[0])/2),int(coord[1])]
				if tuple(screen.get_at((test_coord[0],test_coord[1])))==(0,0,0,255):
					return False
				else:
					return True
			elif i in (3,4):
				test_coord=[int(coord[0]),int((coord[1]+new_coord[1])/2)]
				if tuple(screen.get_at((test_coord[0],test_coord[1])))==(0,0,0,255):
					return False
				else:
					return True
		else:
			return False


	def selectAction(self,st,Q,epsilon):
		n=random.uniform(0,1)
		S=self.States()
		s=S.index(tuple(st))
		if n<epsilon:
			a=random.choice(list(self.actionspace(st).keys()))-1
			while Q[s][a]==-100:
				a=random.choice(list(self.actionspace(st).keys()))-1
		else:
			#Why we have -100
			a=np.argmax(Q[s])
		print(n)
		print(epsilon)
		return a
	def QTable(self):
		#D[1]=Actions for state 1, states are in the order of self.S()
		S=self.States()
		Q=np.zeros((len(self.States()),4))
		for s in range(len(Q)):
			for i in range(1,len(Q[s])):
				if i in list(self.actionspace(S[s]).keys()):
					Q[s][i-1]=0
				else:
					Q[s][i-1]=-100
		return Q
	def Qlearning(self):
		init_s=self.start
		S=self.States()
		Q=self.QTable()
		epsilon=1
		counts=0
		while counts<100:
			#print(counts)
			epsilon=epsilon-0.01
			final_s=self.start
			AlreadyVisited=[init_s]
			while final_s!=self.end:
				a=self.selectAction(init_s,Q,epsilon)+1
				if self.IsMoveValid(init_s,a)==True:
					final_s=[S1+S2 for S1,S2 in zip(init_s,self.actionspace(init_s)[a])]
					s=S.index(tuple(init_s))
					s2=S.index(tuple(final_s))
					LM=[]
					LM=list(self.actionspace(final_s).keys())
					# if final_s in AlreadyVisited:
					# 	Q[s][a-1]=Q[s][a-1]+0.9*(self.reward(final_s)+0.9*(max([Q[s2][i-1] for i in LM]))-Q[s][a-1])
					# else:
					Q[s][a-1]=Q[s][a-1]+0.9*(self.reward(final_s)+0.9*(max([Q[s2][i-1] for i in LM]))-Q[s][a-1])						
					init_s=final_s
					AlreadyVisited.append(final_s)
					pygame.display.update()
					pygame.draw.circle(screen,(255,0,0),(init_s[0],init_s[1]),10)
					pygame.display.update()
					pygame.draw.circle(screen,(255,255,255),(init_s[0],init_s[1]),10)
					clock.tick(20)
					if init_s==self.end:
						counts=counts+1
						init_s=self.start
						if counts==99:
							return Q,S
				else:
					init_s=final_s
b=board()
b.draw_squares(screen)
drawMaze()
y=playmaze()
y.Qlearning()
# y.nowplay()


running = True
while running:
  	for event in pygame.event.get():
	    if event.type == pygame.QUIT:
	    	running = False
	    if running == False:
	    	pygame.quit()
