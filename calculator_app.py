import tkinter
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
window=tkinter.Tk()
window.title("Shayaan")
a=tkinter.Entry(window,width=35,borderwidth=5)
a.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
def button_add(number):
    temp=a.get()
    a.delete(0,99)
    a.insert(0,str(temp)+str(number))
def arithmetic(num):
    temp=a.get()
    a.delete(0,99)
    if(num==1):
        a.insert(0,str(temp)+"+")
    elif(num==2):
        a.insert(0,str(temp)+"-")
    elif(num==3):
        a.insert(0,str(temp)+"x")
    elif(num==4):
        a.insert(0,str(temp)+"/")
def equate():
    temp=a.get()
    b=int('1')
    a.delete(0,99)
    i=int('0')
    k=int('0')
    j=len(temp)
    for c in temp[k:]:
        if c=='+' or c=='-' or c=='x' or c=='/' or i==j:
            break
        i=i+1
    num1=int(temp[k:i])
    while i<j:
        ar=temp[i]
        i=i+1
        k=i
        for c in temp[k:]:
            if c=='+' or c=='-' or c=='x' or c=='/' or i==j:
                break
            i=i+1
        num2=int(temp[k:i])
        if ar=='-':
            num1=num1-num2
        elif ar=='+':
            num1=num1+num2
        elif ar=='x':
            num1=num1*num2
        elif ar=='/':
            num1=num1/num2
    if(b==0):
        a.insert(0,'invalid syntax')
    else:
        a.insert(0,str(num1))
def button_clear():
    a.delete(0,99)
button1=tkinter.Button(window,text="1",padx=40,pady=20,command=lambda:button_add(1))
button2=tkinter.Button(window,text="2",padx=40,pady=20,command=lambda:button_add(2))
button3=tkinter.Button(window,text="3",padx=40,pady=20,command=lambda:button_add(3))
button4=tkinter.Button(window,text="4",padx=40,pady=20,command=lambda:button_add(4))
button5=tkinter.Button(window,text="5",padx=40,pady=20,command=lambda:button_add(5))
button6=tkinter.Button(window,text="6",padx=40,pady=20,command=lambda:button_add(6))
button7=tkinter.Button(window,text="7",padx=40,pady=20,command=lambda:button_add(7))
button8=tkinter.Button(window,text="8",padx=40,pady=20,command=lambda:button_add(8))
button9=tkinter.Button(window,text="9",padx=40,pady=20,command=lambda:button_add(9))
button0=tkinter.Button(window,text="0",padx=40,pady=20,command=lambda:button_add(0))
buttonadd=tkinter.Button(window,text="+",padx=40,pady=20,command=lambda:arithmetic(1))
buttonsub=tkinter.Button(window,text="-",padx=40,pady=20,command=lambda:arithmetic(2))
buttonmul=tkinter.Button(window,text="x",padx=40,pady=20,command=lambda:arithmetic(3))
buttondiv=tkinter.Button(window,text="/",padx=40,pady=20,command=lambda:arithmetic(4))
buttonequal=tkinter.Button(window,text="=",padx=90,pady=20,command=lambda:equate())
buttonclear=tkinter.Button(window,text="clear",padx=90,pady=20,command=lambda:button_clear())
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
buttonadd.grid(row=4,column=1)
buttonsub.grid(row=4,column=2)
buttonmul.grid(row=5,column=0)
buttondiv.grid(row=6,column=0)
buttonequal.grid(row=5,column=1,columnspan=2)
buttonclear.grid(row=6,column=1,columnspan=2)
window.mainloop()
