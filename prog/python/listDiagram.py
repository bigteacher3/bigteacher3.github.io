import tkinter
import tkinter.simpledialog as sd

win = tkinter.Tk()
win.title("Інфографіка")
win.geometry("400x400+200+100")

money = list()

def inputMoney() :
    money.clear()
    n = 7
    for x in range(7) :
        y = sd.askinteger("Введення", f"Введи виручку за {x+1} день: ")
        if y == None :
            money.append(0)
        else :
            money.append(y)
    tkinter.messagebox.showinfo("Повідомлення","Дані введено успішно. Для побудови інфографікинатисніть відповідну кнопку")

def showInfo() :
    canv.delete("all")
    canv.create_line(5, 255, 335, 255, fill = "red")
    
    dx = 10
    if len(money) > 0 :
        full = max(money)
        if full > 0:
            for x in money :
                h = int(240 * x / full)
                canv.create_rectangle(dx, 255 - h, dx + 40, 255, fill = "blue")
                dx += 47
        else:
            tkinter.messagebox.showerror("Помилка!", "Усі значення нульові")
    else :
        tkinter.messagebox.showerror("Помилка!", "Спочатку введи дані")
    pass


btn1 = tkinter.Button(win, text = "Почати введення", command = inputMoney)
btn1.pack()

btn2 = tkinter.Button(win, text = "Створення інфографіки", command = showInfo)
btn2.pack()

canv = tkinter.Canvas(win, width=340, height=260, bg="white")
canv.pack()

win.mainloop()
