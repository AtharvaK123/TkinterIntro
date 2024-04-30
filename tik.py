from tkinter import *

m = Tk()
m.title("Calculator GUI")
m.state("zoomed")


'''
Label(m, text='Continue?').grid(row=0)
Label(m, text='First Number').grid(row=1)
Label(m, text="Operand")
Label(m, text='Second Number').grid(row=2)

ans = Entry(m)
num1 = Entry(m)
num2 = Entry(m)

ans.grid(row=0, column=1)
num1.grid(row=1, column=1)
num2.grid(row=2, column=1)
'''

top = Frame(m)
bottom = Frame(m)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)
        
text = Text(m, height= 10, width= 80)
text.pack()
text.insert("1.0", "hi")

def enterNumber(): 
    print(1) 
    
one=Button(m, width=20, text="1", command = enterNumber)
two=Button(m, width=20, text="1", command = enterNumber)
one.pack(in_=top, side=LEFT)
two.pack(in_=top, side=LEFT)

m.mainloop()
