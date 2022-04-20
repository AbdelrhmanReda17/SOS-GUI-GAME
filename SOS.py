from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.messagebox
screen = Tk()
screen.title(" SOS  BY ABDELRHMAN ")

clicked = True
count = 0
player2_score = 0
player1_score = 0

def b_click(b):
    global clicked , count , player
    if b["text"] == "" and clicked == True:
        player1_string = simpledialog.askstring(" SOS [PLAYER 1]","Please enter [S or O] !")
        if (player1_string == "S") or (player1_string == "O"):
                b["text"] = player1_string
                clicked = False
                count += 1
                player = 1
                checkifwin()
                L1 = Label(screen, text="PLAYER 2 TURN" , font=("COMIC SANS MS",7,"bold")).grid(row=0,column=0)
                L3.configure(text=("[PLAYER 2 = "+ str(player2_score)+"]"))
                L3.grid(row=0,column=2)
                L2.configure(text=("[PLAYER 1 = "+ str(player1_score)+"]"))
                L2.grid(row=0,column=1)
        else :
            messagebox.showerror(" SOS  [P1] ","ERROR !!, Please enter [S or O]\n be sure that you make them capital ! ")
            b_click(b)
    elif b["text"] == "" and clicked == False:
        player2_string = simpledialog.askstring(" SOS  [PLAYER 1]","Please enter [S or O] !")
        if (player2_string == "S") or (player2_string == "O"):
                b["text"] = player2_string
                clicked = True
                count += 1
                player = 2
                checkifwin()
                L1 = Label(screen, text="PLAYER 1 TURN" , font=("COMIC SANS MS",7,"bold")).grid(row=0,column=0)
                L3.configure(text=("[PLAYER 2 = "+ str(player2_score)+"]"))
                L3.grid(row=0,column=2)
                L2.configure(text=("[PLAYER 1 = "+ str(player1_score)+"]"))
                L2.grid(row=0,column=1)


        else :
            messagebox.showerror(" SOS [P2] ","ERROR !!, Please enter [S or O]\n be sure that you make them capital ! ")
            b_click(b)

def disabled_all_buttons():
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
    b11.configure(state=DISABLED)
    b12.configure(state=DISABLED)
    b13.configure(state=DISABLED)
    b14.configure(state=DISABLED)
    b15.configure(state=DISABLED)
    b16.configure(state=DISABLED)
    
check1 = False
check2 = False
check3 = False
check4 = False
check5 = False
check6 = False
check7 = False
check8 = False
check9 = False
check10 = False
check11 = False
check12 = False
check13 = False
check14 = False

def checkifwin(): 
    global count,player,player2_score,player1_score
    global check1,check2,check3,check4,check6,check8,check9,check10,check11,check12,check5,check7,check13,check14
    if ((b1["text"] == "S") and (b2["text"] == "O") and (b3["text"] == "S")) and ((b2["text"] == "S") and (b3["text"] =="O") and (b4["text"] == "S")):
            if b2["text"] =="O": 
                b1.config(bg = "red"),b2.config(bg = "red"),b3.config(bg = "red")
            else: 
                b2.config(bg = "red"),b3.config(bg = "red"),b4.config(bg = "red")
            if player == 1 and check1 == False: 
                    player1_score += 1
                    check1 = True
            elif player ==2 and check1 == False:
                    player2_score += 1 
                    check1 = True
            
    if ((b5["text"] == "S") and (b6["text"] == "O") and (b7["text"] == "S")) or ((b6["text"] == "S") and (b7["text"] =="O") and (b8["text"] == "S")):
            if b6["text"] == "O": b5.config(bg = "red"),b6.config(bg = "red"),b7.config(bg = "red")
            else : b6.config(bg = "red"),b7.config(bg = "red"),b8.config(bg = "red") 
            if player == 1 and check2 == False: 
                    player1_score += 1
                    check2 = True
            elif player ==2 and check2 == False:
                    player2_score += 1 
                    check2 = True
                
    if ((b9["text"] == "S") and (b10["text"] == "O") and (b11["text"] == "S")) or ((b10["text"] == "S") and (b11["text"] =="O") and (b12["text"] == "S")):
            if b10["text"] == "O": b9.config(bg = "red"),b10.config(bg = "red"),b11.config(bg = "red")
            else : b10.config(bg = "red"),b11.config(bg = "red"),b12.config(bg = "red") 
            if player == 1 and check3 == False: 
                    player1_score += 1
                    check3 = True
            elif player == 2 and check3 == False:
                    player2_score += 1 
                    check3 = True
                
    if ((b13["text"] == "S") and (b14["text"] == "O") and (b15["text"] == "S")) or ((b14["text"] == "S") and (b15["text"] =="O") and (b16["text"] == "S")):
            if b14["text"] == "O": b13.config(bg = "red"),b14.config(bg = "red"),b15.config(bg = "red")
            else : b14.config(bg = "red"),b15.config(bg = "red"),b16.config(bg = "red") 
            if player == 1 and check4 == False: 
                player1_score += 1
                check4 = True
            elif player == 2 and check4 == False:
                player2_score += 1 
                check4 = True
                
    if ((b1["text"] == "S") and (b5["text"] == "O") and (b9["text"] == "S")) or ((b5["text"] == "S") and (b9["text"] =="O") and (b13["text"] == "S")):
            if b5["text"] == "O": b1.config(bg = "red"),b5.config(bg = "red"),b9.config(bg = "red")
            else : b5.config(bg = "red"),b9.config(bg = "red"),b13.config(bg = "red") 
            if player == 1 and check5 == False: 
                player1_score += 1
                check5 = True
            elif player == 2 and check5 == False:
                player2_score += 1 
                check5 = True
                
    if ((b2["text"] == "S") and (b6["text"] == "O") and (b10["text"] == "S")) or ((b6["text"] == "S") and (b10["text"] =="O") and (b14["text"] == "S")):
            if b6["text"] == "O": b2.config(bg = "red"),b6.config(bg = "red"),b10.config(bg = "red")
            else : b6.config(bg = "red"),b10.config(bg = "red"),b14.config(bg = "red") 
            if player == 1 and check6 == False: 
                player1_score += 1
                check6 = True
            elif player == 2 and check6 == False:
                player2_score += 1 
                check6 = True
                
                
    if ((b3["text"] == "S") and (b7["text"] == "O") and (b11["text"] == "S")) or ((b7["text"] == "S") and (b11["text"] =="O") and (b15["text"] == "S")):
            if b6["text"] == "O": b3.config(bg = "red"),b7.config(bg = "red"),b11.config(bg = "red")
            else : b7.config(bg = "red"),b11.config(bg = "red"),b15.config(bg = "red") 
            if player == 1 and check7 == False: 
                player1_score += 1
                check7 = True
            elif player == 2 and check7 == False:
                player2_score += 1 
                check7 = True
                
    if ((b4["text"] == "S") and (b8["text"] == "O") and (b12["text"] == "S")) or ((b8["text"] == "S") and (b12["text"] =="O") and (b16["text"] == "S")):
            if b8["text"] == "O": b4.config(bg = "red"),b8.config(bg = "red"),b12.config(bg = "red")
            else : b8.config(bg = "red"),b12.config(bg = "red"),b16.config(bg = "red") 
            if player == 1 and check8 == False: 
                player1_score += 1
                check8 = True
            elif player == 2 and check8 == False:
                player2_score += 1 
                check8 = True
                
    if ((b4["text"] == "S") and (b7["text"] == "O") and (b10["text"] == "S")) or ((b7["text"] == "S") and (b10["text"] =="O") and (b13["text"] == "S")):
            if b7["text"] == "O": b4.config(bg = "red"),b7.config(bg = "red"),b10.config(bg = "red")
            else : b7.config(bg = "red"),b10.config(bg = "red"),b13.config(bg = "red") 
            if player == 1 and check9 == False: 
                player1_score += 1
                check9 = True
            elif player == 2 and check9 == False:
                player2_score += 1 
                check9 = True
    if ((b1["text"] == "S") and (b6["text"] == "O") and (b11["text"] == "S")) or ((b6["text"] == "S") and (b11["text"] =="O") and (b16["text"] == "S")):
            if b6["text"] == "O": b1.config(bg = "red"),b6.config(bg = "red"),b11.config(bg = "red")
            else : b6.config(bg = "red"),b11.config(bg = "red"),b16.config(bg = "red") 
            if player == 1 and check10 == False: 
                player1_score += 1
                check10 = True
            elif player == 2 and check10 == False:
                player2_score += 1 
                check10 = True
    if ((b2["text"] == "S") and (b7["text"] == "O") and (b12["text"] == "S")) :
            b2.config(bg = "red"),b7.config(bg = "red"),b12.config(bg = "red")
            if player == 1 and check11 == False: 
                player1_score += 1
                check11 = True
            elif player == 2 and check11 == False:
                player2_score += 1 
                check11 = True
    if (b5["text"] == "S") and (b10["text"] =="O") and (b15["text"] == "S"):
            b5.config(bg = "red"),b10.config(bg = "red"),b15.config(bg = "red")
            if player == 1 and check13 == False: 
                player1_score += 1
                check13 = True
            elif player == 2 and check13 == False:
                player2_score += 1 
                check13 = True 
    if ((b3["text"] == "S") and (b6["text"] == "O") and (b9["text"] == "S")):
            b3.config(bg = "red"),b6.config(bg = "red"),b9.config(bg = "red")
            if player == 1 and check12 == False: 
                player1_score += 1
                check12 = True
            elif player == 2 and check12 == False:
                player2_score += 1 
                check12 = True
    if (b8["text"] == "S") and (b11["text"] =="O") and (b14["text"] == "S"):
            b8.config(bg = "red"),b11.config(bg = "red"),b14.config(bg = "red") 
            if player == 1 and check14 == False: 
                player1_score += 1
                check14 = True
            elif player == 2 and check14 == False:
                player2_score += 1 
                check14 = True
    if (count == 16) and (player1_score == player2_score) :
        messagebox.showinfo("Tic Tac Toe ","GAME DRAW !")
        disabled_all_buttons()
    elif (count ==16) and (player1_score > player2_score):
        messagebox.showinfo("Tic Tac Toe ","PLAYER 1 WIN !")
        disabled_all_buttons()
    elif (count ==16) and (player2_score > player1_score):
        messagebox.showinfo("Tic Tac Toe ","PLAYER 2 WIN !")
        disabled_all_buttons()        

b1 = Button(screen, text ="" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b1) )
b2 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b2) )
b3 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b3) )
b4 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b4) )

b5 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b5) )
b6 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b6) )
b7 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b7) )
b8 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b8) )

b9 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b9) )
b10 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b10) )
b11 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b11) )
b12 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b12) )

b13 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b13) )
b14 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b14) )
b15 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b15) )
b16 = Button(screen, text= "" , font=("Helvetica",20),height =3 , width=6, bg="SystemButtonFace",command=lambda: b_click(b16) )

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

b5.grid(row=2, column=0)
b6.grid(row=2, column=1)
b7.grid(row=2, column=2)
b8.grid(row=2, column=3)

b9.grid(row=3, column=0)
b10.grid(row=3, column=1)
b11.grid(row=3, column=2)
b12.grid(row=3, column=3)

b13.grid(row=4, column=0)
b14.grid(row=4, column=1)
b15.grid(row=4, column=2)
b16.grid(row=4, column=3)


screen.mainloop()
