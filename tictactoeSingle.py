import tkinter as tk
import tkinter.font as font
from tkinter import ttk
import random
import time

#This is the root class
class StartApp(tk.Tk):

    #Constructor of root class
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame = None
        self.title('Tic Tac Toe')
        global font1
        font1 = font.Font(family="Times New Roman", size=20)
        self.switchframe(StartFrame)

    #This method helps switch the frames
    def switchframe(self, frame_class):
        newframe = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = newframe
        self.frame.pack()

    #This method can help pass winning character as argument to another Frame
    def endgame(self, frame, win, board):
        newframe = frame(self, win, board)
        self.frame.destroy()
        self.frame = newframe
        self.frame.pack()


#This is the Frame of Start Window
class StartFrame(ttk.Frame):

    #Constructor of Start Window Frame
    def __init__(self, master):
        super().__init__(master)
        global font1
        text = tk.Label(self, text = 'Press the button to start', font = font1)
        button = tk.Button(self, text = 'Start', bg = 'black', fg = 'white',
                            font = font1, command = lambda:master.switchframe(StartGame))
        text.grid(row = 0, column = 0, padx = 5, pady = 5)
        button.grid(row = 1, column = 0, padx = 5, pady = 5)


#This is the Frame of Main Game
class StartGame(ttk.Frame):

    #Initialization of class variables
    player = 1
    position = []

    #Constructor for the Game Frame
    def __init__(self, master):
        super().__init__(master)
        self.reset()
        self.master = master
        global font1
        position1 = tk.Button(self, textvariable = self.position[0],
                                font = font1, command = lambda:self.switch(0), width = 3)
        position2 = tk.Button(self, textvariable = self.position[1], 
                                font = font1, command = lambda:self.switch(1), width = 3)
        position3 = tk.Button(self, textvariable = self.position[2],
                                font = font1, command = lambda:self.switch(2), width = 3)
        position4 = tk.Button(self, textvariable = self.position[3],
                                font = font1, command = lambda:self.switch(3))
        position5 = tk.Button(self, textvariable = self.position[4],
                                font = font1, command = lambda:self.switch(4))
        position6 = tk.Button(self, textvariable = self.position[5],
                                font = font1, command = lambda:self.switch(5))
        position7 = tk.Button(self, textvariable = self.position[6],
                                font = font1, command = lambda:self.switch(6))
        position8 = tk.Button(self, textvariable = self.position[7],
                                font = font1, command = lambda:self.switch(7))
        position9 = tk.Button(self, textvariable = self.position[8],
                                font = font1, command = lambda:self.switch(8))
        position1.grid(row = 0, column = 0, sticky = "NSEW")
        position2.grid(row = 0, column = 1, sticky = "NSEW")
        position3.grid(row = 0, column = 2, sticky = "NSEW")
        position4.grid(row = 1, column = 0, sticky = "NSEW")
        position5.grid(row = 1, column = 1, sticky = "NSEW")
        position6.grid(row = 1, column = 2, sticky = "NSEW")
        position7.grid(row = 2, column = 0, sticky = "NSEW")
        position8.grid(row = 2, column = 1, sticky = "NSEW")
        position9.grid(row = 2, column = 2, sticky = "NSEW")
    
    #This method is used to reset the 'X' and 'O' from the Frame
    def reset(self):
        self.position = []
        tkvar = tk.StringVar()
        for i in range(9):
            tkvar = tk.StringVar()
            tkvar.set(' ')
            self.position.append(tkvar)

    #This method is used to mark 'X' and 'O' and to switch to Winner Frame
    def switch(self, i):
        if str(self.position[i].get()) == ' ':
            if self.player % 2:
                self.position[i].set('X')
                self.player += 1
            else:
                self.position[i].set('O')
                self.player += 1
        
        self.computerPlay()

        check = self.check()
        position = [i.get() for i in self.position]
        if check[0] == True or ' ' not in position:
            if ' ' not in position and check[0] == False:
                winner = 'No one'
            else:
                winner = check[1]
            position = [i.get() for i in self.position]
            self.master.endgame(Winner, winner, position)
    
    #This method marks O
    def computerPlay(self):
        position = [i.get() for i in self.position]
        if ' ' not in position:
            return

        #These check the conditions for O winning
        if position[0] == position[1] == 'O' and position[2] == ' ':
            self.position[2].set('O')
        elif position[3] == position[4] == 'O' and position[5] == ' ':
            self.position[5].set('O')
        elif position[6] == position[7] == 'O' and position[8] == ' ':
            self.position[8].set('O')
        elif position[1] == position[2] == 'O' and position[0] == ' ':
            self.position[0].set('O')
        elif position[4] == position[5] == 'O' and position[3] == ' ':
            self.position[3].set('O')
        elif position[7] == position[8] == 'O' and position[6] == ' ':
            self.position[6].set('O')
        elif position[0] == position[2] == 'O' and position[1] == ' ':
            self.position[1].set('O')
        elif position[3] == position[5] == 'O' and position[4] == ' ':
            self.position[4].set('O')
        elif position[6] == position[8] == 'O' and position[7] == ' ':
            self.position[7].set('O')
        elif position[0] == position[3] == 'O' and position[6] == ' ':
            self.position[6].set('O')
        elif position[1] == position[4] == 'O' and position[7] == ' ':
            self.position[7].set('O')
        elif position[2] == position[5] == 'O' and position[8] == ' ':
            self.position[8].set('O')
        elif position[3] == position[6] == 'O' and position[0] == ' ':
            self.position[0].set('O')
        elif position[4] == position[7] == 'O' and position[1] == ' ':
            self.position[1].set('O')
        elif position[5] == position[8] == 'O' and position[2] == ' ':
            self.position[2].set('O')
        elif position[0] == position[6] == 'O' and position[3] == ' ':
            self.position[3].set('O')
        elif position[1] == position[7] == 'O' and position[4] == ' ':
            self.position[4].set('O')
        elif position[2] == position[8] == 'O' and position[5] == ' ':
            self.position[5].set('O')
        elif position[0] == position[4] == 'O' and position[8] == ' ':
            self.position[8].set('O')
        elif position[4] == position[8] == 'O' and position[0] == ' ':
            self.position[0].set('O')
        elif position[0] == position[8] == 'O' and position[4] == ' ':
            self.position[4].set('O')
        elif position[2] == position[4] == 'O' and position[6] == ' ':
            self.position[6].set('O')
        elif position[2] == position[6] == 'O' and position[4] == ' ':
            self.position[4].set('O')
        elif position[6] == position[4] == 'O' and position[2] == ' ':
            self.position[2].set('O')

        #These check the conditions for X winning and blocks it
        elif position[0] == position[1] == 'X' and position[2] == ' ':
            self.position[2].set('O')
        elif position[3] == position[4] == 'X' and position[5] == ' ':
            self.position[5].set('O')
        elif position[6] == position[7] == 'X' and position[8] == ' ':
            self.position[8].set('O')
        elif position[1] == position[2] == 'X' and position[0] == ' ':
            self.position[0].set('O')
        elif position[4] == position[5] == 'X' and position[3] == ' ':
            self.position[3].set('O')
        elif position[7] == position[8] == 'X' and position[6] == ' ':
            self.position[6].set('O')
        elif position[0] == position[2] == 'X' and position[1] == ' ':
            self.position[1].set('O')
        elif position[3] == position[5] == 'X' and position[4] == ' ':
            self.position[4].set('O')
        elif position[6] == position[8] == 'X' and position[7] == ' ':
            self.position[7].set('O')
        elif position[0] == position[3] == 'X' and position[6] == ' ':
            self.position[6].set('O')
        elif position[1] == position[4] == 'X' and position[7] == ' ':
            self.position[7].set('O')
        elif position[2] == position[5] == 'X' and position[8] == ' ':
            self.position[8].set('O')
        elif position[3] == position[6] == 'X' and position[0] == ' ':
            self.position[0].set('O')
        elif position[4] == position[7] == 'X' and position[1] == ' ':
            self.position[1].set('O')
        elif position[5] == position[8] == 'X' and position[2] == ' ':
            self.position[2].set('O')
        elif position[0] == position[6] == 'X' and position[3] == ' ':
            self.position[3].set('O')
        elif position[1] == position[7] == 'X' and position[4] == ' ':
            self.position[4].set('O')
        elif position[2] == position[8] == 'X' and position[5] == ' ':
            self.position[5].set('O')
        elif position[0] == position[4] == 'X' and position[8] == ' ':
            self.position[8].set('O')
        elif position[4] == position[8] == 'X' and position[0] == ' ':
            self.position[0].set('O')
        elif position[0] == position[8] == 'X' and position[4] == ' ':
            self.position[4].set('O')
        elif position[2] == position[4] == 'X' and position[6] == ' ':
            self.position[6].set('O')
        elif position[2] == position[6] == 'X' and position[4] == ' ':
            self.position[4].set('O')
        elif position[6] == position[4] == 'X' and position[2] == ' ':
            self.position[2].set('O')

        #If no condition is satisfied then random block is marked O
        else:
            i = 0
            while True:
                i = random.randint(0,8)
                if position[i] == ' ':
                    break
            self.position[i].set('O')
        
        self.player += 1


    #This method checks if anyone has won the game and returns the winner name
    def check(self):
        position = self.position
        conditions = []
        conditions.append([position[0].get() == position[1].get() == position[2].get() 
                            and position[0].get() != ' ', position[0].get()])
        conditions.append([position[0].get() == position[3].get() == position[6].get()
                            and position[0].get() != ' ', position[0].get()])
        conditions.append([position[0].get() == position[4].get() == position[8].get()
                            and position[0].get() != ' ', position[0].get()])
        conditions.append([position[1].get() == position[4].get() == position[7].get()
                            and position[1].get() != ' ', position[1].get()])
        conditions.append([position[2].get() == position[5].get() == position[8].get()
                            and position[2].get() != ' ', position[2].get()])
        conditions.append([position[3].get() == position[4].get() == position[5].get()
                            and position[3].get() != ' ', position[3].get()])
        conditions.append([position[6].get() == position[7].get() == position[8].get()
                            and position[6].get() != ' ', position[6].get()])
        conditions.append([position[2].get() == position[4].get() == position[6].get()
                            and position[2].get() != ' ', position[2].get()])
        
        for item in conditions:
            if item[0] == True:
                return item

        return [False, ' ']


#This is the Frame of Final Window from where you can restart the game
class Winner(ttk.Frame):

    #Constructor for Winner Frame
    def __init__(self, master, winner, position):
        global font1
        super().__init__(master)
        label = ttk.Label(self, text = f'{winner} wins', font = font1)
        label1 = ttk.Label(self, text = 'Do you want to play again?', font = font1)
        button = tk.Button(self, text = 'Play Again', font = font1, bg = 'black',
                            fg = 'white', command = lambda:master.switchframe(StartGame))

        position1 = tk.Label(self, text = position[0],
                                font = font1, width = 3, relief="groove")
        position2 = tk.Label(self, text = position[1], 
                                font = font1, width = 3, relief="groove")
        position3 = tk.Label(self, text = position[2],
                                font = font1, width = 3, relief="groove")
        position4 = tk.Label(self, text = position[3],
                                font = font1, relief="groove")
        position5 = tk.Label(self, text = position[4],
                                font = font1, relief="groove")
        position6 = tk.Label(self, text = position[5],
                                font = font1, relief="groove")
        position7 = tk.Label(self, text = position[6],
                                font = font1, relief="groove")
        position8 = tk.Label(self, text = position[7],
                                font = font1, relief="groove")
        position9 = tk.Label(self, text = position[8],
                                font = font1, relief="groove")
                                
        position1.grid(row = 0, column = 0, sticky = "NSEW")
        position2.grid(row = 0, column = 1, sticky = "NSEW")
        position3.grid(row = 0, column = 2, sticky = "NSEW")
        position4.grid(row = 1, column = 0, sticky = "NSEW")
        position5.grid(row = 1, column = 1, sticky = "NSEW")
        position6.grid(row = 1, column = 2, sticky = "NSEW")
        position7.grid(row = 2, column = 0, sticky = "NSEW")
        position8.grid(row = 2, column = 1, sticky = "NSEW")
        position9.grid(row = 2, column = 2, sticky = "NSEW")

        label.grid(row = 3, column = 0, columnspan = 3)
        label1.grid(row = 4, column = 0, columnspan = 3)
        button.grid(row = 5, column = 0, columnspan = 3)

#Initiating the GUI
app = StartApp()
app.mainloop()