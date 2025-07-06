import tkinter
import turtle as t

class SnakeScreen(t.TurtleScreen):

    def __init__(self, *args, width=600, height=600, title="Snake Game", bg="black",**kwargs):


        self.root = tkinter.Tk()
        self.root.title(title)
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()

        # Pass the tkinter Canvas to the TurtleScreen initializer

        super(SnakeScreen,self).__init__(*args, self.canvas, **kwargs)

        # Additional setup

        self.screensize(canvwidth=width, canvheight=height)
        self.bgcolor(bg)

    def start(self):
        self.onscreenclick(self.exit_on_click)

        self.root.mainloop()

    def exit_on_click(self, x, y):
        self.root.destroy()


