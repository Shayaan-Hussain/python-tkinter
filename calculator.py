import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import math

#Initializing tkinter root window and font
root = tk.Tk()
root.title('Calculator')
font1 = font.Font(family="Times New Roman", size=15)

#Defining Class for calculator Frame
class Calculator(ttk.Frame):

    #Defining the Constructor
    def __init__(self, master):
        super().__init__(master)

        #Initializing Buttons and Entry Field
        self.entry = ttk.Entry(self, font = font1)
        buttoncalc = tk.Button(self, text = "=", font = font1, bg = 'black', fg = 'white', command = self.calc)
        buttonclr = tk.Button(self, text = "AC", font = font1, bg = 'black', fg = 'white', command = self.clear)
        buttonerase = tk.Button(self, text = "<-", font = font1, bg = 'black', fg = 'white', command = self.erase)
        button1 = tk.Button(self, text = "1", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(1))
        button2 = tk.Button(self, text = "2", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(2))
        button3 = tk.Button(self, text = "3", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(3))
        button4 = tk.Button(self, text = "4", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(4))
        button5 = tk.Button(self, text = "5", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(5))
        button6 = tk.Button(self, text = "6", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(6))
        button7 = tk.Button(self, text = "7", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(7))
        button8 = tk.Button(self, text = "8", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(8))
        button9 = tk.Button(self, text = "9", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(9))
        button0 = tk.Button(self, text = "0", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(0))
        buttonbop = tk.Button(self, text = "(", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('('))
        buttonbcl = tk.Button(self, text = ")", font = font1, bg = 'black', fg = 'white', command = lambda : self.update(')'))
        buttonadd = tk.Button(self, text = "+", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('+'))
        buttonsub = tk.Button(self, text = "-", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('-'))
        buttonmul = tk.Button(self, text = "x", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('x'))
        buttondiv = tk.Button(self, text = "/", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('/'))
        buttonpow = tk.Button(self, text = "^", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('^'))
        buttondot = tk.Button(self, text = ".", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('.'))
        buttonper = tk.Button(self, text = "%", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('%'))
        buttonsqrt = tk.Button(self, text = "√", font = font1, bg = 'black', fg = 'white', command = lambda : self.update('√'))

        #Placing Buttons and Entry Field on the Grid
        self.entry.grid(row = 0, column = 0, columnspan = 4, sticky = "NSEW")
        button1.grid(row = 1, column = 0, sticky = "NSEW")
        button2.grid(row = 1, column = 1, sticky = "NSEW")
        button3.grid(row = 1, column = 2, sticky = "NSEW")
        buttonclr.grid(row = 1, column = 3, sticky = "NSEW")
        button4.grid(row = 2, column = 0, sticky = "NSEW")
        button5.grid(row = 2, column = 1, sticky = "NSEW")
        button6.grid(row = 2, column = 2, sticky = "NSEW")
        buttonerase.grid(row = 2, column = 3, sticky = "NSEW")
        button7.grid(row = 3, column = 0, sticky = "NSEW")
        button8.grid(row = 3, column = 1, sticky = "NSEW")
        button9.grid(row = 3, column = 2, sticky = "NSEW")
        buttonadd.grid(row = 3, column = 3, sticky = "NSEW")
        buttondot.grid(row = 4, column = 0, sticky = "NSEW")
        button0.grid(row = 4, column = 1, sticky = "NSEW")
        buttonsqrt.grid(row = 4, column = 2, sticky = "NSEW")
        buttonsub.grid(row = 4, column = 3, sticky = "NSEW")
        buttonbop.grid(row = 5, column = 0, sticky = "NSEW")
        buttonbcl.grid(row = 5, column = 1, sticky = "NSEW")
        buttonpow.grid(row = 5, column = 2, sticky = "NSEW")
        buttondiv.grid(row = 5, column = 3, sticky = "NSEW")
        buttoncalc.grid(row = 6, column = 0, columnspan = 3, sticky = "NSEW")
        buttonmul.grid(row = 6, column = 3, sticky = "NSEW")

        #Binding the Enter key to Calculate function
        master.bind('<Return>', self.calc)


    #Method to clear the Entry Field
    def clear(self):
        self.entry.delete(0, 99)


    #Method to update content on Entry Field
    def update(self, char):
        temp = len(str(self.entry.get()))
        self.entry.insert(temp, str(char))


    #Method to erase last element of Entry Field
    def erase(self):
        temp = len(str(self.entry.get()))
        self.entry.delete(temp - 1)
    

    #Method to evaluate Arithmetic Expression
    #Note that the evaluation is done based on precedence order
    def evaluate(self, exp):
        
        i = 0
        exp1 = exp
        exp = []
        while i < len(exp1):
            if i < len(exp1) - 2 and str(exp1[i]) == '√':
                exp.append(math.sqrt(exp1[i+1]))
                i += 2
            else:
                exp.append(exp1[i])
                i += 1

        i = 0
        exp1 = exp
        exp = []
        while i < len(exp1):
            if i < len(exp1) - 2 and str(exp1[i+1]) == '^':
                exp.append(exp1[i] ** exp1[i+2])
                i += 3
            else:
                exp.append(exp1[i])
                i += 1

        i = 0
        exp1 = []
        while i < len(exp):
            if i < len(exp) - 2 and str(exp[i+1]) == 'x':
                exp1.append(exp[i] * exp[i+2])
                i += 3
            else:
                exp1.append(exp[i])
                i += 1
            
        i = 0
        exp = []
        while i < len(exp1):
            if i < len(exp1) - 2 and str(exp1[i+1]) == '/':
                exp.append(exp1[i] / exp1[i+2])
                i += 3
            else:
                exp.append(exp1[i])
                i += 1

        i = 1
        result = exp[0]
        while i < len(exp):
            if exp[i] == '+':
                result += exp[i+1]
            elif exp[i] == '-':
                result -= exp[i+1]
            i += 2
        
        return result


    #Method that splits Entry string into list and passes it to evaluate function
    def calc(self, *args):
        arithmetic = ['-', '+', 'x', '/', '^', '√']
        brackets = ['(', ')']
        expression = str(self.entry.get())
        charlist = [expression[i] for i in range(len(expression))]

        #Cancel Evaluation if expression is invalid
        if charlist[-1] in arithmetic or len(charlist) == 0:
            self.entry.delete(0, 99)
            self.entry.insert(0, 'Syntax Error')
            pass

        else:
            #Combine integers and separate by arithmetic expressions
            exp = []
            i = 0
            while i < len(charlist):
                if charlist[i] in arithmetic or charlist[i] in brackets or charlist[i] == '.':
                    exp.append(charlist[i])
                    i += 1
                elif charlist[i] == ' ':
                    i += 1
                    continue
                else:
                    n = 0
                    while i < len(charlist) and charlist[i] not in arithmetic and charlist[i] not in brackets and charlist[i] != '.':
                        if charlist[i] == ' ':
                            i += 1
                            continue
                        n = (n * 10) + int(charlist[i])
                        i += 1
                    exp.append(n)

            #Converting Integers to Float where necessary
            i = 0
            exp1 = []
            while i < len(exp):
                if exp[i] == '.':
                    exp1[len(exp1)-1] = float(f'{str(exp[i-1])}{exp[i]}{str(exp[i+1])}')
                    i += 2
                else:
                    exp1.append(exp[i])
                    i += 1
            exp = exp1

            if exp[0] in arithmetic and exp[0] != '√':
                exp1 = exp
                exp = []
                exp.append(0)
                for i in exp1:
                    exp.append(i)

            #Find and evaluate peranthesis first
            i = 0
            length = len(exp)
            while i < length:
                exp1 = []
                if str(exp[i]) == '(': 
                    j = i + 1
                    while str(exp[j]) != ')':
                        exp1.append(exp[j])
                        j += 1
                    result = self.evaluate(exp1)
                    k = 0
                    exp1 = []
                    while k < len(exp):
                        if k == i:
                            k = j
                            exp1.append(result)
                        else:
                            exp1.append(exp[k])
                            k += 1
                    exp = exp1
                    i = length - j
                    length = len(exp)
                else:
                    i += 1
            
            #Evaluate the final list of expressions
            result = self.evaluate(exp)

            #Assign the result and display on the Entry Field
            self.entry.delete(0, 99)
            self.entry.insert(0, str(result))

#Declare a variable of Calculator Class and display it on root window
calculator = Calculator(root)
calculator.grid(row = 0, column = 0)

#Keep the root window running till program is closed
root.mainloop()