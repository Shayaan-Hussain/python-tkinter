# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:14:08 2020

@author: Shayaan
"""
import tkinter as tk
from tkinter import ttk
from ctypes import windll
import tkinter.font as font
windll.shcore.SetProcessDpiAwareness(1)
class DistanceConv(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.title("Distance Conversion")
        def choice():
            f_to_m=FeetToMeters(self,padding=(30,15))
            f_to_m.grid(row=0,column=0,columnspan=2)
            self.bind("<Return>",f_to_m.calc)
        def choice1():
            m_to_f=MeterToFeet(self,padding=(30,15))
            m_to_f.grid(row=0,column=0,columnspan=2)
            self.bind("<Return>",m_to_f.calc)
        ftombutton=ttk.Button(self,text="Feet to Meter",command=choice)
        mtofbutton=ttk.Button(self,text="Meter to Feet",command=choice1)
        ftombutton.grid(row=0,column=0,padx=5,pady=5)
        mtofbutton.grid(row=0,column=1,padx=5,pady=5)
class MeterToFeet(ttk.Frame):
    def __init__(self,container,**kwargs):
        super().__init__(container,**kwargs)
        self.fval=tk.StringVar()
        self.mval=tk.StringVar()
        mlabel=ttk.Label(self,text="Meters : ")
        minput=ttk.Entry(self,width=10,textvariable=self.mval,font=("Segoe UI",10))
        flabel=ttk.Label(self,text="Feet : ")
        fdisp=ttk.Label(self,textvariable=self.fval)
        calc=ttk.Button(self,text="Calculate",command=self.calc)
        ftom=ttk.Button(self,text="Select another option",command=self.ftom)
        mlabel.grid(row=0,column=0,padx=5,pady=5,sticky="E")
        minput.grid(row=0,column=1,sticky="EW",padx=5,pady=5)
        flabel.grid(row=1,column=0,padx=5,pady=5,sticky="E")
        fdisp.grid(row=1,column=1,sticky="EW",padx=5,pady=5)
        calc.grid(row=3,column=0,sticky="W",padx=5,pady=5)
        ftom.grid(row=3,column=1,sticky="E",padx=5,pady=5)
    def ftom(self):
        self.destroy()
    def calc(self,*args):
        try:
            m=float(self.mval.get())
            i=m*39.3701
            f=int(i/12)
            i=i-(f*12)
            self.fval.set(f"{f}' {i:.3f}''")
        except ValueError:
            self.fval.set('Invalid Argument')
class FeetToMeters(ttk.Frame):
    def __init__(self,container,**kwargs):
        super().__init__(container,**kwargs)
        self.fval=tk.StringVar()
        self.mval=tk.StringVar()
        flabel=ttk.Label(self,text="Feet : ")
        finput=ttk.Entry(self,width=10,textvariable=self.fval,font=("Segoe UI",10))
        mlabel=ttk.Label(self,text="Meters : ")
        mdisp=ttk.Label(self,textvariable=self.mval)
        calc=ttk.Button(self,text="Calculate",command=self.calc)
        mtof=ttk.Button(self,text="Select another option",command=self.mtof)
        flabel.grid(row=0,column=0,padx=5,pady=5,sticky="E")
        finput.grid(row=0,column=1,sticky="EW",padx=5,pady=5)
        mlabel.grid(row=1,column=0,padx=5,pady=5,sticky="E")
        mdisp.grid(row=1,column=1,sticky="EW",padx=5,pady=5)
        calc.grid(row=3,column=0,sticky="W",padx=5,pady=5)
        mtof.grid(row=3,column=1,sticky="E",padx=5,pady=5)
    def mtof(self):
        self.destroy()
    def calc(self,*args):
        try:
            f=float(self.fval.get())
            m=f/3.28084
            self.mval.set(f"{m:.3f}")
        except ValueError:
            self.mval.set('Invalid Argument')
app=DistanceConv()
font.nametofont("TkDefaultFont").configure(size=10)
app.mainloop()