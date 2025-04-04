#Made by ArtiXGamer
#Creation start date: 02.04.2025
#Finished: almost the same day, 04.04.2025, it takes about 3-4h

import time
import os

mainMenuOptions = [
    "0 Exit",
    "1 Start game",
    "2 Creator",
    "3 Keybinds (not available)",
    "4 Statistics (not available)"
]

class Board:
    def __init__(self):
        self.v = [" "] * 9
        self.leftMoves = 9
    
    def GetBoard(self):
        return f"""
      1   2   3
    ┌───┬───┬───┐
  1 │ {self.v[0]} │ {self.v[1]} │ {self.v[2]} │
    ├───┼───┼───┤
  2 │ {self.v[3]} │ {self.v[4]} │ {self.v[5]} │
    ├───┼───┼───┤
  3 │ {self.v[6]} │ {self.v[7]} │ {self.v[8]} │
    └───┴───┴───┘
    """
    
    def ChangeCell(self, cellNumb, player):
        if self.v[cellNumb] == " ":
            self.v[cellNumb] = player
            self.leftMoves -= 1
            return True
        else:
            return False

def DrawLine():
    print("=" * 28)

def LoadMainMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    DrawLine()
    print("Select an option:")
    DrawLine()
    for option in mainMenuOptions:
        print(option)
    DrawLine()

def WrongInput(errorNumb):
    os.system('cls' if os.name == 'nt' else 'clear')
    DrawLine()
    print("Wrong choice!\nerror:", errorNumb)
    DrawLine()
    time.sleep(2)

def LoadCredits():
    os.system('cls' if os.name == 'nt' else 'clear')
    DrawLine()
    print("Made by autistic ArtiXGamer")
    DrawLine()
    input("Enter to continue... ")

def WinCommunicat(winer):
    DrawLine()
    print("Player",winer,", you win!")
    DrawLine()
    input("Enter to continue... ")

def DrawCommunicat():
    os.system('cls' if os.name == 'nt' else 'clear')
    DrawLine()
    print("DRAW! Nobody wins")
    DrawLine()
    input("Enter to continue... ")

def StartGame():
    board = Board()
    turn = "O"
    game = True
        
    while game:
        turn = "X" if turn == "O" else "O"

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            DrawLine()
            print("Player", turn, "turn")
            DrawLine()
            print(board.GetBoard())
            DrawLine()

            choosenCell = input("Select a cell (column + row): ")

            if len(choosenCell) == 2 and choosenCell.isdigit():
                column, row = int(choosenCell[0]), int(choosenCell[1])
                if 1 <= column <= 3 and 1 <= row <= 3:
                    cellIndex = (row - 1) * 3 + (column - 1)
                    if board.ChangeCell(cellIndex, turn):

                        # Checking for win (not optimized)
                        
                        for i in range(0,3):
                            if ((board.v[i*3] == "X") or (board.v[i*3] == "O")) and board.v[i*3] == board.v[i*3+1]:
                                if board.v[i*3+1] == board.v[i*3+2]: # rows
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    DrawLine()
                                    print(board.GetBoard())                        
                                    WinCommunicat(turn)
                                    game = False
                                    break
                            elif ((board.v[i] == "X") or (board.v[i] == "O")) and board.v[i] == board.v[i+3]: # columns
                                if board.v[i+3] == board.v[i+6]:
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    DrawLine()
                                    print(board.GetBoard())                        
                                    WinCommunicat(turn)
                                    game = False
                                    break
                                    
                        for i in range(0,2):
                            if board.v[i*2] == "X" or board.v[i*2] == "O":
                                if board.v[i*2] == board.v[i*2+(4-i*2)]:
                                    if board.v[i*2+(4-i*2)] == board.v[i*2+2*(4-i*2)]:
                                        os.system('cls' if os.name == 'nt' else 'clear')
                                        DrawLine()
                                        print(board.GetBoard())                        
                                        WinCommunicat(turn)
                                        game = False
                                        break 
                                
                        if board.leftMoves == 0:
                            game = False
                            DrawCommunicat()
                        break
                    else:
                        WrongInput("Cell is already occupied")
                else:
                    WrongInput("Cell doesn't exist")
            else:
                WrongInput("Invalid input (format: two digits)")

def LoadChoosenOption(choosenOption):
    if choosenOption == 0:
        quit()
    elif choosenOption == 1:
        StartGame()
    elif choosenOption == 2:
        LoadCredits()

def MainMenu():
    while True:
        while True:
            try:
                LoadMainMenu()
                choosenOption = int(input("I'm choosing: "))
                if 0 <= choosenOption < len(mainMenuOptions):
                    break
                else:
                    WrongInput("Out of range")
            except ValueError:
                WrongInput("Letter was received")
        LoadChoosenOption(choosenOption)

MainMenu()
