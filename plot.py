import matplotlib.pyplot as plt
from matplotlib import patches
from tkinter import *
from matplotlib.container import BarContainer
from matplotlib.patches import Rectangle
import numpy as np
class barChart(object):

    def __init__(self,x,y,xlabel,ylabel):
        self.x = x


        self.y = y
        self.width = 0.35
        self.fig, self.ax = plt.subplots()
        self.ax.bar(x, y, self.width,color = 'b', label='Men', picker=True)

        self.ax.set_xlabel(xlabel)
        self.ax.set_ylabel(ylabel, picker=True)
        self.bars = [i for i in self.ax.containers if isinstance(i, BarContainer)][0]

        for index, value in enumerate(y):
            self.ax.text(index, value, str(value))
        self.Left = None
        self.Right = None


        def onclick(event):
            t = event.artist.get_height()
            if not self.Left:
                self.Left = t
            elif not self.Right:
                if t < self.Left:
                    self.Right = self.Left
                    self.Left = t
                else:
                    self.Right = t
            elif t < self.Left:
                self.Left = t
            elif t > self.Right:
                self.Right = t
            else:
                if abs(t - self.Left) > abs(t-self.Right):
                    self.Left = t
                else:
                    self.Right = t
            for x in self.bars:
                if x.get_height() == self.Left or x.get_height() == self.Right:
                    x.set_color('r')
                else:
                    x.set_color('b')
                plt.show()


        self.cid = self.fig.canvas.mpl_connect('pick_event', onclick)
    def getSelected(self):
        return (self.Left,self.Right)

# barChart()
# window = Tk()
#
# # setting the title
# window.title('Plotting in Tkinter')
#
# # dimensions of the main window
# window.geometry("500x500")
#
# # button that displays the plot
# plot_button = Button(master=window,
#                      command=plt.show,
#                      height=2,
#                      width=10,
#                      text="Plot")
#
# # place the button
# # in main window
# plot_button.pack()
#
# # run the gui
# window.mainloop()