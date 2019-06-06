import time
import tkinter as tk
from tkinter import font as tkfont


class ExperimentInfo(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self._controller = controller
        label = tk.Label(self, text="Experiment Information", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        labelframe1 = tk.LabelFrame(self, text="Adding pedestrians, cyclists and vehicles...")
        labelframe1.pack(fill="both", expand="yes")

        text_font = tkfont.Font(family='Helvetica', size=25, weight="bold", slant="italic")
        toplabel = tk.Label(labelframe1, text="Place to put the positive comments", font=text_font)
        toplabel.pack()
        toplabel.place(anchor="c", relx=.5, rely=.5)

        self.bind("<<"+self.__class__.__name__+">>", self._event_call)

    def _event_call(self, event):
        print(self.__class__.__name__)
        print("event -> " + str(event))
        time.sleep(10)
        self._controller.show_frame("SearchingRoute")