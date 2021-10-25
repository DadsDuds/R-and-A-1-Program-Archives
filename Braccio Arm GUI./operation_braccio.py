'''
!!!!! KNOWN ISSUES !!!!!
 1) After the Arduino initializes and the GUI pops up, interacting with any
    of the scales will cause the gripper rotation motor to move first 
    before you are able to move the other scales with their respective motors
    
 2) When changing from one position to another, the arm may choose to return
    to that previous position before moving to the initially selected
    position
    
 3) Yes, I know the scales and motors are out of order, not sure how to
    fix that
'''

import tkinter as tk
import serial
import time


class Braccio_OP:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Assignment 3")
        
        self.serial_arduino = self.initialize_serial()
        
        self.layer1 = tk.Frame(self.main_window)
        self.layer2 = tk.Frame(self.main_window)
        self.layer3 = tk.Frame(self.main_window)
        self.layer4 = tk.Frame(self.main_window)
        
        self.title = tk.Label(self.layer1,
                              text = "Operation Braccio!")
           
        self.m1_label = tk.Label(self.layer2,
                                 text = "Motor 1 - Base")
        
        self.m1_scale = tk.Scale(self.layer2,
                                 from_ = 0,
                                 to = 180,
                                 length = 250,
                                 orient = tk.HORIZONTAL,
                                 command = self.scale_move)
        
        self.m2_label = tk.Label(self.layer2,
                                 text = "Motor 2 - Arm Position")
        
        self.m2_scale = tk.Scale(self.layer2,
                                 from_ = 0,
                                 to = 180,
                                 length = 250,
                                 orient = tk.HORIZONTAL,
                                 command = self.scale_move)
        
        self.m3_label = tk.Label(self.layer2,
                                 text = "Motor 3 - Shoulder")
        
        self.m3_scale = tk.Scale(self.layer2,
                                 from_ = 0,
                                 to = 180,
                                 length = 250,
                                 orient = tk.HORIZONTAL,
                                 command = self.scale_move)
        
        self.m4_label = tk.Label(self.layer2,
                                 text = "Motor 4 - Elbow")
        
        self.m4_scale = tk.Scale(self.layer2,
                                 from_ = 0,
                                 to = 180,
                                 length = 250,
                                 orient = tk.HORIZONTAL,
                                 command = self.scale_move)
        
        self.m5_label = tk.Label(self.layer2,
                                 text = "Motor 5 - Gripper")
        
        self.m5_scale = tk.Scale(self.layer2,
                                 from_ = 20,
                                 to = 90,
                                 length = 250,
                                 orient = tk.HORIZONTAL,
                                 command = self.scale_move)
        
        self.m6_label = tk.Label(self.layer2,
                                 text = "Motor 6 - Gripper Rotation")
        
        self.m6_scale = tk.Scale(self.layer2,
                                 from_ = 10,
                                 to = 73,
                                 length = 250,
                                 orient = tk.HORIZONTAL,
                                 command = self.scale_move)
        
        self.m1_scale.set(90)
        self.m2_scale.set(90)
        self.m3_scale.set(90)
        self.m4_scale.set(90)
        self.m5_scale.set(90)
        self.m6_scale.set(73)
        
        self.title2 = tk.Label(self.layer3,
                               text = "Select your set position:")

        self.radio_var = tk.IntVar()
        self.radio_var.set(1)

        self.text_var = tk.StringVar()
        self.text_var.set("...")
        
        self.rb1 = tk.Radiobutton(self.layer3,
        text = "Position 1",
        variable = self.radio_var,
        value = 1)

        self.rb2 = tk.Radiobutton(self.layer3,
        text = "Position 2",
        variable = self.radio_var,
        value = 2)

        self.rb3 = tk.Radiobutton(self.layer3,
        text = "Position 3",
        variable = self.radio_var,
        value = 3)
        
        self.label = tk.Label(self.layer3,
                              text = "Robot position currently at:")
        
        self.changeable = tk.Label(self.layer3,
                                   textvariable = self.text_var)
        
        self.pos_button = tk.Button(self.layer3,
                                    text = "Change position",
                                    command = self.pos_buttonclick)
        
        self.home_button = tk.Button(self.layer4,
                                     text = "Home",
                                     command = self.go_home)
        
        self.quit_button = tk.Button(self.layer4,
                                     text = "Quit",
                                     command = self.i_quit)
        
        self.layer1.pack()
        self.layer2.pack()
        self.layer3.pack()
        self.layer4.pack()
        
        self.title.pack()
        
        self.m1_label.pack()
        self.m1_scale.pack()
        
        self.m2_label.pack()
        self.m2_scale.pack()
        
        self.m3_label.pack()
        self.m3_scale.pack()
        
        self.m4_label.pack()
        self.m4_scale.pack()
        
        self.m5_label.pack()
        self.m5_scale.pack()
        
        self.m6_label.pack()
        self.m6_scale.pack()
    
        self.title2.pack()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.label.pack()
        self.changeable.pack()
        
        self.pos_button.pack()
        self.home_button.pack(side = "left")
        self.quit_button.pack(side = "left")
        
        tk.mainloop()
    
    def scale_move(self, evt):
        a = self.m1_scale.get()
        b = self.m2_scale.get()
        c = self.m3_scale.get()
        d = self.m4_scale.get()
        e = self.m5_scale.get()
        f = self.m6_scale.get()
        
        string = '<m1,' + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d) + ',' + str(e) + ',' + str(f) + '>'
        print(string)
        
        self.serial_arduino.write(string.encode())
        
        tmp = self.serial_arduino.readline().decode('utf-8')
        print(tmp)
    
    def pos_buttonclick(self):

        if self.radio_var.get() == 1:
            print("User has selected Position 1.")
            self.text_var.set("Position 1")
            self.m1_scale.set(50)
            self.m2_scale.set(100)
            self.m3_scale.set(20)
            self.m4_scale.set(115)
            self.m5_scale.set(45)
            self.m6_scale.set(35)
            
            self.serial_arduino.write('<p1, 50, 100, 20, 115, 40, 25>'.encode())
            
        
        elif self.radio_var.get() == 2:
            print("User has selected Position 2.")
            self.text_var.set("Position 2")
            self.m1_scale.set(80)
            self.m2_scale.set(70)
            self.m3_scale.set(45)
            self.m4_scale.set(10)
            self.m5_scale.set(30)
            self.m6_scale.set(55)
            
            self.serial_arduino.write('<p2, 80, 70, 45, 10, 15, 55>'.encode())

        
        elif self.radio_var.get() == 3:
            print("User has selected Position 3.")
            self.text_var.set("Position 3")
            self.m1_scale.set(170)
            self.m2_scale.set(100)
            self.m3_scale.set(80)
            self.m4_scale.set(90)
            self.m5_scale.set(80)
            self.m6_scale.set(20)
            
            self.serial_arduino.write('<p3, 170, 100, 80, 90, 70, 45>'.encode())

              
    def go_home(self):
        self.text_var.set("Home")
        print("Went home. All motor scales have been reset.")
        
        self.m1_scale.set(90)
        self.m2_scale.set(90)
        self.m3_scale.set(90)
        self.m4_scale.set(90)
        self.m5_scale.set(90)
        self.m6_scale.set(73)

        self.radio_var.set(1)
        
        self.serial_arduino.write('<H, 90, 90, 90, 90, 90, 73>'.encode())

    
    def i_quit(self):
        self.serial_arduino.close()
        print("Arduino Port successfully closed.")
        self.main_window.destroy()
    
    def initialize_serial(self):
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

if __name__ == "__main__":
    my_gui = Braccio_OP()
