import librosa as librosa
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import tkinter as tk
import numpy as np
import plot
import librosa.display
from assistance import CleaningAssistant


class Application(Frame):
    def __init__(self,master=None):
        self.f = ["1","2","3","4","5"]
        self.count = 0
        self.inputs = []
        self.outputs = []
        self.buttons= []
        self.input = True
        super().__init__(master)
        self.master = master
        self.createPipeFrame()
        self.createWidget()
        self.createSPY()
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
        self.inputBtn1 = Button(self.PipeFrame, text="f0")
        self.inputBtn1.place(x=10,y=400)
        self.inputBtn1.bind('<Button-1>',self.addMetrics)
        self.inputBtn2 = Button(self.PipeFrame, text="mel")
        self.inputBtn2.place(x=50, y=400)
        self.inputBtn2.bind('<Button-1>', self.addMetrics)
        self.inputBtn3 = Button(self.PipeFrame, text="audio")
        self.inputBtn3.place(x=100, y=400)
        self.inputBtn3.bind('<Button-1>', self.addMetrics)
        self.inputBtn4 = Button(self.PipeFrame, text="text")
        self.inputBtn4.place(x=150,y=400)
        self.inputBtn4.bind('<Button-1>', self.addMetrics)
        self.inputBtn5 = Button(self.PipeFrame, text="spk")
        self.inputBtn5.place(x=200,y=400)
        self.inputBtn5.bind('<Button-1>', self.addMetrics)
        self.commitBtn = Button(self.PipeFrame, text ='add')
        self.commitBtn.place(x=10,y=450)
        self.commitBtn.bind('<Button-1>',self.commited)
        self.commitBtn = Button(self.PipeFrame, text ='delete')
        self.commitBtn.place(x=50,y=450)
        self.commitBtn.bind('<Button-1>',self.deleted)
        self.commitBtn = Button(self.PipeFrame, text ='submit')
        self.commitBtn.place(x=100,y=450)
        self.commitBtn.bind('<Button-1>',self.submitted)
        self.LB = Button(master=self.master, text="generate script")
        self.LB.place(x=1000, y=550)
        self.LB.bind('<Button-1>', self.lengthF)
    def createSPY(self):
        self.quantizer = Label(master=self.master,text="audio quantizer")
        self.quantizer.place(x = 500, y=10)
        self.quantizer.pack()
        self.qe = Entry(master=self.master,bg="white",width=30,fg="grey")
        self.qe.insert(0,"enter bin size")
        self.qe.place(x=550,y=10)
        self.qe.bind("<FocusIn>", self.handle_focus_in)
        self.qe.pack()
        self.melS = Label(master=self.master,text="mel specification")
        self.melS.place(x=500,y=40)
        self.melS.pack()
        self.me = Entry(master=self.master,bg="white",width=30,fg="grey")
        self.me.place(x=550,y=40)
        self.me.insert(0,"fmax ex:8000")
        self.me.bind("<Return>", self.handle_enter)
        self.me.bind("<FocusIn>", self.handle_focus_in)
        self.me.pack()
        self.f0S = Label(master=self.master,text="f0 specification")
        self.f0S.place(x=500,y=70)
        self.f0S.pack()
        self.fe = Entry(master=self.master,bg="white",width=30,fg="grey")
        self.fe.place(x=550,y=70)
        self.fe.insert(0,"fmin and fmax in note ex:'A C' ")
        self.fe.bind("<FocusIn>", self.handle_focus_in)
        self.fe.bind("<Return>", self.handle_enter)
        self.fe.pack()

    def deleted(self,event):
        if self.PipeTree.selection():
            selected_item = self.PipeTree.selection()[0]
            self.PipeTree.delete(selected_item)
    def submitted(self,event):
        self.clean = CleaningAssistant()
        self.recommendation = self.clean.tech_suggestions(self.finputs,self.foutputs)
        self.features()

    def commited(self,event):
        if self.inputs != [] and self.outputs != []:
            self.PipeTree.insert("","end",values = (self.inputs,self.outputs))
            self.finputs = self.inputs
            self.foutputs = self.outputs
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
    def features(self):
        for i in range(len(self.recommendation)):
            self.buttons.append(Button(master=self.master,text=self.recommendation[i]))
            if "length_regularization" in self.recommendation[i]:
                if "text" not in self.recommendation[i]:
                    self.buttons[-1].bind('<Button-1>',self.getAudioLength)
            self.buttons[-1].place(x =500,y =(i*30+200) )
            self.buttons[-1].pack()

    def handle_focus_in(self,event):
            event.widget.delete(0, tk.END)
            event.widget.config(fg='black')


    def handle_enter(self,event):
        pathAudio = "audios/"
        files = librosa.util.find_files(pathAudio, ext=['wav'])
        file = np.asarray(files)[0]

        if event.widget == self.fe:
            f = event.widget.get().split()
            y, sr = librosa.load(file)
            f0, voiced_flag, voiced_probs = librosa.pyin(y,fmin = librosa.note_to_hz(f[0]),
                                                         fmax=librosa.note_to_hz(f[1]))
            times = librosa.times_like(f0)
            D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
            fig, ax = plt.subplots()
            img = librosa.display.specshow(D, x_axis='time', y_axis='log', ax=ax)
            ax.set(title='pYIN fundamental frequency estimation')
            fig.colorbar(img, ax=ax, format="%+2.f dB")
            ax.plot(times, f0, label='f0', color='cyan', linewidth=3)
            ax.legend(loc='upper right')
            plt.show()
        elif event.widget == self.me:
            y, sr = librosa.load(file)
            D = np.abs(librosa.stft(y)) ** 2
            S = librosa.feature.melspectrogram(S=D, sr=sr,fmax=int(event.widget.get()))
            fig, ax = plt.subplots()
            S_dB = librosa.power_to_db(S, ref=np.max)
            img = librosa.display.specshow(S_dB, x_axis='time',
                                           y_axis='mel', sr=sr,
                                           fmax=int(event.widget.get()), ax=ax)
            fig.colorbar(img, ax=ax, format='%+2.0f dB')
            ax.set(title='Mel-frequency spectrogram')
            plt.show()
        # print(full_name_entry.get())
        # handle_focus_out('dummy')

    def getAudioLength(self,event):
        dur = {}
        pathAudio = "audios/"
        files = librosa.util.find_files(pathAudio, ext=['wav'])
        files = np.asarray(files)
        for file in files:
            y, sr = librosa.load(file)
            d = int(librosa.get_duration(y=y, sr=sr))
            dur[d] = dur.get(d, 0) + 1
        keys = sorted(dur.keys())
        d = []
        for key in keys:
            d.append(dur[key])
        c, k = zip(*sorted(zip(d, keys)))
        self.a = plot.barChart(k,c,"duration","count")
        self.lengthB()
        plt.show()
    def lengthF(self,event):
        l,r = self.a.getSelected()
        print(l,r)
if __name__ == '__main__':
    root = Tk()
    root.geometry("1200x600+200+300")
    root.title("HDI is the best")
    Application(master=root)
    root.mainloop()

