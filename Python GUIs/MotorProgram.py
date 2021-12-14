import tkinter as tk
import serial
import time

class Motor_GUI:
    def __init__(self):
        self.mw = tk.Tk()
        self.mw.title("Assignment 9")
        
        self.whatisit = tk.StringVar()
        self.whatisit.set("")
        self.whereitgoin = tk.StringVar()
        self.whereitgoin.set("")
        
        self.serial_arduino = self.initialize_serial()
        
        self.en_frame = tk.Frame(self.mw)
        self.cc_frame = tk.Frame(self.mw)
        self.slide_frame = tk.Frame(self.mw)
        self.quit_frame = tk.Frame(self.mw)
        
        self.en_title = tk.Label(self.en_frame,
                                 text = "Enable/Disable Motor")
        
        self.en_button = tk.Button(self.en_frame,
                                   text = "Enable",
                                   command = self.turn_on)
        
        self.dis_button = tk.Button(self.en_frame,
                                    text = "Disable",
                                    command = self.turn_off)
        
        self.motorcheck = tk.Label(self.en_frame,
                                   text = "Motor:")
        
        self.labelvar1 = tk.Label(self.en_frame,
                                 textvar = self.whatisit)
        
        self.cc_title = tk.Label(self.cc_frame,
                                 text = "Choose a Clockwise")
        
        self.cw_button = tk.Button(self.cc_frame,
                                   text = "Go CCW",
                                   command = self.go_cw)
        
        self.ccw_button = tk.Button(self.cc_frame,
                                    text = "Go CW",
                                    command = self.go_ccw)
        
        self.clockcheck = tk.Label(self.cc_frame,
                                   text = "Motor is currently going:")
        
        self.labelvar2 = tk.Label(self.cc_frame,
                                  textvar = self.whereitgoin)
        
        self.slide_title = tk.Label(self.slide_frame,
                                    text = "Configure Motor Speed")
        
        self.speed = tk.Scale(self.slide_frame,
                              from_ = 0,
                              to = 255,
                              length = 250,
                              orient = tk.HORIZONTAL,
                              command = self.scale_move)
        
        self.quit_button = tk.Button(self.quit_frame,
                                     text = "Quit",
                                     command = self.i_quit)
        
        self.en_frame.pack()
        self.cc_frame.pack()
        self.slide_frame.pack()
        self.quit_frame.pack()
        
        self.en_title.pack()
        self.en_button.pack(side = "left")
        self.dis_button.pack(side = "left")
        self.motorcheck.pack(side = "left")
        self.labelvar1.pack()
        
        self.cc_title.pack()
        self.cw_button.pack()
        self.ccw_button.pack()
        self.clockcheck.pack()
        
        self.slide_title.pack(side = "left")
        self.speed.pack()
        self.speed.set(125)
        
        self.labelvar2.pack()
        self.quit_button.pack()
        
        tk.mainloop()
    
    def turn_on(self):
        self.whatisit.set("Enabled")
        self.serial_arduino.write('<e>'.encode())
        
    def turn_off(self):
        self.whatisit.set("Disabled")
        self.serial_arduino.write('<d>'.encode())
    
    def scale_move(self, evt):
        a = self.speed.get()
        string = '<s,' + str(a) + '>'
        self.serial_arduino.write(string.encode())
        
        tmp = self.serial_arduino.readline().decode('utf-8')
        print(tmp)
    
    def go_cw(self):
        self.whereitgoin.set("Clockwise")
        self.serial_arduino.write('<C>'.encode())
    
    def go_ccw(self):
        self.whereitgoin.set("Counterclockwise")
        self.serial_arduino.write('<CW>'.encode())
    
    def initialize_serial(self):
        try:
            self.serial_arduino = serial.Serial("COM3", 115200, timeout = 2)
            time.sleep(10)
            self.serial_arduino.write('<i, 0>'.encode())
            tmp = self.serial_arduino.readline().decode('utf-8')
            print(tmp)
            
            if tmp == 'Ready!\r\n':
                print("Arduino is ready.")
                return self.serial_arduino
            
            else:
                return False
        
        except serial.serialutil.SerialException:
            print("Serial error.")
    
    def i_quit(self):
        self.serial_arduino.close()
        print("Arduino Port successfully closed.")
        self.mw.destroy()

if __name__ == "__main__":
    my_gui = Motor_GUI()
