import tkinter as tk


class DrivingSummary(tk.Frame):

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
