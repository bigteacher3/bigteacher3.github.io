import tkinter
import time

win = tkinter.Tk()
win.title("Заголовок програми")
win.geometry("350x450") # розмір вікна

x = list(range(7))

def start() :
    for a in x :
        label.config(text = f"Відлік: {7-a}", width = 30)
        time.sleep(1)
        
label = tkinter.Label(win, text = "Відлік")
label.pack(pady = 10)
button = tkinter.Button(win, text = "Start", command = start)
button.pack()

win.mainloop()