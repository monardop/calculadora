from tkinter import *
from matplotlib.pyplot import text

from numpy import multiply, number

class App(Frame):
    def __init__(self):
        super().__init__()
        self. initUI()
    
    def initUI(self):
        self.master.title("Calculadora")
        self.master.config(padx=20, pady=20)

        number = Label(self, width= 400, text="Hola, soy un texto de prueba")
        
        area1 = Frame(self) #this area is going to have the numbers
        
        nro0 = Button(area1, text="0")
        nro1 = Button(area1, text="1")
        nro2 = Button(area1, text="2")
        nro3 = Button(area1, text="3")
        nro4 = Button(area1, text="4")
        nro5 = Button(area1, text="5")
        nro6 = Button(area1, text="6")
        nro7 = Button(area1, text="7")
        nro8 = Button(area1, text="8")
        nro9 = Button(area1, text="9")
        point = Button(area1, text="·")
        equal = Button(area1, text="=")
        
        nro0.grid(column=0,row=3)
        point.grid(column=1,row=3)
        equal.grid(column=2,row=3)
        nro1.grid(column=0,row=2)
        nro2.grid(column=1,row=2)
        nro3.grid(column=2,row=2)
        nro4.grid(column=0,row=1)
        nro5.grid(column=1,row=1)
        nro6.grid(column=2,row=1)
        nro7.grid(column=0,row=0)
        nro8.grid(column=1,row=0)
        nro9.grid(column=2,row=0)


        area2 = Frame(self)
        delete = Button(area2, text="<-")
        delete.grid(row=0)
        divide = Button(area2, text="%")
        divide.grid(row=1)
        multiplication = Button(area2, text="X")
        multiplication.grid(row=2)
        minus = Button(area2, text="-")
        minus.grid(row=3)
        plus = Button(area2, text="+")
        plus.grid(row=4)

        self.pack()
        area1.pack()
        area2.pack()

    
if __name__ == "__main__":
    root = Tk()
    app = App()
    root.mainloop()
