# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:51:09 2020

@author: Shayaan
"""
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
root=tk.Tk()
font1=font.Font(family="MS Serif",size=12)
font2=font.Font(family="Times New Roman",size=15)

class MainFrame(ttk.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        button1=tk.Button(self,text="Metre to Feet",font=font1,bg='black',fg='white',command=self.mtof)
        button2=tk.Button(self,text="Feet to Metre",font=font1,bg='black',fg='white',command=self.ftom)
        button3=tk.Button(self,text="Centimetre\nto Inch",font=font1,bg='black',fg='white',command=self.ctoi)
        button4=tk.Button(self,text="Inch to\nCentimetre",font=font1,bg='black',fg='white',command=self.itom)
        button5=tk.Button(self,text="Feet to\nKilometre",font=font1,bg='black',fg='white',command=self.ftok)
        button6=tk.Button(self,text="Kilometre\nto Feet",font=font1,bg='black',fg='white',command=self.ktof)
        button7=tk.Button(self,text="Kilometre\nto Mile",font=font1,bg='black',fg='white',command=self.ktom)
        button8=tk.Button(self,text="Mile to\nKilometre",font=font1,bg='black',fg='white',command=self.mtok)
        button9=tk.Button(self,text="Mile to\nNautical Mile",font=font1,bg='black',fg='white',command=self.mton)
        button10=tk.Button(self,text="Nautical Mile\nto Mile",font=font1,bg='black',fg='white',command=self.ntom)
        button1.grid(column=0,row=0,padx=5,pady=5,sticky="NSEW")
        button2.grid(column=1,row=0,padx=5,pady=5,sticky="NSEW")
        button3.grid(column=0,row=1,padx=5,pady=5,sticky="NSEW")
        button4.grid(column=1,row=1,padx=5,pady=5,sticky="NSEW")
        button5.grid(column=0,row=2,padx=5,pady=5,sticky="NSEW")
        button6.grid(column=1,row=2,padx=5,pady=5,sticky="NSEW")
        button7.grid(column=0,row=3,padx=5,pady=5,sticky="NSEW")
        button8.grid(column=1,row=3,padx=5,pady=5,sticky="NSEW")
        button9.grid(column=0,row=4,padx=5,pady=5,sticky="NSEW")
        button10.grid(column=1,row=4,padx=5,pady=5,sticky="NSEW")
        
    def mtof(self):
        def calc():
            m=float(metre.get())
            f=3.28084*m
            feet.set(str(f))
        def back():
            frame_mtof.destroy()
            frame=MainFrame()
            frame.grid(row=0,column=0)
        self.destroy()
        metre=tk.StringVar()
        feet=tk.StringVar()
        frame_mtof=ttk.Frame()
        frame_mtof.grid(row=0,column=0)
        label1=ttk.Label(frame_mtof,text="Metre :",font=font2)
        entry1=ttk.Entry(frame_mtof,textvar=metre,font=font2)
        label2=ttk.Label(frame_mtof,text="Feet :",font=font2)
        disp2=ttk.Label(frame_mtof,textvariable=feet,font=font2)
        equate=tk.Button(frame_mtof,text="Calculate",font=font2,command=calc)
        back=tk.Button(frame_mtof,text="Back to Main Menu",font=font2,command=back)
        label1.grid(row=0,column=0,padx=5,pady=5,sticky="NSE")
        entry1.grid(row=0,column=1,padx=5,pady=5,sticky="NSEW")
        label2.grid(row=1,column=0,padx=5,pady=5,sticky="NSE")
        disp2.grid(row=1,column=1,padx=5,pady=5,sticky="NSW")
        equate.grid(row=2,column=0,padx=5,pady=5,sticky="NSEW")
        back.grid(row=2,column=1,padx=5,pady=5,sticky="NSEW")
        
    def ftom(self):
        def calc():
            f=float(feet.get())
            m=0.3048*f
            metre.set(str(m))
        def back():
            frame_mtof.destroy()
            frame=MainFrame()
            frame.grid(row=0,column=0)
        self.destroy()
        metre=tk.StringVar()
        feet=tk.StringVar()
        frame_mtof=ttk.Frame()
        frame_mtof.grid(row=0,column=0)
        label1=ttk.Label(frame_mtof,text="Feet :",font=font2)
        entry1=ttk.Entry(frame_mtof,textvar=feet,font=font2)
        label2=ttk.Label(frame_mtof,text="Metre :",font=font2)
        disp2=ttk.Label(frame_mtof,textvariable=metre,font=font2)
        equate=tk.Button(frame_mtof,text="Calculate",font=font2,command=calc)
        back=tk.Button(frame_mtof,text="Back to Main Menu",font=font2,command=back)
        label1.grid(row=0,column=0,padx=5,pady=5,sticky="NSE")
        entry1.grid(row=0,column=1,padx=5,pady=5,sticky="NSEW")
        label2.grid(row=1,column=0,padx=5,pady=5,sticky="NSE")
        disp2.grid(row=1,column=1,padx=5,pady=5,sticky="NSW")
        equate.grid(row=2,column=0,padx=5,pady=5,sticky="NSEW")
        back.grid(row=2,column=1,padx=5,pady=5,sticky="NSEW")
        
    def ctoi(self):
        def calc():
            cm1=float(cm.get())
            inch1=cm1*0.393701
            inch.set(str(inch1))
        def back():
            frame_mtof.destroy()
            frame=MainFrame()
            frame.grid(row=0,column=0)
        self.destroy()
        cm=tk.StringVar()
        inch=tk.StringVar()
        frame_mtof=ttk.Frame()
        frame_mtof.grid(row=0,column=0)
        label1=ttk.Label(frame_mtof,text="Centimetre :",font=font2)
        entry1=ttk.Entry(frame_mtof,textvar=cm,font=font2)
        label2=ttk.Label(frame_mtof,text="Inch :",font=font2)
        disp2=ttk.Label(frame_mtof,textvariable=inch,font=font2)
        equate=tk.Button(frame_mtof,text="Calculate",font=font2,command=calc)
        back=tk.Button(frame_mtof,text="Back to Main Menu",font=font2,command=back)
        label1.grid(row=0,column=0,padx=5,pady=5,sticky="NSE")
        entry1.grid(row=0,column=1,padx=5,pady=5,sticky="NSEW")
        label2.grid(row=1,column=0,padx=5,pady=5,sticky="NSE")
        disp2.grid(row=1,column=1,padx=5,pady=5,sticky="NSW")
        equate.grid(row=2,column=0,padx=5,pady=5,sticky="NSEW")
        back.grid(row=2,column=1,padx=5,pady=5,sticky="NSEW")
        
    def itom(self):
        def calc():
            inch1=float(inch.get())
            cm1=inch1*2.54
            cm.set(str(cm1))
        def back():
            frame_mtof.destroy()
            frame=MainFrame()
            frame.grid(row=0,column=0)
        self.destroy()
        cm=tk.StringVar()
        inch=tk.StringVar()
        frame_mtof=ttk.Frame()
        frame_mtof.grid(row=0,column=0)
        label1=ttk.Label(frame_mtof,text="Inch :",font=font2)
        entry1=ttk.Entry(frame_mtof,textvar=inch,font=font2)
        label2=ttk.Label(frame_mtof,text="Centimetre :",font=font2)
        disp2=ttk.Label(frame_mtof,textvariable=cm,font=font2)
        equate=tk.Button(frame_mtof,text="Calculate",font=font2,command=calc)
        back=tk.Button(frame_mtof,text="Back to Main Menu",font=font2,command=back)
        label1.grid(row=0,column=0,padx=5,pady=5,sticky="NSE")
        entry1.grid(row=0,column=1,padx=5,pady=5,sticky="NSEW")
        label2.grid(row=1,column=0,padx=5,pady=5,sticky="NSE")
        disp2.grid(row=1,column=1,padx=5,pady=5,sticky="NSW")
        equate.grid(row=2,column=0,padx=5,pady=5,sticky="NSEW")
        back.grid(row=2,column=1,padx=5,pady=5,sticky="NSEW")
        
    def ftok(self):
        def calc():
            f=float(feet.get())
            km1=0.0003048*f
            km.set(str(km1))
        def back():
            frame_mtof.destroy()
            frame=MainFrame()
            frame.grid(row=0,column=0)
        self.destroy()
        km=tk.StringVar()
        feet=tk.StringVar()
        frame_mtof=ttk.Frame()
        frame_mtof.grid(row=0,column=0)
        label1=ttk.Label(frame_mtof,text="Feet :",font=font2)
        entry1=ttk.Entry(frame_mtof,textvar=feet,font=font2)
        label2=ttk.Label(frame_mtof,text="Kilometre :",font=font2)
        disp2=ttk.Label(frame_mtof,textvariable=km,font=font2)
        equate=tk.Button(frame_mtof,text="Calculate",font=font2,command=calc)
        back=tk.Button(frame_mtof,text="Back to Main Menu",font=font2,command=back)
        label1.grid(row=0,column=0,padx=5,pady=5,sticky="NSE")
        entry1.grid(row=0,column=1,padx=5,pady=5,sticky="NSEW")
        label2.grid(row=1,column=0,padx=5,pady=5,sticky="NSE")
        disp2.grid(row=1,column=1,padx=5,pady=5,sticky="NSW")
        equate.grid(row=2,column=0,padx=5,pady=5,sticky="NSEW")
        back.grid(row=2,column=1,padx=5,pady=5,sticky="NSEW")
        
    def ktof(self):
        def calc():
            km1=float(km.get())
            f=3280.84*km1
            feet.set(str(f))
        def back():
            frame_mtof.destroy()
            frame=MainFrame()
            frame.grid(row=0,column=0)
        self.destroy()
        km=tk.StringVar()
        feet=tk.StringVar()
        frame_mtof=ttk.Frame()
        frame_mtof.grid(row=0,column=0)
        label1=ttk.Label(frame_mtof,text="Kilometre :",font=font2)
        entry1=ttk.Entry(frame_mtof,textvar=km,font=font2)
        label2=ttk.Label(frame_mtof,text="Feet :",font=font2)
        disp2=ttk.Label(frame_mtof,textvariable=feet,font=font2)
        equate=tk.Button(frame_mtof,text="Calculate",font=font2,command=calc)
        back=tk.Button(frame_mtof,text="Back to Main Menu",font=font2,command=back)
        label1.grid(row=0,column=0,padx=5,pady=5,sticky="NSE")
        entry1.grid(row=0,column=1,padx=5,pady=5,sticky="NSEW")
        label2.grid(row=1,column=0,padx=5,pady=5,sticky="NSE")
        disp2.grid(row=1,column=1,padx=5,pady=5,sticky="NSW")
        equate.grid(row=2,column=0,padx=5,pady=5,sticky="NSEW")
        back.grid(row=2,column=1,padx=5,pady=5,sticky="NSEW")
        
    def ktom(self):
        def calc():
            km1=float(km.get())
            m=0.621371*km1
            mile.set(str(m))
        def back():
            frame_mtof.destroy()
            frame=MainFrame()
            frame.grid(row=0,column=0)
        self.destroy()
        km=tk.StringVar()
        mile=tk.StringVar()
        frame_mtof=ttk.Frame()
        frame_mtof.grid(row=0,column=0)
        label1=ttk.Label(frame_mtof,text="Kilometre :",font=font2)
        entry1=ttk.Entry(frame_mtof,textvar=km,font=font2)
        label2=ttk.Label(frame_mtof,text="Mile :",font=font2)
        disp2=ttk.Label(frame_mtof,textvariable=mile,font=font2)
        equate=tk.Button(frame_mtof,text="Calculate",font=font2,command=calc)
        back=tk.Button(frame_mtof,text="Back to Main Menu",font=font2,command=back)
        label1.grid(row=0,column=0,padx=5,pady=5,sticky="NSE")
        entry1.grid(row=0,column=1,padx=5,pady=5,sticky="NSEW")
        label2.grid(row=1,column=0,padx=5,pady=5,sticky="NSE")
        disp2.grid(row=1,column=1,padx=5,pady=5,sticky="NSW")
        equate.grid(row=2,column=0,padx=5,pady=5,sticky="NSEW")
        back.grid(row=2,column=1,padx=5,pady=5,sticky="NSEW")
        
    def mtok(self):
        def calc():
            m=float(mile.get())
            km1=1.60934*m
            km.set(str(km1))
        def back():
            frame_mtof.destroy()
            frame=MainFrame()
            frame.grid(row=0,column=0)
        self.destroy()
        km=tk.StringVar()
        mile=tk.StringVar()
        frame_mtof=ttk.Frame()
        frame_mtof.grid(row=0,column=0)
        label1=ttk.Label(frame_mtof,text="Mile :",font=font2)
        entry1=ttk.Entry(frame_mtof,textvar=mile,font=font2)
        label2=ttk.Label(frame_mtof,text="Kilometre :",font=font2)
        disp2=ttk.Label(frame_mtof,textvariable=km,font=font2)
        equate=tk.Button(frame_mtof,text="Calculate",font=font2,command=calc)
        back=tk.Button(frame_mtof,text="Back to Main Menu",font=font2,command=back)
        label1.grid(row=0,column=0,padx=5,pady=5,sticky="NSE")
        entry1.grid(row=0,column=1,padx=5,pady=5,sticky="NSEW")
        label2.grid(row=1,column=0,padx=5,pady=5,sticky="NSE")
        disp2.grid(row=1,column=1,padx=5,pady=5,sticky="NSW")
        equate.grid(row=2,column=0,padx=5,pady=5,sticky="NSEW")
        back.grid(row=2,column=1,padx=5,pady=5,sticky="NSEW")
        
    def mton(self):
        def calc():
            m=float(mile.get())
            nm=0.868976*m
            naum.set(str(nm))
        def back():
            frame_mtof.destroy()
            frame=MainFrame()
            frame.grid(row=0,column=0)
        self.destroy()
        mile=tk.StringVar()
        naum=tk.StringVar()
        frame_mtof=ttk.Frame()
        frame_mtof.grid(row=0,column=0)
        label1=ttk.Label(frame_mtof,text="Mile :",font=font2)
        entry1=ttk.Entry(frame_mtof,textvar=mile,font=font2)
        label2=ttk.Label(frame_mtof,text="Nautical Mile :",font=font2)
        disp2=ttk.Label(frame_mtof,textvariable=naum,font=font2)
        equate=tk.Button(frame_mtof,text="Calculate",font=font2,command=calc)
        back=tk.Button(frame_mtof,text="Back to Main Menu",font=font2,command=back)
        label1.grid(row=0,column=0,padx=5,pady=5,sticky="NSE")
        entry1.grid(row=0,column=1,padx=5,pady=5,sticky="NSEW")
        label2.grid(row=1,column=0,padx=5,pady=5,sticky="NSE")
        disp2.grid(row=1,column=1,padx=5,pady=5,sticky="NSW")
        equate.grid(row=2,column=0,padx=5,pady=5,sticky="NSEW")
        back.grid(row=2,column=1,padx=5,pady=5,sticky="NSEW")
        
    def ntom(self):
        def calc():
            nm=float(naum.get())
            m=1.15078*nm
            mile.set(str(m))
        def back():
            frame_mtof.destroy()
            frame=MainFrame()
            frame.grid(row=0,column=0)
        self.destroy()
        mile=tk.StringVar()
        naum=tk.StringVar()
        frame_mtof=ttk.Frame()
        frame_mtof.grid(row=0,column=0)
        label1=ttk.Label(frame_mtof,text="Nautical Mile :",font=font2)
        entry1=ttk.Entry(frame_mtof,textvar=naum,font=font2)
        label2=ttk.Label(frame_mtof,text="Mile :",font=font2)
        disp2=ttk.Label(frame_mtof,textvariable=mile,font=font2)
        equate=tk.Button(frame_mtof,text="Calculate",font=font2,command=calc)
        back=tk.Button(frame_mtof,text="Back to Main Menu",font=font2,command=back)
        label1.grid(row=0,column=0,padx=5,pady=5,sticky="NSE")
        entry1.grid(row=0,column=1,padx=5,pady=5,sticky="NSEW")
        label2.grid(row=1,column=0,padx=5,pady=5,sticky="NSE")
        disp2.grid(row=1,column=1,padx=5,pady=5,sticky="NSW")
        equate.grid(row=2,column=0,padx=5,pady=5,sticky="NSEW")
        back.grid(row=2,column=1,padx=5,pady=5,sticky="NSEW")
        
frame1=MainFrame()
frame1.grid(row=0,column=0)
root.mainloop()