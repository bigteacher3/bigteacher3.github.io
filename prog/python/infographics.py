from tkinter import *

win = Tk()
win.title("Інфографіка за даними списку")
win.geometry("400x450")

market = []
week = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Нд"]
current = 0

def inputData() :
    global market, week, current
    if current == len(week) - 1 :
        btn1["state"] = "disabled"
        inp1["state"] = "disabled"
        btn2["state"] = "enabled"
        current = -1
        market = []
        lbl1.config(text = "Виручка за день: " + week[0] + " - ціле число")
    else :
        lbl1["text"] = "Виручка за день: " + week[current + 1] + " - ціле число"
    market.append(int(inp1.get()))
    inp1.delete(0, END)
    current += 1

def showGraphics() :
    global market, week
    #to bee continued
    
    #finalization
    btn1["state"] = "enabled"
    btn2["state"] = "disabled"
    inp1["state"] = "enabled"
    pass

lbl0 = Label(win, text = "Введення даних")
lbl0.pack()
lbl1 = Label(win, text = "Виручка за день: " + week[0] + " - ціле число")
lbl1.pack()
inp1 = Entry(win)
inp1.pack()
btn1 = Button(win, text = "Підтверджую", command = inputData)
btn1.pack()
btn2 = Button(win, text = "Інфографіка", command = showGraphics, state = "disabled")
btn2.pack()
page = Canvas(win, height = 260, width = 360, bg = "yellow")
page.pack()

win.mainloop()
