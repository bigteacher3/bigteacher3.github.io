from tkinter import *

win = Tk()
win.title("Інфографіка за даними списку")
win.geometry("400x480")

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
        lbl1.config(text = "Виручка за день: " + week[current] + " - ціле число")
    else :
        lbl1["text"] = "Виручка за день: " + week[current + 1] + " - ціле число"
    market.append(int(inp1.get()))
    page.delete("all")
    inp1.delete(0, END)
    current += 1
    print(market)

def showGraphics() :
    global market, week
    # begin draw
    my = page["height"] - 40
    page.create_line(20, my, 340, my,    # координати другої лінії
              fill='red',                          # колір лінії 
              width=5,                             # ширина лінії
              activefill='brown',                 # колір лінії, коли над нею мишка
              arrow=LAST,                          # розміщення стрілки в кінці лінії
              arrowshape="10 30 10")               # розміри стрілки
    key = my / max(market)-1
    sx = 20
    for d in week :
        page.create_text(sx, my + 20, text = d, fill = "brown")
        sx += 50
    sy = my - int(key * market[0])
    sx = 20
    ex = 0
    ey = 0
    cnt = len(week) - 1
    for k in range(cnt) :
        ex = sx + 50
        ey = my - int(key * market[k + 1])
        page.create_line(sx, sy, ex, ey, fill = "blue", width = 7)
        sx = ex
        sy = ey
    # end draw
    btn1["state"] = "enabled"
    btn2["state"] = "disabled"
    inp1["state"] = "enabled"
    market = []
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
