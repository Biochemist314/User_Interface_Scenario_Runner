import subprocess
import sys
import tkinter as tk, threading
from tkinter import font as tkfont


class DrivingMode(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self._controller = controller
        label = tk.Label(self, text="Driving Mode", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        labelframe1 = tk.LabelFrame(self, text="Driving Mode!")
        labelframe1.pack(side="top",fill="both",pady=10, expand="yes")
        labelframe1.place(anchor="c", relx=.5, rely=.5)

        text_font = tkfont.Font(family='Helvetica', size=25, weight="bold", slant="italic")
        top_label = tk.Label(labelframe1, text="Place to put the positive comments", font=text_font)
        top_label.pack()

        self._parameters = ['ls', '-l']

        self.bind("<<"+self.__class__.__name__+">>", self._event_call)

    def run(self):
        command = self._parameters
        print(command)
        subprocess.run(command, stdout=sys.stdout, stderr=subprocess.PIPE)

        self._controller.show_frame("DrivingSummary")

    def _event_call(self, event):
        print(self.__class__.__name__)
        print("event -> "+str(event))
        self._thread = threading.Thread(target=self.run)
        self._thread.daemon = 1
        self._thread.start()