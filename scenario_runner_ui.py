import os
import random

import tkinter as tk
from tkinter import font as tkfont

from utils.StartPage import StartPage
from utils.ExperimentInfo import ExperimentInfo
from utils.ChooseTown import ChooseTown
from utils.SearchingRoute import SearchingRoute
from utils.PopulateScenario import PopulateScenario
from utils.DrivingMode import DrivingMode
from utils.DrivingSummary import DrivingSummary


class ScenarioRunnerApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Carla Scenario Runner UI")

        self.title_font = tkfont.Font(family='Helvetica', size=10, slant="italic")

        self.map_of_scenarios = {}

        self.selected_scenario = None


        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path,".list_of_scenarios"), "r") as f:
            counter = 0
            lines = f.read().splitlines()
            for line in lines:
                print(">>"+line)
                self.map_of_scenarios[line] = line
                counter += 1

        key = random.choice(list(self.map_of_scenarios.keys()))

        self.selected_scenario = self.map_of_scenarios[key]

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ExperimentInfo, SearchingRoute, PopulateScenario, DrivingMode, DrivingSummary):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        self.geometry("1024x768")  # You want the size of the app to be 500x500
        self.resizable(0, 0)  # Don't allow resizing in the x or y direction

        self.bind("<<"+self.__class__.__name__+">>", self._event_call)

    def _event_call(self, event):
        print(event)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        frame.update()
        print(page_name)
        frame.event_generate("<<"+page_name+">>")


if __name__ == "__main__":
    app = ScenarioRunnerApp()
    app.mainloop()

