import tkinter as tk

# window
class Window:
    def __init__(self):
        self.name = "Visualizer 1.0 Mandelbrot"
    def start(self):
        root = tk.Tk()
        frm = tk.Frame(root, width=1000, height=600) 
        frm.grid()
        root.title(self.name)
        root.mainloop()
