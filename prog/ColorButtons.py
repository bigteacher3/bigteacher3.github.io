from tkinter import *
from tkinter.messagebox import showinfo, showerror

win = Tk()
win.title("Color Buttons")
win.geometry("200x200+200+100")
    

btns = []
colors = ["yellow","lightblue","orange","green"]

for c in colors:
    btns.append(Button(text = c, bg = c, fg = "brown"))

for b in btns:
    b.pack()
                
btns[0].bind("<Motion>", lambda evnt: showinfo("Обрано", "Жовтий"))
btns[1].bind("<Button-1>", lambda evnt: showinfo("Обрано", "Блакитний"))
btns[2].bind("<3>", lambda evnt: showinfo("Обрано", "Помаранчовий"))
btns[3].bind("<Double-1>", lambda evnt: showinfo("Обрано", "Зелений"))
    
win.mainloop()
