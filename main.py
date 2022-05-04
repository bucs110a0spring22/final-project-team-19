import pygame
import sys
import controller
import turtle as pongball
import timer
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
      if width/2 <= mouse[0] <= width/2+140 and height/2 <=         mouse[1] <= height/2+40: 
                pygame.quit()

    window=pongball.Screen()
    window.title("Meta-Pong")
    window.bgcolor("green")
    window.setup(width=720,height=720)
    window.tracer(0)
    
def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    mylist = []
    mylist = input("enter a number four times: ")
    for item in mylist:
      print(item)
      newList = [mylist]
      print(swapList(newList))

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
