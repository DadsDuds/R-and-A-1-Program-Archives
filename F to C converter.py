import tkinter as tk

class F2C_GUI:
    def __init__(self):
        self.main_win = tk.Tk()
        self.main_win.title('Temp Converter')
        
        self.first_layer = tk.Frame(self.main_win)  # I was considering 4 layers but decided to do 5 for a clean GUI
        self.second_layer = tk.Frame(self.main_win)
        self.third_layer = tk.Frame(self.main_win)
        self.fourth_layer = tk.Frame(self.main_win)
        self.fifth_layer = tk.Frame(self.main_win)
        
        self.var = tk.StringVar()
        self.var.set("Thy answer")  # placeholder text
        
        # first label asks user the following:
        self.first_q = tk.Label(self.first_layer,
                                text = "What conversion type will you be using?")
        
        self.radio_var = tk.IntVar()
        self.radio_var.set(1)
        
        # --- RADIOBUTTONS ---
        self.rb1 = tk.Radiobutton(self.second_layer,
                                        text = "Fahrenheit to Celsius",
                                        variable = self.radio_var,
                                        value = 1)
        
        self.rb2 = tk.Radiobutton(self.second_layer,
                                        text = "Celsius to Fahrenheit",
                                        variable = self.radio_var,
                                        value = 2)
        
        self.label1 = tk.Label(self.third_layer,
                               text = "Enter your temp: ")
        
        # entry box where user will type their temp
        self.entry = tk.Entry(self.third_layer) 
        
        self.label2 = tk.Label(self.fourth_layer,
                               text = "Your converted temp is:")
        
        # --- TEXTVAR ---
        self.label3 = tk.Label(self.fourth_layer,
                               textvar = self.var)
        
        # --- BUTTONS ---
        self.convert_button = tk.Button(self.fifth_layer,
                                        text = "Convert",
                                        command = self.convert_temp)
        
        self.quit_button = tk.Button(self.fifth_layer,
                                     text = "Quit",
                                     command = self.main_win.destroy)
        
        # a whole bunch of packing
        self.first_layer.pack()
        self.second_layer.pack()
        self.third_layer.pack()
        self.fourth_layer.pack()
        self.fifth_layer.pack()
        
        self.first_q.pack(side = 'left')
        
        self.rb1.pack(side = 'left')
        self.rb2.pack(side = 'left')
        
        self.label1.pack(side = 'left')
        self.entry.pack(side = 'left')
        
        self.label2.pack(side = 'left')
        self.label3.pack(side = 'left')
        
        self.convert_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        
        tk.mainloop()   # Can't forget this!
     
        # this function checks if the user has selcted either
        # the first or second radiobutton and if so
        # do their respective conversion equations
        # print lines were used for debugging & confirmation
    def convert_temp(self):
        if self.radio_var.get() == 1:
            answer = float(self.entry.get())
            conv = (answer - 32) / 1.8
            self.var.set(conv)
            print("The user inputted:", answer, "°F and received:", conv, "°C")
            
        elif self.radio_var.get() == 2:
            answer = float(self.entry.get())
            conv = (answer * 1.8) + 32
            self.var.set(conv)
            print("The user inputted:", answer, "°C and received:", conv, "°F")

# Creates an instance of the F2C GUI class       
if __name__ == "__main__":
    my_gui = F2C_GUI()