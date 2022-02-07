# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:49:50 2020

@author: Shayaan
"""


import tkinter as tk
from tkinter import ttk
from ctypes import windll
import pandas as pd
from random import randint,shuffle
import tkinter.font as font
windll.shcore.SetProcessDpiAwareness(1)
root=tk.Tk()
root.geometry("180x170")
myFont=font.Font(size=20)
global i
i=0
words=pd.read_excel('words.xlsx')
listword=words['Test Word']
def wordupdate():
    index=randint(0,len(listword)-1)
    ques=listword[index]
    global ans
    ans=ques
    ques=list(ques)
    shuffle(ques)
    ques=''.join(ques)
    textdisp.set(ques)
    intake.set('')
    if i>0:
        frame.destroy()
def test(*args,**kwargs):
    global frame
    global i
    i=1
    frame=tk.Frame(root)
    frame.grid(row=3,column=0)
    if intake.get() == ans:
        result=ttk.Label(frame,text="Correct!!")
        nex=ttk.Button(frame,text="Next",command=wordupdate)
        result.grid(row=0,column=0,padx=5,pady=5,sticky="EW")
        nex.grid(row=0,column=1,padx=5,pady=5,sticky="EW")
    else:
        result=ttk.Label(frame,text="Incorrect!!")
        result.grid(row=0,column=0,padx=5,pady=5,sticky="EW")
global intake
global textdisp
intake=tk.StringVar()
textdisp=tk.StringVar()
wordupdate()
queslabel=ttk.Label(root,textvariable=textdisp,font=myFont)
ansbox=ttk.Entry(root,textvariable=intake)
submit=ttk.Button(root,text="Submit",command=test)
queslabel.grid(row=0,column=0,padx=5,pady=5)
ansbox.grid(row=1,column=0,padx=5,pady=5,sticky="EW")
submit.grid(row=2,column=0,padx=5,pady=5,sticky="EW")
ansbox.bind('<Return>',test)
root.mainloop()