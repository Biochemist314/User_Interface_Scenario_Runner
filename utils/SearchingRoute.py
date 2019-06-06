import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk


class SearchingRoute(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=controller.frames["ChooseTown"].scenario_selected, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        select_scenario = tk.Button(self,text="Would you like to play?",
                                    command = lambda:controller.show_frame("PopulateScenario"))
        select_scenario.pack()

        self._video_end = False

        # button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
        # button.pack()

        video_name = "routes.mp4"  # This is your video file path
        my_video = imageio.get_reader(video_name)

        my_label = tk.Label(self)

        my_label.pack()
        thread = threading.Thread(target=self.stream, args=(my_video, my_label))
        thread.daemon = 1
        thread.start()

        self.bind(self.__class__.__name__, self.eventCall)

    def stream(self,video, label):

        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image
        self._video_end = True

    def eventCall(self, event):
        print(event)
