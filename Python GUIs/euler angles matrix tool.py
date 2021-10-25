

import tkinter as tk
import numpy as np
import math as m

class EulerGUI:
    def __init__(self):
        self.main_win = tk.Tk()
        self.main_win.title("Euler Angle Matrix Tool")
        
        self.layer1 = tk.Frame(self.main_win)
        self.layer2 = tk.Frame(self.main_win)
        self.layer3 = tk.Frame(self.main_win)
        
        self.var = tk.StringVar()
        self.var.set("")
        
        self.input = tk.Label(self.layer1,
                              text = "Please input your z,y,x degrees: ")
        
        self.yaw_label = tk.Label(self.layer1,
                                  text = "Yaw: ")
        
        self.entry1 = tk.Entry(self.layer1)
        
        self.pitch_label = tk.Label(self.layer1,
                                  text = "Pitch: ")
        
        self.entry2 = tk.Entry(self.layer1)
        
        self.roll_label = tk.Label(self.layer1,
                                  text = "Roll: ")
    
        self.entry3 = tk.Entry(self.layer1)
        
        self.display = tk.Label(self.layer2,
                                textvar = self.var)
        
        self.button = tk.Button(self.layer3,
                                text = "Calculate",
                                command = self.calculate_matrix)
        
        self.quit_button = tk.Button(self.layer3,
                                     text = "Quit",
                                     command = self.main_win.destroy)
        
        self.layer1.pack()
        self.layer2.pack()
        self.layer3.pack()
        
        self.input.pack()
        
        self.yaw_label.pack(side = 'left')
        self.entry1.pack(side = 'left')
        
        self.pitch_label.pack(side = 'left')
        self.entry2.pack(side = 'left')
        
        self.roll_label.pack(side = 'left')
        self.entry3.pack(side = 'left')
        
        self.display.pack()
        self.button.pack()
        self.quit_button.pack()

        tk.mainloop()
    
    def calculate_matrix(self):
        yaw = np.radians(float(self.entry1.get()))
        #print("yaw =", np.round(np.degrees(yaw), decimals = 2))
        
        pitch = np.radians(float(self.entry2.get()))
        #print("pitch =", np.round(np.degrees(pitch), decimals = 2))

        roll = np.radians(float(self.entry3.get()))
        #print("roll =", np.round(np.degrees(roll), decimals = 2))
        
        yawMatr = np.matrix([
                    [m.cos(yaw), -m.sin(yaw), 0],
                    [m.sin(yaw), m.cos(yaw), 0],
                    [0, 0, 1]
                    ])

        pitchMatr = np.matrix([
                    [m.cos(pitch), 0, m.sin(pitch)],
                    [0, 1, 0],
                    [-m.sin(pitch), 0, m.cos(pitch)]
                    ])

        rollMatr = np.matrix([
                    [1, 0, 0],
                    [0, m.cos(roll), -m.sin(roll)],
                    [0, m.sin(roll), m.cos(roll)]
                    ])

        R = yawMatr * pitchMatr * rollMatr
        
        self.var.set(np.round(R, decimals = 4))
        #print(np.round(R, decimals = 4))


if __name__ == "__main__":
    my_gui = EulerGUI()
