"""
Доповни коден рядок програми 
однорядковими коментарями з поясненнями
про дії, що описані відповідною вказівкою.
Запусти програму на виконання та за необхідності
виправ помилки
"""
import tkinter
import tkinter.messagebox as mb

win = tkinter.Tk()
win.title("Пробне вікно")
win.geometry("300x400")

def pressClick() :
    mb.showinfo("Інформація","Програма припинить роботу")
    win.destroy()

mess = tkinter.Label(win, text = "Текстове повідомлення")
mess.pack()

press = tkinter.Button(win, "Гаразд",
                       command = pressClick)
press.pack()

win.mainloop()