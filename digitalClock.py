from tkinter import Tk, Label
from datetime import datetime

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")
window.configure(background="grey")

label = Label(window, font=("Arial", 78, "bold"), background="steelblue", foreground="black")
label.pack(pady=100)

def clock():
    time = datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500, clock)

clock()
window.mainloop()
