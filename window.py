import tkinter as tk
from ppmath import numHandler
# window
class Window:
    def __init__(self):
        self.name = "Visualizer 1.0 Mandelbrot"
        self.math = numHandler()
        self.scrollX = 0
        self.scrollXOld = 0
        self.scrollY = 0
        self.scrollYOld = 0
        self.clicked = False
    def draw(self, x, y, color):
        self.canvas.create_oval(x, y, x, y, fill = color, outline = "red")
    def handle_click(self, event): # draws graph on first click
        if (self.clicked == False):
            self.clicked = True
            for j in range(len(self.math.ImgGrid)):
                for i in range(len(self.math.RealGrid)):
                    if self.math.runMandelbrot(self.math.CompGrid[i][j]) == True:
                        self.draw(i + 200, j + 200, "white")
        # if (event.x > 800 and event.x < 980): # scroll right
        #     # self.scrollXOld = self.scrollX
        #     self.scrollX -= 60
        #     self.canvas.delete("all")
        #     # if (self.scrollX - self.scrollXOld > 0):
        #     #             self.math.range += self.scrollX - self.scrollXOld
        #     #             self.math.runGraph()
        #     # if (self.scrollX - self.scrollXOld < 0):
        #     #         self.math.range -= self.scrollX - self.scrollXOld
        #     for point in self.math.points:
        #         self.draw(point[0] + 500 + self.scrollX, -point[1] + 300 + self.scrollY) 

        # if (event.x > 20 and event.x < 200): # scroll left
        #             # self.scrollXOld = self.scrollX
        #             self.scrollX += 60
        #             self.canvas.delete("all")
        #             # if (self.scrollX - self.scrollXOld > 0):
        #             #             self.math.range += self.scrollX - self.scrollXOld
        #             #             self.math.runGraph()
        #             # if (self.scrollX - self.scrollXOld < 0):
        #             #         self.math.range -= self.scrollX - self.scrollXOld
        #             for point in self.math.points:
        #                 self.draw(point[0] + 500 + self.scrollX, -point[1] + 300 + self.scrollY) 
    # def handle_scroll(self, event):
    #     # self.scrollX += event.delta / 2
    #     self.scrollYOld = self.scrollY
    #     self.scrollY += event.delta // 2
    #     self.canvas.delete("all")
    #     if (self.scrollY - self.scrollYOld > 0):
    #         self.math.range += self.scrollY - self.scrollYOld
    #         self.math.runGraph()
    #     if (self.scrollY - self.scrollYOld < 0):
    #         self.math.range -= self.scrollY - self.scrollYOld
    #     for point in self.math.points:
    #                 self.draw(point[0] + 500 + self.scrollX, -point[1] + 300 + self.scrollY) 
    def start(self):
        root = tk.Tk()
        frm = tk.Frame(root, width=600, height=600) 
        frm.grid()
        root.title(self.name)
        root.bind("<Button-1>", self.handle_click)
        # root.bind("<MouseWheel>", self.handle_scroll)
        root.eval('tk::PlaceWindow . center')
        self.canvas = tk.Canvas(frm, width=600, height=600, bg="black")
        self.canvas.grid()
        root.mainloop()
