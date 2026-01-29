import tkinter as tk
import tkinter.ttk as ttk
from gpiozero import LED
led = LED(10)
root = tk.Tk()
lives = 3
def destroy():
    led.toggle()
root.title("Window")
root.geometry("400x400")
text = tk.Label(text=LED, background="black",  foreground="white")
button = tk.Button(text='Toggle LED', command=destroy)
button.place(x=0, y=50)
text.pack()
root.mainloop()
