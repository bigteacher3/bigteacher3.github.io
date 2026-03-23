"""
Завдання:
Змінити вказівки побудови інтерфейсу, 
замінивши багато вказівок створення та пуьлікації
текстових міток, що призначені
для виведення таблиці множення
"""

import tkinter # імпорт бібліотеки віджетів

win = tkinter.Tk() # створення вікна
win.title("Таблиця множення") # встановлення заголовку вікна
win.geometry("300x450") # встановлення розмірів вікна

def tableCreate() : # Створення обробника подій для кнопки
    pass

# створення та публікація тексту запитання
quest = tkinter.Label(win, text = "Введи ціле число")
quest.pack()
# створення та публікація віджету введення відповіді
resp = tkinter.Entry(win)
resp.pack()
# створення та публікація віджету кнопки
btn = tkinter.Button(win, text = "Зґенерувати", command = tableCreate)
btn.pack()

# створення та публікація декількох текстових повідомлень,
# що призначені для виведення таблиці множення
expr1 = tkinter.Label(win, text = "Множення на 1")
expr1.pack()
expr2 = tkinter.Label(win, text = "Множення на 2")
expr2.pack()
expr3 = tkinter.Label(win, text = "Множення на 3")
expr3.pack()
expr4 = tkinter.Label(win, text = "Множення на 4")
expr4.pack()
expr5 = tkinter.Label(win, text = "Множення на 5")
expr5.pack()
expr6 = tkinter.Label(win, text = "Множення на 6")
expr6.pack()
expr7 = tkinter.Label(win, text = "Множення на 7")
expr7.pack()
expr8 = tkinter.Label(win, text = "Множення на 8")
expr8.pack()
expr9 = tkinter.Label(win, text = "Множення на 9")
expr9.pack()
expr10 = tkinter.Label(win, text = "Множення на 10")
expr10.pack()

# запуск циклічного опитування подій
win.mainloop()