import tkinter

app = tkinter.Tk()

WIDTHBUTTON = 3
HEIGHTBUTTON = 1
memory = 0
action = ""

app.title("Калькулятор")

def calc(m1):
    global memory
    global action
    if action == "+" :
        m1 = memory + float(m1)
        pass
    elif action == "-" :
        m1 = memory - float(m1)
        pass
    elif action == "*" :
        m1 = memory * float(m1)
        pass
    else :
        if m1 == "0" :
            m1 = "DivByZerro!"
        else :
            m1 = memory / float(m1)
            pass
        pass
    memory = 0
    action = ""
    return m1

def clear() :
    global memory
    global action
    memory = ""
    action = ""
    display.delete(0, tkinter.END)
    display.insert(0, "0")

def click(bt) :
    global action
    global memory
    if bt in "0123456789" :
        if display.get() == "0" :
            display.delete(0, 1)
        display.insert(tkinter.END, bt)
    if bt == "C" :
        clear()
    if bt == "." :
        if not(bt in display.get()) :
            display.insert(tkinter.END, bt)
    if bt in "+-*/" :
        if action == "" :
            memory = float(display.get())
            display.delete(0, tkinter.END)
            display.insert(0, 0)
            action = bt
    if bt == "=" :
        res = calc(display.get())
        display.delete(0, tkinter.END)
        display.insert(0, res)

# формуємо інтерфейс
## дисплей
display = tkinter.Entry(master = app, 
                        font = ("", 20), 
                        width = 18,
                        justify = "right")
display.grid(row = 0, column = 0, columnspan = 4)
display.insert(0, "0")
## кнопки
btns = []
txtBtns = "C789*456/123+0.=-"
for txt in txtBtns :
    btns.append(tkinter.Button(master = app,
                      width = WIDTHBUTTON,
                      height = HEIGHTBUTTON,
                      font = ("", 20),
                      text = txt,
                      command = lambda itm = txt : click(itm)
                              )
               )
    
btns[0].grid(row = 1, column = 3)
r = 2
c = 0
for i in range(1, len(txtBtns)) :
    btns[i].grid(row = r, column = c)
    c += 1
    if c > 3 :
        r += 1
        c = 0

app.mainloop()