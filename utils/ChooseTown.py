import tkinter as tk


class ChooseTown(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Selecting your town...", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        select_scenario = tk.Button(self,text="Search route"
                                    ,command = lambda:controller.show_frame("SearchingRoute"))
        select_scenario.pack()

        lbl1 = tk.Label(self, text="Node List:", fg='black', font=("Helvetica", 16, "bold"))
        lbl1.pack()
        lbl2 = tk.Label(self, text="Node Information:", fg='black', font=("Helvetica", 16, "bold"))
        lbl2.pack()
        # lbl1.grid(row=0, column=0, sticky=tk.W)
        # lbl2.grid(row=0, column=1, sticky=tk.W)
        self.scenario_selected = None

        frm = tk.Frame(self)
        # frm.grid(row=1, column=0, sticky=tk.N + tk.S)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        scrollbar = tk.Scrollbar(frm, orient="vertical")
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self._listNodes = tk.Listbox(frm, width=20, yscrollcommand=scrollbar.set, font=("Helvetica", 12))
        self._listNodes.bind('<<ListboxSelect>>', self._scenario_clicked)
        self._listNodes.pack(expand=True, fill=tk.Y)

        scrollbar.config(command=self._listNodes.yview)

        for k, v in controller.map_of_scenarios.items():
            if self.scenario_selected is None:
                self.scenario_selected = v
            self._listNodes.insert(tk.END, v)
        frm.pack()

        # listSelection = tk.Listbox(self, height=4, font=("Helvetica", 12))
        # # listSelection.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N)
        # for x in "ABCD":
        #     listSelection.insert(tk.END, x + ": ?")
        # listSelection.pack()

        button = tk.Button(self, text="Search Route", command=lambda: controller.show_frame("SearchingRoute"))
        button.pack()

        photo = tk.PhotoImage(file="scenario.gif")
        scenicroute = tk.Label(self,image=photo)
        scenicroute.image = photo
        scenicroute.pack()

        self.bind(self.__class__.__name__, self.eventCall)

    def eventCall(self, event):
        print(event)

    def _scenario_clicked(self, event):
        widget = event.widget
        selection = widget.curselection()
        print("selection -> " + str(selection))
        picked = widget.get(selection[0])
        print("picked -> " + str(picked))

