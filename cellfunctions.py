import random
from tkinter import *
import celldictionaries as cdicts
from tkinter import messagebox
class boardFuncs:
    class nonIntBoardFuncs:
        def __init__(self):
            self.n = 8
            self.window = Tk()
            self.window.title("65536")
            self.gameArea = Frame(self.window , bg = "azure3")
            self.board = []
            self.gridCell = [[0] * 8 for i in range(8)]
            self.compress = False
            self.merge = False
            self.moved = False
            self.score = 0
            for i in range(8):
                rows = []
                for j in range(8):
                    l = Label(self.gameArea , text = "" , bg = "azure4" , 
                    font = ("comfortaa" , 15 , "normal") , width = 4 , height = 2)
                    l.grid(row = i , column = j , padx = 7 , pady = 7)
                    rows.append(l)
                self.board.append(rows)
            self.gameArea.grid()
        def reverse(self):
            for ind in range(8):
                i = 0
                j = 7
                while(i < j):
                    self.gridCell[ind][i] , self.gridCell[ind][j] = self.gridCell[ind][j] , self.gridCell[ind][i]
                    i += 1
                    j -= 1
        def transpose(self):
            self.gridCell = [list(t) for t in zip(*self.gridCell)]
        def compressGrid(self):
            self.compress = False
            temp = [[0] * 8 for i in range(8)]
            for i in range(8):
                cnt = 0
                for j in range(8):
                    if self.gridCell[i][j] != 0:
                        temp[i][cnt] = self.gridCell[i][j]
                        if cnt != j:
                            self.compress = True
                        cnt += 1
            self.gridCell = temp
        def mergeGrid(self):
            self.merge = False
            for i in range(8):
                for j in range(8 - 1):
                    if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                        self.gridCell[i][j] *= 2
                        self.gridCell[i][j + 1] = 0
                        self.score += self.gridCell[i][j]
                        self.merge = True
        def randomCell(self):
            cells = []
            for i in range(8):
                for j in range(8):
                    if self.gridCell[i][j] == 0:
                        cells.append((i , j))
            curr = random.choice(cells)
            i = curr[0]
            j = curr[1]
            tileList = [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 2]
            luckyList = [2 , 2 , 2 , 2 , 2 , 2 , 2 , 2 , 2 , 4]
            randNum = random.choice(tileList)
            if randNum == 1:
                self.gridCell[i][j] = randNum
            else:
                self.gridCell[i][j] = random.choice(luckyList)
        def canMerge(self):
            for i in range(8):
                for j in range(7):
                    if self.gridCell[i][j] == self.gridCell[i][j + 1]:
                        return True
            for i in range(7):
                for j in range(8):
                    if self.gridCell[i + 1][j] == self.gridCell[i][j]:
                        return True
            return False
        def paintGrid(self):
            for i in range(8):
                for j in range(8):
                    if self.gridCell[i][j] == 0:
                        self.board[i][j].config(text = "" , bg = "azure4")
                    else:
                        self.board[i][j].config(text = str(self.gridCell[i][j]) , 
                        bg = cdicts.nonIntDicts.bgColor.get(str(self.gridCell[i][j])) , 
                        fg = cdicts.nonIntDicts.fgColor.get(str(self.gridCell[i][j])))
    class intBoardFuncs:
        def intPaintGrid(self):
            for i in range(8):
                for j in range(8):
                    if self.gridCell[i][j] == 0:
                        self.board[i][j].config(text = "" , bg = "azure4")
                    else:
                        self.board[i][j].config(text = str(self.gridCell[i][j]) , 
                        bg = cdicts.intDicts.intBgColor.get(str(self.gridCell[i][j])) , 
                        fg = cdicts.intDicts.intFgColor.get(str(self.gridCell[i][j])))
class gameFuncs:
    class nonIntGameFuncs:
        def __init__(self , gamepanel):
            self.gamepanel = gamepanel
            self.end = False
            self.won = False
        def start(self):
            self.gamepanel.nonIntBoardFuncs.randomCell()
            self.gamepanel.randomCell()
            self.gamepanel.paintGrid()
            self.gamepanel.window.bind("<Key>" , self.linkKeys)
            self.gamepanel.window.mainloop()
        def linkKeys(self , event):
            mouse = 0
            if self.end or self.won:
                return
            self.gamepanel.compress = False
            self.gamepanel.merge = False
            self.gamepanel.moved = False
            pressedKey = event.keysym
            if pressedKey == "Up":
                self.gamepanel.transpose()
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
                self.gamepanel.transpose()
            elif pressedKey == "Down":
                self.gamepanel.transpose()
                self.gamepanel.reverse()
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
                self.gamepanel.reverse()
                self.gamepanel.transpose()
            elif pressedKey == "Left":
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
            elif pressedKey == "Right":
                self.gamepanel.reverse()
                self.gamepanel.compressGrid()
                self.gamepanel.mergeGrid()
                self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
                self.gamepanel.compressGrid()
                self.gamepanel.reverse()
            elif pressedKey == "Alt_R":
                self.gamepanel.__init__()
                self.start()
            elif pressedKey == "Alt_L":
                mouse = 1
                self.gamepanel.__init__()
                self.intStart()
            else:
                pass
            if mouse == 0:
                self.gamepanel.paintGrid()
            else:
                self.gamepanel.intPaintGrid()
            print(self.gamepanel.score)
            flag = 0
            for i in range(8):
                for j in range(8):
                    if(self.gamepanel.gridCell[i][j] == 65536):
                       flag = 1
                       break
            if flag == 1:
                self.won = True
                messagebox.showinfo("65536" , message = "You won! Credits to Mr.Unity Buddy!")
                print("Won")
                print("Credits to Mr.Unity Buddy!")
                messagebox.showinfo("Score" , self.gamepanel.score)
                x = 500
                while x > 0:
                    print(".")
                    print(" .")
                    print("  .")
                    print("   .")
                    print("    .")
                    print("     .")
                    print("     .")
                    print("    .")
                    print("   .")
                    print("  .")
                    print(" .")
                    print(".")
                    x = x - 1
                self.gamepanel.__init__()
                self.start()
                return
            for i in range(8):
                for j in range(8):
                    if self.gamepanel.gridCell[i][j] == 0:
                        flag = 1
                        break
            if not(flag or self.gamepanel.canMerge()):
                self.end = True
                messagebox.showinfo("65536" , message = "Game over! Credits to Mr.Unity Buddy!")
                print("Over")
                print("Credits to Mr.Unity Buddy!")
                messagebox.showinfo("Score" , self.gamepanel.score)
                x = 500
                while x > 0:
                    print(".")
                    print(" .")
                    print("  .")
                    print("   .")
                    print("    .")
                    print("     .")
                    print("     .")
                    print("    .")
                    print("   .")
                    print("  .")
                    print(" .")
                    print(".")
                    x = x - 1
                self.gamepanel.__init__()
                self.start()
                return
            if self.gamepanel.moved:
                self.gamepanel.randomCell()
                if mouse == 0:
                    self.gamepanel.paintGrid()
                elif mouse == 1:
                    self.gamepanel.intPaintGrid()
                else:
                    pass
    class intGameFuncs:
        def intStart(self):
            self.gamepanel.randomCell()
            self.gamepanel.randomCell()
            self.gamepanel.intPaintGrid()
            self.gamepanel.window.bind("<Key>" , self.linkKeys)
            self.gamepanel.window.mainloop()
