from cProfile import label
from tkinter import *
from PIL import Image, ImageTk
import cv2

def show_frames(window, frame):
    # Get the latest frame and convert into Image
    frame =cv2.resize(frame, dsize=None, fx=0.5, fy=0.5)
    cv2image= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    #Label
    label = Label(window)
    label.pack()
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    window.after(15, show_frames)