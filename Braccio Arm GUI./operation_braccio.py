
import tkinter as tk
import serial
import time

def initialize_serial():
    serial_arduino = serial.Serial('COM3', 115200, timeout = 5)
    time.sleep(10)
    print("Arduino is ready.")
    return serial_arduino

serial_arduino = initialize_serial()

class Braccio_OP:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Assignment 3")
        
        self.layer1 = tk.Frame(self.main_window)
        self.layer2 = tk.Frame(self.main_window)
        self.layer3 = tk.Frame(self.main_window)
        self.layer4 = tk.Frame(self.main_window)
        
        self.title = tk.Label(self.layer1,
                              text = "Operation Braccio!")
           
        self.m1_label = tk.Label(self.layer2,
                                 text = "Motor 1")
        
        self.m1_scale = tk.Scale(self.layer2,
                                 from_ = 0,
                                 to = 180,
                                 length = 250,
                                 orient = tk.HORIZONTAL,
                                 command = self.scale_move)
        
        self.m2_label = tk.Label(self.layer2,
                                 text = "Motor 2")
        
        self.m2_scale = tk.Scale(self.layer2,
                                 from_ = 0,
                                 to = 180,
                                 length = 250,
                                 orient = tk.HORIZONTAL,
                                 command = self.scale_move)
        
        self.m3_label = tk.Label(self.layer2,
                                 text = "Motor 3")
        
        self.m3_scale = tk.Scale(self.layer2,
                                 from_ = 0,
                                 to = 180,
                                 length = 250,
                                 orient = tk.HORIZONTAL,
                                 command = self.scale_move)
        
        self.m4_label = tk.Label(self.layer2,
                                 text = "Motor 4")
        
        self.m4_scale = tk.Scale(self.layer2,
                                 from_ = 0,
                                 to = 180,
                                 length = 250,
                                 orient = tk.HORIZONTAL,
                                 command = self.scale_move)
        
        self.m5_label = tk.Label(self.layer2,
                                 text = "Motor 5")
        
        self.m5_scale = tk.Scale(self.layer2,
                                 from_ = 0,
                                 to = 180,
                                 length = 250,
                                 orient = tk.HORIZONTAL,
                                 command = self.scale_move)
        
        self.m6_label = tk.Label(self.layer2,
                                 text = "Motor 6")
        
        self.m6_scale = tk.Scale(self.layer2,
                                 from_ = 0,
                                 to = 90,
                                 length = 250,
                                 orient = tk.HORIZONTAL,
                                 command = self.scale_move)
        
        self.m1_scale.set(90)
        self.m2_scale.set(90)
        self.m3_scale.set(90)
        self.m4_scale.set(90)
        self.m5_scale.set(90)
        self.m6_scale.set(90)
        
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
        a = str(self.m1_scale.get())
        b = str(self.m2_scale.get())
        c = str(self.m3_scale.get())
        d = str(self.m4_scale.get())
        e = str(self.m5_scale.get())
        f = str(self.m6_scale.get())
        
        string = '<' + str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d) + ',' + str(e) + ',' + str(f) + '>'
        print(string)
        serial_arduino.write(string.encode())
        home = serial_arduino.readline().decode('utf-8')
        print(home)
    
    def pos_buttonclick(self):

        if self.radio_var.get() == 1:
            print("User has selected Position 1.")
            self.text_var.set("Position 1")
            self.m1_scale.set(50)
            self.m2_scale.set(100)
            self.m3_scale.set(20)
            self.m4_scale.set(115)
            self.m5_scale.set(40)
            self.m6_scale.set(25)
            
            string = '<50, 100, 20, 115, 40, 25>'
            serial_arduino.write(string.encode())
            pos1 = serial_arduino.readline().decode('utf-8')
            print(pos1)
            
        
        elif self.radio_var.get() == 2:
            print("User has selected Position 2.")
            self.text_var.set("Position 2")
            self.m1_scale.set(80)
            self.m2_scale.set(70)
            self.m3_scale.set(45)
            self.m4_scale.set(10)
            self.m5_scale.set(15)
            self.m6_scale.set(55)
            
            string = '<80, 70, 45, 10, 15, 55>'
            serial_arduino.write(string.encode())
            pos2 = serial_arduino.readline().decode('utf-8')
            print(pos2)
        
        elif self.radio_var.get() == 3:
            print("User has selected Position 3.")
            self.text_var.set("Position 3")
            self.m1_scale.set(170)
            self.m2_scale.set(100)
            self.m3_scale.set(80)
            self.m4_scale.set(90)
            self.m5_scale.set(70)
            self.m6_scale.set(45)
            
            string = '<170, 100, 80, 90, 70, 45>'
            serial_arduino.write(string.encode())
            pos3 = serial_arduino.readline().decode('utf-8')
            print(pos3)
              
    def go_home(self):
        self.text_var.set("Home")
        print("Went home. All motor scales have been reset.")
        
        self.m1_scale.set(90)
        self.m2_scale.set(90)
        self.m3_scale.set(90)
        self.m4_scale.set(90)
        self.m5_scale.set(90)
        self.m6_scale.set(45)

        self.radio_var.set(1)
        
        string = '<90, 90, 90, 90, 90, 90>'
        serial_arduino.write(string.encode())
        home = serial_arduino.readline().decode('utf-8')
        print(home)
    
    def i_quit(self):
        serial_arduino.close()
        print("Arduino Port successfully closed.")
        self.main_window.destroy()

if __name__ == "__main__":
    my_gui = Braccio_OP()