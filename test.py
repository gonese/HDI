import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.text import Text
from matplotlib.image import AxesImage
import numpy as np
from tkinter import *
from tkinter import ttk

class Application(Frame):
    def __init__(self,master=None):
        self.count = 0
        self.inputs = []
        self.outputs = []
        self.input = True
        super().__init__(master)
        self.master = master
        self.createPipeFrame()
        self.createWidget()
        self.pack()
    def createPipeTree(self):
        self.PipeLineFrame = Frame(self.PipeFrame,width=300,height=400,bg='white')
        self.PipeLineFrame.place(x=10,y=50)
        self.PipeTree = ttk.Treeview(self.PipeLineFrame,column=("input","output"),show='headings')
        self.PipeTree.column("input",width=125,stretch=NO)
        self.PipeTree.column("output",width=150,stretch=NO)
        self.PipeTree.heading("input",text="Input")
        self.PipeTree.heading("output",text="Output")
        self.PipeTree.pack()
    def createPipeFrame(self):
        self.PipeFrame = Frame(self.master, width=300, height=500)
        self.PipeFrame.place(x=0, y=0)
        self.createPipeTree()
        self.inputt = Label(text = "input : ")
        self.inputt.place(x=10,y=350)
        self.inputt.bind('<Button-1>',self.select)
        self.outputt = Label(text="output : ")
        self.outputt.place(x=10,y=370)
        self.outputt.bind('<Button-1>',self.select)
        self.inputBtn1 = Button(self.PipeFrame, text="F0").place(x=10,y=400)
        self.inputBtn2 = Button(self.PipeFrame, text="Mel" ).place(x=50, y=400)
        self.inputBtn3 = Button(self.PipeFrame, text="audio" ).place(x=100, y=400)
        self.inputBtn4 = Button(self.PipeFrame, text="text").place(x=150,y=400)
        self.inputBtn5 = Button(self.PipeFrame, text="f0").place(x=200, y=400)
    def select(self,event):
        if event.widget == self.inputt:
            self.input = True
        else:
            self.input = False
        self.refresh()

    def refresh(self):
            text = "input :   "
            for x in self.inputs:
                text += " " + x + " , "
            self.inputt['text'] = text[:-2]
            text = "output :   "
            for x in self.outputs:
                text += " " + x + " , "
            self.outputt['text'] = text[:-2]
    def createWidget(self):
        self.inputBtn1 = Button(self.PipeFrame, text="F0")
        self.inputBtn1.place(x=10,y=400)
        self.inputBtn1.bind('<Button-1>',self.addMetrics)
        self.inputBtn2 = Button(self.PipeFrame, text="Mel")
        self.inputBtn2.place(x=50, y=400)
        self.inputBtn2.bind('<Button-1>', self.addMetrics)
        self.inputBtn3 = Button(self.PipeFrame, text="audio")
        self.inputBtn3.place(x=100, y=400)
        self.inputBtn3.bind('<Button-1>', self.addMetrics)
        self.inputBtn4 = Button(self.PipeFrame, text="text")
        self.inputBtn4.place(x=150,y=400)
        self.inputBtn4.bind('<Button-1>', self.addMetrics)
        self.inputBtn5 = Button(self.PipeFrame, text="f0")
        self.inputBtn5.place(x=200, y=400)
        self.inputBtn5.bind('<Button-1>', self.addMetrics)
        self.commitBtn = Button(self.PipeFrame, text ='add procedure')
        self.commitBtn.place(x=10,y=450)
        self.commitBtn.bind('<Button-1>',self.commited)
    def commited(self,event):
        if self.inputs != [] and self.outputs != []:
            self.PipeTree.insert("","end",values = (self.inputs,self.outputs))
            self.count += 1
            self.inputs = []
            self.outputs = []
            self.refresh()
    def addMetrics(self,event):
        if self.input:
            if event.widget['text'] not in self.inputs:
                self.inputs.append(event.widget['text'])
        else:
            if event.widget['text'] not in self.outputs:
                self.outputs.append(event.widget['text'])
        self.refresh()


if __name__ == '__main__':
    # root = Tk()
    # root.geometry("1200x500+200+300")
    # root.title("HDI is the best")
    # Application(master=root)
    # root.mainloop()
    print(len("Central,60.0,33860.0,594.45,37.0,0.0,37.0,0.0,0.0,37.0,0.0,,,,,,,0.0,35.0,0.0,0.0,,,,,,40.0,0.0,0.0,208.0,208.0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,189.1,0.0,387.31,,,,,,1063.07,0.0,,,,,,,,,,,,,,,,".split(',')))