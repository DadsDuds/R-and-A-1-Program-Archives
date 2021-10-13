import tkinter as tk

class MarshGUI:
    def __init__(self):
        self.main_win = tk.Tk()
        self.main_win.title('KM to Miles Converter')
        
        self.top_frame = tk.Frame(self.main_win)
        self.middle_frame = tk.Frame(self.main_win)
        self.bottom_frame = tk.Frame(self.main_win)
        
        self.var = tk.StringVar()  # allows the label text to change
        self.var.set("")
        
        self.label1 = tk.Label(self.top_frame,
                              text = "Enter a distance in kilometers:")
        
        self.label2 = tk.Label(self.middle_frame,
                                text = "Converted to miles:")
        
        self.label3 = tk.Label(self.middle_frame,
                                textvar = self.var)
        
        self.label4 = tk.Label(self.middle_frame,
                               text = "miles")
        
        self.my_butt_on = tk.Button(self.bottom_frame,
                                    text = "Convert",
                                    command = self.press_convert)
        
        self.quit_button = tk.Button(self.bottom_frame,
                                      text = "Quit",
                                      command = self.main_win.destroy)
        
        self.entry = tk.Entry(self.top_frame)
        
        # on packs you can set a paramenter such as side = 'left', etc
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        
        self.label1.pack(side = 'left')
        self.entry.pack(side = 'left')
        
        self.label2.pack(side = 'left')
        self.label3.pack(side = 'left')
        self.label4.pack(side = "left")
        
        self.my_butt_on.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        
        tk.mainloop()
    
    def press_convert(self):
        km = float(self.entry.get())
        mi = km * 0.6214
        mi_rounded = round(mi, 2)
        self.var.set(mi_rounded)
        

if __name__ == '__main__':
    my_gui = MarshGUI()