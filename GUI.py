### CodeFest
##
### Imports
##import tkinter
##
### class definition
##class GUI:
##    def __init__(self):
##    # Main window
##        self.main_window = tkinter.Tk();
##
##    # Create the frame
##        self.grid = tkinter.Frame();
##
##    # Grid for display
##        # Left Column
##        self.header1 = tkinter.Label(self.grid, text = "Speech")
##        self.header1.grid(row = 0, column = 0);
##        self.speech = tkinter.Entry(self.grid, width = 10);
##        self.speech.grid(row = 1, column = 0);
##        
##        # Middle Column
##        self.f_label = tkinter.Label(self.grid, text = "Text Ppt");
##        self.f_label.grid(row = 0, column = 1);
##        self.value = tkinter.StringVar();
##        self.f_output = ScrolledText.Label(self.grid, textvariable = self.value);
##        self.f_output.grid(row = 1, column = 1);
##        
##        # Right Column
##        self.calc_button = tkinter.Label(self.grid, text = "Image");
##        self.calc_button.grid(row = 0, column = 2);
##        #self.quit_button = tkinter.Button(self.grid, text = "Quit", command = self.main_window.destroy);
##        #self.quit_button.grid(row = 1, column = 2);
##        
##    # Pack the frame
##        self.grid.pack();
##
### class instance
##SpeechToText = GUI();

import tkinter as tk
import tkinter.scrolledtext as tkst

win = tk.Tk()
frame1 = tk.Frame(
    master = win,
    bg = '#808000'
)
frame1.pack(fill='both', expand='yes')
editArea = tkst.ScrolledText(
    master = frame1,
    wrap   = tk.WORD,
    width  = 20,
    height = 10
)
# Don't use widget.place(), use pack or grid instead, since
# They behave better on scaling the window -- and you don't
# have to calculate it manually!
editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
# Adding some text, to see if scroll is working as we expect it
editArea.insert(tk.INSERT,
"""\
Integer posuere erat a ante venenatis dapibus.
Posuere velit aliquet.
Aenean eu leo quam. Pellentesque ornare sem.
Lacinia quam venenatis vestibulum.
Nulla vitae elit libero, a pharetra augue.
Cum sociis natoque penatibus et magnis dis.
Parturient montes, nascetur ridiculus mus.
""")
win.mainloop()
