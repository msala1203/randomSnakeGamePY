#comment New code
#get keyboard input
import random
import msvcrt
import time
import os

boardsize = 20

currentBoardState = []

def clearScreen():
    # Move cursor to top-left and clear screen
    # \x1b = ESC
    print("\x1b[2J\x1b[H", end="")

class Snake():
    currentDirection = 'right'
    headPosition = [random.randrange(0,boardsize), random.randrange(0,boardsize)]
    headCharacter = 'H'
    tailPosition = [headPosition[0], headPosition[1]-1]
    tailDirection = 'right'
    tailCharacter = 'T'
    length = 1
    alive = True

    def __init__(self, xPosition, yPosition, length):
        self.headPosition[0] = xPosition
        self.headPosition[1] = yPosition
        self.length = length

    @classmethod
    def updateSnakeHeadPosition(self):
        if self.currentDirection == 'right':
            self.headPosition[1] += 1
        elif self.currentDirection == 'left':
            self.headPosition[1] -= 1
        elif self.currentDirection == 'up':
            self.headPosition[0] += 1
        elif self.currentDirection == 'down':
            self.headPosition[0] -= 1


    @classmethod
    def updateSnakeDirection(self, input):
        if input == None:
            self.currentDirection = self.currentDirection
        elif input == 'w' and self.currentDirection != 'down':
            self.currentDirection = 'up'
        elif input == 's' and self.currentDirection != 'up':
            self.currentDirection = 'down'
        elif input == 'a' and self.currentDirection != 'right':
            self.currentDirection = 'left'
        elif input == 'd' and self.currentDirection != 'left':
            self.currentDirection = 'right'



def keyboardInputCheck():
    if msvcrt.kbhit():
        return msvcrt.getwch()
    else:
        return None

def generateBoard():
    #create new board
    for i in range(boardsize):
        currentBoardState.append([])
        for j in range(boardsize):
            currentBoardState[i].append('.')


def generateNewAppleLocation():
    positionX = random.randrange(0,boardsize-1)
    positionY = random.randrange(0,boardsize-1)

    while currentBoardState[positionX][positionY] != '.':
        positionX = random.randrange(0,boardsize-1)
        positionY = random.randrange(0,boardsize-1)
    
    currentBoardState[positionX][positionY] = 'O'

def generateSnake():
    snake = Snake(10, 5, 0)

    snake.tailPosition = [snake.headPosition[0], snake.headPosition[1]-1]

    currentBoardState[snake.headPosition[0]][snake.headPosition[1]] = snake.headCharacter
    currentBoardState[snake.tailPosition[0]][snake.tailPosition[1]] = snake.tailCharacter



def printBoard():
    clearScreen()

    boardString = ""

    boardString += "\nScore: " + "0"

    boardString += "\n"

    for i in range(len(currentBoardState)):
        boardString += "==="

    boardString += "\n"


    for i in range(len(currentBoardState)):
        boardString += "\n"
        for j in range(len(currentBoardState)):
            boardString += " " + currentBoardState[i][j] + " "

    boardString += "\n\n"

    for i in range(len(currentBoardState)):
        boardString += "==="

    return boardString

playingGame = True

generateBoard()
generateNewAppleLocation()
generateSnake()

#Main Game loop
while playingGame:
    
    #game logic
    currentInput = keyboardInputCheck()
    

    


    if (currentInput == "q"):
        break
    
    #render
    print(printBoard())

    #time Control
    time.sleep(1/60)
    
    




'''
generateBoard()
generateNewAppleLocation()
printBoard()
'''

'''
while True:
    input = msvcrt.getwch()
    print(input)
    if (input == "q"):
        break
'''