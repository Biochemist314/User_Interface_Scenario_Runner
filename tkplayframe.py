import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
from PIL import Image,ImageTk
import time

class ScenarioRunnerApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ExperimentInfo, StartGame, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        self.geometry("800x600")  # You want the size of the app to be 500x500
        self.resizable(0, 0)  # Don't allow resizing in the x or y direction

        self.bind(self.__class__.__name__, self.eventCall)

    def eventCall(self, event):
        print(event)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        frame.update()
        print(page_name)
        frame.event_generate("<<"+page_name+">>")


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to CARLA ScenarioRunner v1.0", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        simage = Image.open("car.png")
        sphoto = ImageTk.PhotoImage(simage)
        slabel = tk.Label(image=sphoto)
        slabel.image = sphoto
        button1 = tk.Button(self, image=sphoto, text="Start Scenario (\u21b5)", compound=tk.TOP, command=lambda: controller.show_frame("ExperimentInfo"))
        button1.focus()
        button1.pack()


        # bimage = Image.open("score.png")
        # bphoto = ImageTk.PhotoImage(bimage)
        # blabel = tk.Label(image=bphoto)
        # blabel.image = bphoto
        # button2 = tk.Button(self, image=bphoto, text="Leaderboard ()", compound=tk.TOP,
        #                     command=lambda: controller.show_frame("PageTwo"))
        # button2.pack()

        # bimage = Image.open("exit.png")
        # bphoto = ImageTk.PhotoImage(bimage)
        # blabel = tk.Label(image=bphoto)
        # blabel.image = bphoto
        # button3 = tk.Button(self, image=bphoto, text="Exit", compound=tk.TOP,
        #                     command=lambda: exit(0))
        # button3.pack()

        self.bind(self.__class__.__name__, self.eventCall)

    def eventCall(self, event):
        print(event)


class StartGame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Scenario 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)



        select_scenario = tk.Button(self,text="Would you like to play?"
                                    ,command = lambda:controller.show_frame("PageThree"))
        select_scenario.pack()

        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        button.pack()

        photo = tk.PhotoImage(file="scenario.gif")
        scenicroute = tk.Label(self,image=photo)
        scenicroute.image = photo
        scenicroute.pack()

        self.bind(self.__class__.__name__, self.eventCall)

    def eventCall(self, event):
        print(event)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Leaderboard", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        self.bind("<<"+self.__class__.__name__+">>", self.eventCall)

    def eventCall(self, event):
        print(event)


class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self,text="Video Consent",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)

        #master = Tk()
        #scrollbar = Scrollbar(master)
        #scrollbar.pack(side=RIGHT,fill=Y)

        #listbox = Listbox(master,yscrollcommand=scrollbar.set)
        #for i in range(1000):
            #listbox.insert(END,str(i))
        #listbox.pack(side=LEFT,fill=BOTH)

        #scrollbar.config(command=listbox.yview)


        yesbutton = tk.Button(self,text="Yes")
        yesbutton.pack()

        nobutton = tk.Button(self,text="No")
        nobutton.pack()

        button = tk.Button(self,text="Go to the start page",command=lambda: controller.show_frame("StartPage"))
        button.pack()

        self.bind("<<"+self.__class__.__name__+">>", self.eventCall)

    def eventCall(self, event):
        print(event)


class ExperimentInfo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self._controller = controller
        self.controller = controller
        label = tk.Label(self,text="Experiment description",font=controller.title_font)
        label.pack(side="top",fill="x",pady=10)

        labelframe1 = tk.LabelFrame(self, text="Positive Comments")
        labelframe1.pack(fill="both", expand="yes")

        toplabel = tk.Label(labelframe1, text="Place to put the positive comments")
        toplabel.pack()

        self.bind("<<"+self.__class__.__name__+">>", self.eventCall)

    def eventCall(self, event):
        print(event)
        time.sleep(2)
        self.controller.show_frame("StartPage")

if __name__ == "__main__":
    app = ScenarioRunnerApp()
    app.mainloop()