# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:30:00 2020

@author: Shayaan
"""
import tkinter as tk
from tkinter import ttk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)
class InterestCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interest Calculator")
        def simpleint():
            simple=SimpleInterest(self)
            simple.grid(row=0,column=0,rowspan=2)
            self.bind("<Return>",simple.calc)
        def compoundint():
            compound=CompoundInterest(self)
            compound.grid(row=0,column=0,rowspan=2)
            self.bind("<Return>",compound.calc)
        simplebutton=ttk.Button(self,text="Simple Interest",command=simpleint)
        compoundbutton=ttk.Button(self,text="Compound Interest",command=compoundint)
        simplebutton.grid(row=0,column=0,sticky="NEW",padx=5,pady=5)
        compoundbutton.grid(row=1,column=0,sticky="NEW",padx=5,pady=5)
class SimpleInterest(ttk.Frame):
    def __init__(self,container,**kwargs):
        super().__init__(container,**kwargs)
        self.pval=tk.StringVar()
        self.rval=tk.StringVar()
        self.tval=tk.StringVar()
        self.res=tk.StringVar()
        plabel=ttk.Label(self,text="Principle Amount : ")
        pentry=ttk.Entry(self,width=15,textvariable=self.pval)
        rlabel=ttk.Label(self,text="Interest Rate (%) : ")
        rentry=ttk.Entry(self,width=15,textvariable=self.rval)
        tlabel=ttk.Label(self,text="Time (Month) : ")
        tentry=ttk.Entry(self,width=15,textvariable=self.tval)
        reslabel=ttk.Label(self,text="Result : ")
        resdisp=ttk.Label(self,textvariable=self.res)
        calculate=ttk.Button(self,text="Equate",command=self.calc)
        another=ttk.Button(self,text="Select Another Option",command=self.dest)
        plabel.grid(row=1,column=0,padx=5,pady=5,sticky="E")
        pentry.grid(row=1,column=1,padx=5,pady=5,sticky="EW")
        rlabel.grid(row=2,column=0,padx=5,pady=5,sticky="E")
        rentry.grid(row=2,column=1,padx=5,pady=5,sticky="EW")
        tlabel.grid(row=3,column=0,padx=5,pady=5,sticky="E")
        tentry.grid(row=3,column=1,padx=5,pady=5,sticky="EW")
        reslabel.grid(row=4,column=0,padx=5,pady=5,sticky="E")
        resdisp.grid(row=4,column=1,padx=5,pady=5,sticky="EW")
        calculate.grid(row=5,column=0,padx=5,pady=5,sticky="EW")
        another.grid(row=5,column=1,padx=5,pady=5,sticky="EW")
    def calc(self,*args):
        try:
            p=float(self.pval.get())
            r=float(self.rval.get())
            t=float(self.tval.get())
        except:
            self.res.set("Invalid Input")
        else:
            result=p*r*t/100
            self.res.set(f'{result:.3f}')
    def dest(self,*args):
        self.destroy()
class CompoundInterest(ttk.Frame):
    def __init__(self,container,**kwargs):
        super().__init__(container,**kwargs)
        self.res=tk.StringVar()
        self.pval=tk.StringVar()
        self.rval=tk.StringVar()
        self.nval=tk.StringVar()
        self.tval=tk.StringVar()
        plabel=ttk.Label(self,text="Principle Amount : ")
        pentry=ttk.Entry(self,width=20,textvariable=self.pval)
        rlabel=ttk.Label(self,text="Interest Rate (%) : ")
        rentry=ttk.Entry(self,width=20,textvariable=self.rval)
        nlabel=ttk.Label(self,text="Number of payments per year : ")
        nentry=ttk.Entry(self,width=20,textvariable=self.nval)
        tlabel=ttk.Label(self,text="Time (Year) : ")
        tentry=ttk.Entry(self,width=20,textvariable=self.tval)
        reslabel=ttk.Label(self,text="Total Amount : ")
        resdisp=ttk.Label(self,textvariable=self.res)
        calculate=ttk.Button(self,text="Equate",command=self.calc)
        another=ttk.Button(self,text="Select Another Option",command=self.dest)
        plabel.grid(row=1,column=0,padx=5,pady=5,sticky="E")
        pentry.grid(row=1,column=1,padx=5,pady=5,sticky="EW")
        rlabel.grid(row=2,column=0,padx=5,pady=5,sticky="E")
        rentry.grid(row=2,column=1,padx=5,pady=5,sticky="EW")
        nlabel.grid(row=3,column=0,padx=5,pady=5,sticky="E")
        nentry.grid(row=3,column=1,padx=5,pady=5,sticky="EW")
        tlabel.grid(row=4,column=0,padx=5,pady=5,sticky="E")
        tentry.grid(row=4,column=1,padx=5,pady=5,sticky="EW")
        reslabel.grid(row=5,column=0,padx=5,pady=5,sticky="E")
        resdisp.grid(row=5,column=1,padx=5,pady=5,sticky="EW")
        calculate.grid(row=6,column=1,padx=5,pady=5,sticky="EW")
        another.grid(row=6,column=0,padx=5,pady=5,sticky="EW")
    def calc(self,*args):
        try:
            p=float(self.pval.get())
            r=float(self.rval.get())
            t=float(self.tval.get())
            n=float(self.nval.get())
            r=r/100
        except:
            self.res.set("Invalid Input")
        else:
            result=p*((1+(r/n))**(n*t))
            self.res.set(f"{result:.3f}")
    def dest(self,*args):
        self.destroy()
root=InterestCalculator()
root.mainloop()