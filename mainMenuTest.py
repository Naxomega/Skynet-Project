import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import time
from picamera2 import Picamera2
from tkinter import IntVar
import random

mesure = 0
count = 0

def quit():
    root.destroy()


def mesureFrontale():
    global mesure
    count = random.randint(1, 100)
    print(count)
    mesure = str(count)
    ####
    distance.configure(text=f"Distance: {mesure}")
    #pour arhtur ^^^^

    

def update_frame():
    if checkCamera1.get() == 1:
        # Camera ON
        frame = camera.capture_array()
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image)

        camera_label.config(image=photo)
        camera_label.image = photo
    else:
        # Show solid black image of same size
        black_image = np.zeros((480, 640, 3), dtype=np.uint8)
        image = Image.fromarray(black_image)
        photo = ImageTk.PhotoImage(image)

        camera_label.config(image=photo)
        camera_label.image = photo

    root.after(30, update_frame)

# Main window
root = tk.Tk()
root.title("Robot GUI")
root.geometry("1280x960")

# Grid setup
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

checkCamera1 = IntVar(value=1)

# Frames
frame1 = tk.Frame(root, bg="lightblue")
frame2 = tk.Frame(root, bg="lightgreen")

frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=0, column=1, sticky="nsew")

frame1.rowconfigure([0, 1, 2], weight=1)
frame1.columnconfigure(0, weight=1)

frame2.rowconfigure([0, 1], weight=1)
frame2.columnconfigure(0, weight=1)

# Frame 1 content
label1 = tk.Label(frame1, text="Camera", font=("Arial", 20))
label1.grid(row=0, column=0, pady=10)

camera_label = tk.Label(frame1)
camera_label.grid(row=1, column=0)

checkButtonCamera = tk.Checkbutton(
    frame1,
    text="On/Off Camera",
    variable=checkCamera1,
    onvalue=1,
    offvalue=0,
    height=2,
    width=20
)
checkButtonCamera.grid(row=2, column=0, pady=10)

# Frame 2 content
label2 = tk.Label(frame2, text="Info", font=("Arial", 20))
label2.grid(row=0, column=0, pady=10)

#distance
distance = tk.Label(frame2, text=f"Distance:{mesure} ", font=("Arial", 20))
distance.grid(row=0, column=0, pady=10)
button3 = tk.Button(frame2, text="Frame 2 Button", command= mesureFrontale)
button3.grid(row=1, column=0, pady=10)

#quitter
button4 = tk.Button(root, text="Quit", command = quit, bg="red",fg="white")
button4.grid(row=2, column=0, pady=10, padx=10, sticky="swne", columnspan=2)


# Initialize camera
camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"size": (640, 480)}))
camera.start()
time.sleep(1)

# Start updating the frame
update_frame()

# Launch GUI
root.mainloop()
