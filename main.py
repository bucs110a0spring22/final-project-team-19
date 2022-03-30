import pygame
#import your controller

def swapList(newList):
  newList[0], newList[-1] = newList[-1], newList[0]
  return newList


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
