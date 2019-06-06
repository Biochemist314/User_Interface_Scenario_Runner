import tkinter as tk
from tkinter import font as tkfont
import time


class ExperimentInfo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self._controller = controller
        self.controller = controller
        label = tk.Label(self,text="Experiment description",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)

        labelframe1 = tk.LabelFrame(self, text="Experiment Info")
        labelframe1.pack(fill="both", expand="yes")

        ilabel = tk.Label(labelframe1,text='Self-driving vehicles are controlled and tested by Artificial Intelligence (AI).')
        jlabel = tk.Label(labelframe1,text ='The goal of this experiment is to show how AI can be used to assess the safety of self-driving vehicles.')
        ilabel.pack(side = "top")
        jlabel.pack(side="top")

        text_font = tkfont.Font(family='Helvetica', size=25, weight="bold", slant="italic")
        toplabel = tk.Label(labelframe1, text="Place to put the positive comments", font=text_font)
        toplabel.pack()

        self.bind("<<"+self.__class__.__name__+">>", self.eventCall)

    def eventCall(self, event):
        print(event)
        time.sleep(2)
        self.controller.show_frame("ChooseTown")