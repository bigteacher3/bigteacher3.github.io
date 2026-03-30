import tkinter
import tkinter.messagebox as mb
import random as rnd

win = tkinter.Tk()
win.title("Опитування")
win.geometry("300x400")

def btn1Click() :
    mb.showinfo("Прийнято", "А ніхто й не сумнівався :)")
    
def btn2Click(event) :
    mb.showinfo("Прийнято", "Неперевершена спритність!!!")
    win.update()
    
def btn2Enter(event) :
    new_x = rnd.randint(10, 200)
    new_y = rnd.randint(10, 300)
    btn2.place(x = new_x, y = new_y)
    win.update()

txt = tkinter.Label(win, text = "Сподобалася програма?").pack()
btn1 = tkinter.Button(win, text = "Так", command = btn1Click,
                     width = 10, height = 3)
btn1.place(x = 10, y = 175)
btn2 = tkinter.Button(win, text = "Ні", 
                     width = 10, height = 3)
btn2.place(x = 205, y = 175)
btn2.bind("<Motion>", btn2Enter)
btn2.bind("<Button-1>", btn2Click)

win.mainloop()