import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk


class SearchingRoute(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self._controller = controller
        label = tk.Label(self, text=controller.selected_scenario, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        labelframe1 = tk.LabelFrame(self, text="Searching for interesting route...")
        labelframe1.pack(fill="both", expand="yes")

        self._video_running = True

        video_name = "routes.mp4"  # This is your video file path
        my_video = imageio.get_reader(video_name)

        my_label = tk.Label(labelframe1)

        my_label.pack()
        self._thread = threading.Thread(target=self.stream, args=(my_video, my_label))
        self._thread.daemon = 1

        self.bind("<<" + self.__class__.__name__ + ">>", self._event_call)

    def stream(self, video, label):
        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image
        self._controller.show_frame("PopulateScenario")

    def _event_call(self, event):
        print(self.__class__.__name__)
        print("event -> "+str(event))
        self._thread.start()

