import tkinter
import tkinter.simpledialog as sd

win = tkinter.Tk()
win.title("Введення та виведення списків")
win.geometry("400x400+500+200")

def btn1Click() :
    c = int(count.get())
    x = list()
    for y in range(c) :
        k = sd.askfloat("Введення", f"{y+1}-e число:")
        x.append(k)
    print(x)
    # processing
    out = ""
    for y in x :
        out += str(y) + "\n"
    multitext.insert("1.0", out)
    pass


asc_count = tkinter.Label(win, text = "Введи кількість елементів").pack()
count = tkinter.Entry(win)
count.pack()
btn1 = tkinter.Button(win, text = "Підтвердити", command = btn1Click).pack()
multitext = tkinter.Text(win, width = 10, height = 10)
multitext.pack()

win.mainloop()