import tkinter
import random

win = tkinter.Tk()
win.title("Заголовок програми")
win.geometry("350x450") # геометрія вікна

buttons = []
for i in range(16):
    buttons.append(i)

data = []
for i in range(16) :
    k = random.randint(0,len(buttons) - 1)
    data.append(buttons.pop(k))


for y in range(4):
    
    for x in range(4) :
        
        txt = f"{data[x+y*4]}"
        if txt == "0" :
            txt = ""
        buttons.append(tkinter.Button(win, text = txt))
        buttons[x+y*4].grid(row = y, column = x)
        

win.mainloop()
