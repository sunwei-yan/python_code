from cmath import e
from tkinter import Y, EventType
from tkinter.tix import StdButtonBox
from turtle import distance, st
from cv2 import drawKeypoints
import pygame
import cv2
import random
import math
from sklearn.metrics import SCORERS

from sqlalchemy import distinct, false, true

# 初始化游戏界面
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("帅小伙爱冰冰")

 
sltb=bgimg=pygame.image.load('fj/sltb.png')
sbtb=bgimg=pygame.image.load('fj/sbtb.png')
bgimg=pygame.image.load('fj/bjn.png')
fjimg=pygame.image.load('fj/fj.png')
score=0
font=pygame.font.Font('freesansbold.ttf',32)
def xsfs():
    text=f"score:{score}"
    fsxs=font.render(text,True,(0,255,0))
    screen.blit(fsxs,(10,10))
# 飞机配置
fjimg=pygame.image.load('fj/fj.png')
fjx=400
fjy=470
stepfj=0
# # 飞机移动
def fjyd():
    global fjx,stepfj,running
    
    fjx+=stepfj
    if fjx >=740:
        fjx=740
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                stepfj=1.5
            if event.key==pygame.K_LEFT:
                stepfj=-1.5
            if event.key==pygame.K_SPACE:
                # print("发射子弹")
                
                zds.append(zd())

        if event.type==pygame.KEYUP:
            stepfj=0
        if event.type==pygame.QUIT:
            running=False
# 测距函数
def distance(bx,by,ex,ey):
    a=bx-ex
    b=by-ey
    return math.sqrt(a*a+b*b)

# 敌人配置
drrs=6
class ememy():
   def __init__(self):
       self.img=pygame.image.load('fj/bb.png')
       self.x=random.randint(200,600)
       self.y=random.randint(50,100)
       s=random.randint(20,30)
       self.step=s*0.1
       print(self.step)
   def reset(self):
        self.x=random.randint(200,600)
        self.y=random.randint(50,100)

       
emeies=[]
for i in range(drrs):
    emeies.append(ememy())
# 子弹
class zd():
   def __init__(self):
       self.img=pygame.image.load('fj/axzd.png')
       self.x=fjx
       self.y=fjy-5
       self.step=2
# 击中
   def hit(self):
        global score,gamewin
        for e in emeies:
            if(distance(self.x,self.y,e.x,e.y)<30):
                zds.remove(self)
                e.reset()
                score=score+1
                if score>52:
                    gamewin=True
                    print("yxs")


zds=[]
# 子弹发射
def zdfs():
    for b in zds:
        screen.blit(b.img,(b.x,b.y))
        b.hit()
        b.y-=b.step
        if b.y<0:
            zds.remove(b)
# dr=pygame.image.load('fj/eme.png')
# stepdr=0.05
# drx=random.randint(200,600)
# dry=random.randint(50,100)

  
# 敌人移动
def dryd():
    global drx,stepdr,running,gameover
    for e in emeies:
        screen.blit(e.img,(e.x,e.y))
        e.x=e.x+e.step
        if e.x>=740 or e.x<0:
            e.step*=-1
            e.y+=40
            if e.y>480:
                gameover=True
        
    # for event in pygame.event.get():
    #     if event.type==pygame.KEYDOWN:
    #         print(1231231)
    #         if event.key==pygame.K_d:
    #             stepdr=0.5
    #             print(stepdr)
    #         if event.key==pygame.K_a:
    #             stepdr=-0.5
    #             print(stepdr)
    #             print(drx)
            
    #     if event.type==pygame.KEYUP:
    #         stepdr=0
    #     if event.type==pygame.QUIT:
    #         running=False
# 游戏结束
gameover=False
def yxsl():
    if gameover:
        screen.blit(sbtb,(100,0))
        emeies.clear()

gamewin=False
def yxjs():
    if gamewin:
        screen.blit(sltb,(100,0))
        emeies.clear()
        
    
# 主循环

running=True
while running:
  
       
    screen.blit(bgimg,(0,0))
    screen.blit(fjimg,(fjx,fjy))
    fjyd()
    dryd()
    zdfs()
    xsfs()
    yxjs()
    yxsl()
    pygame.display.update()

