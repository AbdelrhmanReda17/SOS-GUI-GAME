from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.messagebox
screen = Tk()
screen.title(" SOS  BY ABDELRHMAN ")

count = 0
player2_score = 0
player1_score = 0
arr=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
clicked = False
arr1=[2,6,10,12,16,20]
char=["A","B","C","D","E","F","J","M","N","K","A","B","C","D","E","F","J","M","N","K"]

def buttonB(temp):
    if temp == 1:
        b1.configure(state=DISABLED)
        b2.configure(state=DISABLED)
        b3.configure(state=DISABLED)
        b4.configure(state=DISABLED)
        b5.configure(state=DISABLED)
        b6.configure(state=DISABLED)
        b7.configure(state=DISABLED)
        b8.configure(state=DISABLED)
        b9.configure(state=DISABLED)
        b10.configure(state=DISABLED)
    else:
        b1.configure(state=NORMAL)
        b2.configure(state=NORMAL)
        b3.configure(state=NORMAL)
        b4.configure(state=NORMAL)
        b5.configure(state=NORMAL)
        b6.configure(state=NORMAL)
        b7.configure(state=NORMAL)
        b8.configure(state=NORMAL)
        b9.configure(state=NORMAL)
        b10.configure(state=NORMAL)

def buttonX(temp):
    if temp == 1:
        x1.configure(state=DISABLED)
        x2.configure(state=DISABLED)
        x3.configure(state=DISABLED)
        x4.configure(state=DISABLED)
        x5.configure(state=DISABLED)
        x6.configure(state=DISABLED)
        x7.configure(state=DISABLED)
        x8.configure(state=DISABLED)
        x9.configure(state=DISABLED)
        x10.configure(state=DISABLED)
    else:
        x1.configure(state=NORMAL)
        x2.configure(state=NORMAL)
        x3.configure(state=NORMAL)
        x4.configure(state=NORMAL)
        x5.configure(state=NORMAL)
        x6.configure(state=NORMAL)
        x7.configure(state=NORMAL)
        x8.configure(state=NORMAL)
        x9.configure(state=NORMAL)
        x10.configure(state=NORMAL)
def b_click(b):
        global count , player,arr ,arr1, clicked,char,temp
        if (clicked == False ):
            count += 1
            temp = 0
            temp = b['text']
            b['text']=char[b['text']]
            clicked = True
            buttonB(1)
            buttonX(2)
def x_click(x):
        global count , player,arr ,arr1, clicked,char,temp1
        if (clicked == True):
            temp1 = 0
            temp1= x['text']
            x['text']=char[x['text']]
            clicked = False
            buttonB(2)
            buttonX(1)

if count in arr1:
    L1=Label(screen, text="PLAYER 1 TURN" , font=("COMIC SANS MS",7,"bold"),height =1,bg="SystemButtonFace")
    L1.grid(row=0, column=0)
else :
    L1=Label(screen, text="PLAYER 2 TURN" , font=("COMIC SANS MS",7,"bold"),height =1,bg="SystemButtonFace")
    L1.grid(row=0, column=0)
         
#BUILD BUTTON AND LABELS !
b1 = Button(screen, text= 1 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b1) )
b2 = Button(screen, text= 2 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b2) )
b3 = Button(screen, text= 3 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b3) )
b4 = Button(screen, text= 4 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b4) )
b5 = Button(screen, text= 5 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b5) )
b6 = Button(screen, text= 6 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b6) )
b7 = Button(screen, text= 7 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b7) )
b8 = Button(screen, text= 8 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b8) )
b9 = Button(screen, text= 9 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b9) )
b10 = Button(screen, text= 10 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b10) )
x1 = Button(screen, text= 11 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: x_click(x1) )
x2 = Button(screen, text= 12 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: x_click(x2) )
x3 = Button(screen, text= 13 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: x_click(x3) )
x4 = Button(screen, text= 14 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: x_click(x4) )
x5 = Button(screen, text= 15 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: x_click(x5) )
x6 = Button(screen, text= 16 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: x_click(x6) )
x7 = Button(screen, text= 17 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: x_click(x7) )
x8 = Button(screen, text= 18 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: x_click(x8) )
x9 = Button(screen, text= 19 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: x_click(x9) )
x10 = Button(screen, text= 20 , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: x_click(x10) )



L1=Label(screen, text="PLAYER 1 TURN" , font=("COMIC SANS MS",7,"bold"),height =1,bg="SystemButtonFace")
L1.grid(row=0, column=0)

L2=Label(screen,text = "[PLAYER 1 = "+ str(player1_score)+"]", font=("COMIC SANS MS",7,"bold"),height =1,bg="SystemButtonFace")
L2.grid(row=0, column=1)
L3=Label(screen,text = "[PLAYER 2 = "+ str(player1_score)+"]", font=("COMIC SANS MS",7,"bold"),height =1,bg="SystemButtonFace")
L3.grid(row=0, column=2)

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=1, column=3)
b5.grid(row=1, column=4)
b6.grid(row=1, column=5)
b7.grid(row=1, column=6)
b8.grid(row=1, column=7)
b9.grid(row=1, column=8)
b10.grid(row=1, column=9)

x1.grid(row=2, column=0)
x2.grid(row=2, column=1)
x3.grid(row=2, column=2)
x4.grid(row=2, column=3)
x5.grid(row=2, column=4)
x6.grid(row=2, column=5)
x7.grid(row=2, column=6)
x8.grid(row=2, column=7)
x9.grid(row=2, column=8)
x10.grid(row=2, column=9)







buttonX(2)
screen.mainloop()
