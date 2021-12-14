# Marshall Sullivan
# ENGN 4075 - Robotics & Automation
# Final Project

import tkinter as tk
import serial
import time

# we'll need these two for later
count = 0
board=[['','','',],
           ['','','',],
           ['','','',]]


class TTT:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Tic-Tac-Toe")
        
        self.serial_arduino = self.initialize_serial()
        
        self.C_Layer = tk.Frame(self.main_window)
        self.D_Layer = tk.Frame(self.main_window)
        self.RT = tk.Frame(self.main_window)
        self.Q_Layer = tk.Frame(self.main_window)
        self.HT = tk.Frame(self.main_window)
        self.H_Layer = tk.Frame(self.main_window)
        self.QQ_Layer = tk.Frame(self.main_window)
        
        self.radio_var = tk.IntVar()
        self.radio_var.set(1)
        self.test = tk.StringVar()
        self.test.set("")
        
        self.Title = tk.Label(self.C_Layer,
                                text = "Tic-Tac-Toe")
        
        self.Question = tk.Label(self.C_Layer,
                                text = "What will the robot be playing as?")
        
        self.RButton1 = tk.Radiobutton(self.D_Layer,
                                        text = "X",
                                        variable = self.radio_var,
                                        value = 1)
        
        self.RButton2 = tk.Radiobutton(self.D_Layer,
                                        text = "O",
                                        variable = self.radio_var,
                                        value = 2)
        
        self.ConfirmButton = tk.Button(self.D_Layer,
                                        text = "Confirm selection",
                                        command = self.confirmation)
        
        self.Grabber = tk.Button(self.D_Layer,
                                 text = "Grab Block",
                                 command = self.grabBlock)
        
        self.R_Title = tk.Label(self.RT, text = "Robot's Move")
        
        self.b1=tk.Button(self.Q_Layer, text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.Top_L)
        self.b2=tk.Button(self.Q_Layer,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.Top_M)
        self.b3=tk.Button(self.Q_Layer,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.Top_R)
        self.b4=tk.Button(self.Q_Layer,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.Middle_L)
        self.b5=tk.Button(self.Q_Layer,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.Middle)
        self.b6=tk.Button(self.Q_Layer,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.Middle_R)
        self.b7=tk.Button(self.Q_Layer,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.Bottom_L)
        self.b8=tk.Button(self.Q_Layer,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.Bottom_M)
        self.b9=tk.Button(self.Q_Layer,text="",height=4,width=8,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.Bottom_R)

        self.b1.grid(row=2,column=0)
        self.b2.grid(row=2,column=1)
        self.b3.grid(row=2,column=2)

        self.b4.grid(row=3,column=0)
        self.b5.grid(row=3,column=1)
        self.b6.grid(row=3,column=2)

        self.b7.grid(row=4,column=0)
        self.b8.grid(row=4,column=1)
        self.b9.grid(row=4,column=2)
     
        self.H_Title = tk.Label(self.HT, text = "Human's Move - only use this when a human opponent has made a move")
        
        self.hb1=tk.Button(self.H_Layer, text="",height=2,width=4,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.HTop_L)
        self.hb2=tk.Button(self.H_Layer,text="",height=2,width=4,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.HTop_M)
        self.hb3=tk.Button(self.H_Layer,text="",height=2,width=4,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.HTop_R)
        self.hb4=tk.Button(self.H_Layer,text="",height=2,width=4,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.HMiddle_L)
        self.hb5=tk.Button(self.H_Layer,text="",height=2,width=4,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.HMiddle)
        self.hb6=tk.Button(self.H_Layer,text="",height=2,width=4,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.HMiddle_R)
        self.hb7=tk.Button(self.H_Layer,text="",height=2,width=4,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.HBottom_L)
        self.hb8=tk.Button(self.H_Layer,text="",height=2,width=4,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.HBottom_M)
        self.hb9=tk.Button(self.H_Layer,text="",height=2,width=4,bg="black",activebackground="white",fg="white",font="Times 15 bold",command = self.HBottom_R)
     
        self.hb1.grid(row=2,column=0)
        self.hb2.grid(row=2,column=1)
        self.hb3.grid(row=2,column=2)

        self.hb4.grid(row=3,column=0)
        self.hb5.grid(row=3,column=1)
        self.hb6.grid(row=3,column=2)

        self.hb7.grid(row=4,column=0)
        self.hb8.grid(row=4,column=1)
        self.hb9.grid(row=4,column=2)   
     
        self.resetboard = tk.Button(self.QQ_Layer,
                                    text = "Reset Board",
                                    command = self.resettheboard)
        
        self.i_quit = tk.Button(self.QQ_Layer,
                                text = "Quit",
                                command = self.i_quit)
        
        self.C_Layer.pack()
        self.D_Layer.pack()
        self.RT.pack()
        self.Q_Layer.pack()
        self.HT.pack()
        self.H_Layer.pack()
        self.QQ_Layer.pack()
        
        self.Title.pack()
        self.Question.pack()
        self.RButton1.pack()
        self.RButton2.pack()
        self.ConfirmButton.pack()
        self.Grabber.pack()
        self.R_Title.pack()
        self.H_Title.pack()
        
        self.resetboard.pack()
        self.i_quit.pack()
        
        tk.mainloop()
    
    def checkMove(self, row, col):
        # this function checks if an X or O should be added in
        # a button's row/col coords
        global count
        
        if self.radio_var.get() == 1:
            board[row][col] = "X"
            count = count + 1
        
        if self.radio_var.get() == 2:
            board[row][col] = "O"
            count = count + 1
        
        if count >= 5:
            self.checkWinner()
        
        print(board)
       
    def checkWinner(self):
        # this function checks if any of the winning conditions
        # have been reached (row, column, diagonal)
        global count, board

        if self.radio_var.get() == 1:
            
            if (board[0][0]==board[0][1]==board[0][2]=="X"
                or board[1][0]==board[1][1]==board[1][2]=="X"
                or board[2][0]==board[2][1]==board[2][2]=="X"
                or board[0][0]==board[1][0]==board[2][0]=="X"
                or board[0][1]==board[1][1]==board[2][1]=="X"
                or board[0][2]==board[1][2]==board[2][2]=="X"
                or board[0][0]==board[1][1]==board[2][2]=="X"
                or board[0][2]==board[1][1]==board[2][0]=="X"):
                self.displayWinner("Player X")

                
        if self.radio_var.get() == 2:    
            if (board[0][0]==board[0][1]==board[0][2]=="O"
                or board[1][0]==board[1][1]==board[1][2]=="O"
                or board[2][0]==board[2][1]==board[2][2]=="O"
                or board[0][0]==board[1][0]==board[2][0]=="O"
                or board[0][1]==board[1][1]==board[2][1]=="O"
                or board[0][2]==board[1][2]==board[2][2]=="O"
                or board[0][0]==board[1][1]==board[2][2]=="O"
                or board[0][2]==board[1][1]==board[2][0]=="O"):
                self.displayWinner("Player O")
                
                    
        elif count >= 9:
            self.displayWinner("Tie")
        
    def displayWinner(self, winner):   
        # This function determines who wins the game
        # It also determines if the bot was playing either X or O
        global isBotPlayingX, isBotPlayingO
        #print(winner)
        
        if winner == "Player X":
            if isBotPlayingX == True:
                print("Braccio won!")
                self.serial_arduino.write('<W>'.encode())
                
            else:
                print("You have beaten the robot!")
                self.serial_arduino.write('<L>'.encode())
                
                
        if winner == "Player O":
            if isBotPlayingO == True:
                print("Braccio won!")
                self.serial_arduino.write('<W>'.encode())
                
            else:
                print("You have beaten the robot!")
                self.serial_arduino.write('<L>'.encode())
        
        
        elif winner == "Tie":
            print("Stalemate!")
                
## ------ ROBOT MOVES ----- ##        
    def Top_L(self):
       self.serial_arduino.write('<TL>'.encode())
       self.checkMove(0, 0)        
    
    def Top_M(self):
        self.serial_arduino.write('<TM>'.encode())
        self.checkMove(0, 1)
    
    def Top_R(self):
        self.serial_arduino.write('<TR>'.encode())
        self.checkMove(0, 2)
    
    def Middle_L(self):
        self.serial_arduino.write('<ML>'.encode())
        self.checkMove(1, 0)
    
    def Middle(self):
        self.serial_arduino.write('<M>'.encode())
        self.checkMove(1, 1)
    
    def Middle_R(self):
        self.serial_arduino.write('<MR>'.encode())
        self.checkMove(1, 2)
    
    def Bottom_L(self):
        self.serial_arduino.write('<BL>'.encode())
        self.checkMove(2, 0)
    
    def Bottom_M(self):
        self.serial_arduino.write('<BM>'.encode())
        self.checkMove(2, 1)
    
    def Bottom_R(self):
        self.serial_arduino.write('<BR>'.encode())
        self.checkMove(2, 2)  
     
## ----- HUMAN MOVES ----- ##        
    def HTop_L(self):
       
       self.checkMove(0, 0)
    
    def HTop_M(self):
        
        self.checkMove(0, 1)
        
    def HTop_R(self):
        
        self.checkMove(0, 2)
    
    def HMiddle_L(self):
        
        self.checkMove(1, 0)
    
    def HMiddle(self):
        
        self.checkMove(1, 1)
    
    def HMiddle_R(self):
        
        self.checkMove(1, 2)
    
    def HBottom_L(self):
        
        self.checkMove(2, 0)
    
    def HBottom_M(self):
        
        self.checkMove(2, 1)
    
    def HBottom_R(self):
        
        self.checkMove(2, 2) 
            
                

    def confirmation(self):
        # This function tells Python that the bot is either
        # playing as X or O and will be neede for displayWinner()
        global isBotPlayingX, isBotPlayingO
        
        if self.radio_var.get() == 1:
            print("Braccio will play as X!")
            isBotPlayingX = True
            isBotPlayingO = False
            
        
        if self.radio_var.get() == 2:
            print("Braccio will play as O!")
            isBotPlayingO = True
            isBotPlayingX = False
            

    def grabBlock(self):
        # this just sends parse data to Arduino to grab a block
        # this'll work regardless of X or O block
        if self.radio_var.get() == 1:
            self.serial_arduino.write('<X>'.encode())
        
        if self.radio_var.get() == 2:
            self.serial_arduino.write('<X>'.encode())
    
    
    def initialize_serial(self):    # readys the Arduino port
        try:
            self.serial_arduino = serial.Serial("COM3", 115200, timeout = 2)
            time.sleep(10)
            self.serial_arduino.write('<i, 0, 0, 0, 0, 0, 0>'.encode())
            tmp = self.serial_arduino.readline().decode('utf-8')
            print(tmp)
            
            if tmp == 'Ready!\r\n':
                print("Arduino is ready.")
                return self.serial_arduino
            
            else:
                return False
        
        except serial.serialutil.SerialException:
            print("Serial error.")
    
    def resettheboard(self):
        # this functions resets the board and move counter
        global count, board
        board[0][0] = ""
        board[0][1] = ""
        board[0][2] = ""
        board[1][0] = ""
        board[1][1] = ""
        board[1][2] = ""
        board[2][0] = ""
        board[2][1] = ""
        board[2][2] = ""

        count = 0
        print(board)
    

    def i_quit(self):   # quit function
        self.serial_arduino.close()
        print("Arduino Port successfully closed.")
        self.main_window.destroy()

if __name__ == "__main__":
    my_gui = TTT()