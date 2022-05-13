import pygame
import sys
import controller
import turtle as pongball
import threading
import time
playerAscore = 0
playerBscore = 0
#import your controller

pygame.init()
res = (720,720)
screen = pygame.display.set_mode()

color = (255,255,255)
color_light = (170,170,170)
width = screen.get_width()
height = screen.get_height()

font = pygame.font.SysFont('Impact',40, color)
text = font.render('quit', True, color)

while True:
  mouse = pygame.mouse.get_pos()
  for ev in pygame.event.get():
    if ev.type == pygame.QUIT:
      pygame.quit()
    if ev.type == pygame.MOUSEBUTTONDOWN:
      if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.quit()

    window=pongball.Screen()
    window.title("Meta-Pong")
    window.bgcolor("green")
    window.setup(width=width, height=height)
    
    
def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    mylist = []
    mylist = input("enter a number four times: ")
    for item in mylist:
      print(item)
      newList = [mylist]
      print.swapList(newList)

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
  #creating the left paddle
lpaddle=pongball.Turtle()
lpaddle.speed(0)
lpaddle.shape("square")
lpaddle.color("white")
lpaddle.shapesize(stretch_wid=5,stretch_len=1)
lpaddle.penup()
lpaddle.goto(-350,0)

  #creating the right paddle
rpaddle=pongball.Turtle()
rpaddle.speed(0)
rpaddle.shape("square")
rpaddle.color("white")
rpaddle.shapesize(stretch_wid=5,stretch_len=1)
rpaddle.penup()
rpaddle.goto(-350,0)

  #creating scorecard
pen=pongball.Turtle()
pen.speed(0)
pen.color("Red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('Arial',22,'normal'))

  #moving right paddle
def rightpaddleup():
    y=rpaddle.ycor()
    y=y+90
    rpaddle.sety(y)
  
def rightpaddledown():
    y=rpaddle.ycor()
    y=y+90
    rpaddle.sety(y)

  #moving left paddle

def leftpaddleup():
    y=lpaddle.ycor()
    y=y+90
    lpaddle.sety(y)
  
def leftpaddledown():
    y=lpaddle.ycor()
    y=y+90
    lpaddle.sety(y)

  #assigning keys
window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')

while True:
  window.update()


  #Setting up borders for the game
if pongball.ycor()>290:
  pongball.sety(290)
  ballydirection=ballydirection*-1
if pongball.ycor()<-290:
  pongball.sety(-290)
  ballydirection=ballydirection*-1
        
if pongball.xcor() > 390:
  pongball.goto(0,0)
  ball_dx = ball_dx * -1
  player_a_score = playerAscore + 1
  pen.clear()
  pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
os.system("afplay wallhit.wav&")

  #Paddle Collisions
if(pongball.xcor() > 340) and (pongball.xcor() < 350) and (pongball.ycor() < rpaddle.ycor() + 40 and pongball.ycor() > rpaddle.ycor() - 40):
  pongball.setx(340)
  ball_dx = ball_dx * -1
  os.system("afplay paddle.wav&")
  
if(pongball.xcor() < -340) and (pongball.xcor() > -350) and (pongball.ycor() < lpaddle.ycor() + 40 and pongball.ycor() > lpaddle.ycor() - 40):
  pongball.setx(-340)
  ball_dx = ball_dx * -1
  os.system("afplay paddle.wav&")