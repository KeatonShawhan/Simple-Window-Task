#-----import statements-----
import turtle as trtl
import random as rand
import time

#-----game configuration----
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
turns = 1

#------create turtles-------
square0 = trtl.Turtle()
square0.shape("square")
square0.turtlesize(6)
square0.penup()
square0.goto(-150,150)

square1 = trtl.Turtle()
square1.shape("square")
square1.turtlesize(6)
square1.penup()
square1.goto(0,150)

square2 = trtl.Turtle()
square2.shape("square")
square2.turtlesize(6)
square2.penup()
square2.goto(150,150)

square3 = trtl.Turtle()
square3.shape("square")
square3.turtlesize(6)
square3.penup()
square3.goto(-150, 0)

square4 = trtl.Turtle()
square4.shape("square")
square4.turtlesize(6)
square4.penup()
square4.goto(0,0)

square5 = trtl.Turtle()
square5.shape("square")
square5.turtlesize(6)
square5.penup()
square5.goto(150,0)

square6 = trtl.Turtle()
square6.shape("square")
square6.turtlesize(6)
square6.penup()
square6.goto(-150,-150)

square7 = trtl.Turtle()
square7.shape("square")
square7.turtlesize(6)
square7.penup()
square7.goto(0,-150)

square8 = trtl.Turtle()
square8.shape("square")
square8.turtlesize(6)
square8.penup()
square8.goto(150, -150)

squareListOrder = []
squareList = [square0, square1, square2, square3, square4, square5, square6, square7, square8]
randomSquare = rand.randint(0,8)

#-----game functions--------
# Make User input function, onkeypress activation

player_turn = False
computer_turn = True
clicks = 1
i = 0
allClicked = 0

# squareClicked function = the player turn

def squareClicked(x,y):
  global i, allClicked, computer_turn, player_turn
  x = int(x)
  y = int(y)
  print(x)
  print(int(squareListOrder[0].xcor()))
  if int(squareListOrder[0].xcor()) in range(x-60, x+60) and int(squareListOrder[0].ycor()) in range(y-60, y+60):
    player_turn = True
    if player_turn:
      global randomSquare
      allClicked += 1
      squareListOrder[0].color("blue")
      time.sleep(0.3)
      squareListOrder[0].color("black")
      squareListOrder.append(squareListOrder.pop(0))
      print(f'i: {i} and allClicked: {allClicked}')
    if (allClicked == i):
      allClicked = 0
      player_turn = False
      computer_turn = True
      TurnSys(turns, randomSquare, computer_turn, player_turn, allClicked)

# def player_clicks(clicks):

def computerOrder(turns, randomSquare):
  randomSquare = rand.randint(0,8)
  squareListOrder.append(squareList[randomSquare])
  squareListOrder[len(squareListOrder) - 1].onclick(squareClicked)
  computerRepeat()
  
def computerRepeat():
  for y in squareListOrder:
    y.color("green")
    time.sleep(0.3)
    y.color("black")
    time.sleep(0.3)

def TurnSys(turns, randomSquare, computer_turn, player_turn, allClicked):
  global i
  if (i < 6):
    while (computer_turn):
      for t in range(turns):
        i += 1
        computerOrder(turns, randomSquare)
        computer_turn = False
        player_turn = True


        
#def playerClick(allClicked, i, player_turn, computer_turn):
 # while (allClicked != i):
  #  player_turn = True
 # computer_turn = True


  
    

TurnSys(turns, randomSquare, computer_turn, player_turn, allClicked)




# check if squareListOrder[1] is clicked (1st round square)
# put the first round square (squareListOrder[1] into the back of the list)
# now the 2nd round square is squareListOrder[1], repreating to check if the 2nd round square is clicked)


#----------inputs-----------
# User input is on click


wn.listen()
wn.mainloop()