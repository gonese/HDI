import matplotlib.pyplot as plt
from matplotlib import patches
from tkinter import *
from matplotlib.container import BarContainer
from matplotlib.patches import Rectangle
import numpy as np
class barChart(object):

    def __init__(self):
        self.labels = ['G1', 'G2', 'G3', 'G4', 'G5']


        self.men_means = [20, 27, 30, 30, 35]
        self.width = 0.35
        self.fig, self.ax = plt.subplots()
        self.ax.bar(self.labels, self.men_means, self.width,color = 'b', label='Men', picker=True)

        self.ax.set_xlabel('Men')
        self.ax.set_ylabel('Scores', picker=True)
        self.ax.set_title('Scores by group and gender')
        self.bars = [i for i in self.ax.containers if isinstance(i, BarContainer)][0]

        for index, value in enumerate(self.men_means):
            self.ax.text(index, value, str(value))
        # for label in self.ax.get_xticklabels():
        #     label.set_picker(True)
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
            print(self.Left,self.Right)
            for x in self.bars:
                if x.get_height() == self.Left or x.get_height() == self.Right:
                    x.set_color('r')
                else:
                    x.set_color('b')
                plt.show()


        self.cid = self.fig.canvas.mpl_connect('pick_event', onclick)


barChart()
window = Tk()

# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("500x500")

# button that displays the plot
plot_button = Button(master=window,
                     command=plt.show,
                     height=2,
                     width=10,
                     text="Plot")

# place the button
# in main window
plot_button.pack()

# run the gui
window.mainloop()