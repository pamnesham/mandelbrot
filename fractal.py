
import turtle
from mandelbrot import *

#this class creates the visual aspects of the Mandelbrot
class Display:
    def __init__(self):
        #set up for speed and size of turtle
        turtle.hideturtle()
        turtle.screensize(300, 300)
        turtle.pensize(1)
        turtle.speed(0)
        turtle.tracer(2000, 0)
        turtle.pu()
        turtle.goto(-150, -150)

        #these variables help center and zoom the fractal, keeps track of bounds:
        self.range = 4
        self.centerx = 0
        self.centery = 0
        xcord = -150
        ycord = -150
        realNumber = -2
        imagNumber = -2


        #This draws the fractal pixel by pixel, line by line:
        turtle.pd()
        self.running = True
        while ycord < 150:
            while xcord < 150:
                mcolor = Mandelbrot(Complex(realNumber, imagNumber)).get_color()
                turtle.color(mcolor)
                turtle.goto(xcord+1, ycord)
                xcord = xcord + 1
                realNumber = realNumber + (4/300)
            turtle.pu()
            ycord = ycord + 1
            xcord = -150
            realNumber = -2
            imagNumber = imagNumber + (4/300)
            turtle.goto(xcord, ycord)
            turtle.pd()
        self.running = False
        turtle.listen()
        turtle.onscreenclick(self.click)

    #This function finds the coordinates of user's click and calls zoom
    def click(self, x, y):
        if self.running == False:
            turtle.goto(x, y)
            self.tx = turtle.xcor()
            self.ty = turtle.ycor()
            if self.tx < -150 or self.tx > 150 or self.ty < -150 or self.ty > 150:
                pass
            else:
                turtle.clear()
                self.zoom()

    #Redefine the complex boundaries to zoom in
    def zoom(self):
        self.range = self.range / 2
        self.centerx = ((self.range) * (self.tx/150)) + self.centerx
        self.centery = ((self.range) * (self.ty/150)) + self.centery
        self.realx = self.centerx
        self.imagy = self.centery
        #find starting points for drawing
        self.realx = self.realx - (self.range/2)
        self.imagy = self.imagy - (self.range/2)
        self.draw()


    # Redraw the fractal once zoomed in
    def draw(self):
        xcord = -150
        ycord = -150
        turtle.pu()
        turtle.goto(-150, -150)
        turtle.pd()
        self.running = True
        while ycord < 150:
            while xcord < 150:
                drawmcolor = Mandelbrot(Complex(self.realx, self.imagy)).get_color()
                turtle.color(drawmcolor)
                turtle.goto(xcord+1, ycord)
                xcord = xcord + 1
                self.realx = self.realx + (self.range/300)
            turtle.pu()
            ycord = ycord + 1
            xcord = -150
            #go back to left side of screen:
            self.realx = self.realx - self.range
            self.imagy = self.imagy + (self.range/300)
            turtle.goto(xcord, ycord)
            turtle.pd()
        self.running = False
        turtle.listen()
        turtle.onscreenclick(self.click)


#call all functions to create a Mandelbrot fractal:
def main():
    d = Display()
    turtle.done()

if __name__ == "__main__":
    main()
