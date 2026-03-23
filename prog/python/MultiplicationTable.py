# підключаємо бібліотеку віджетів
import tkinter

win = tkinter.Tk() # створюємо вікно
win.title("Таблиця множення") # заголовок вікна
win.geometry("350x450") # геометрія вікна

# Описуємо формування таблиці
def createTable() :
    n = select.get() # дізнаємося множник
    mess = "" # готуємо змінну для повідомлення
    for y in range(10) : # 10 разів створюємо нове повідомлення 
        d = (y + 1) * n # обчислюємо добуток
        mess = f"{(y+1)} * {n} = {d}" # f-рядком описуємо повідомлення
        table[y].config(text = mess) # публікуємо повідомлення у
                                     # текстовій мітці з відповідним номером

# створюємо пояснювальний текст
txt1 = tkinter.Label(win, text = "Обери значення:").pack()
# створюємо віджет вибору - шкалу
select = tkinter.Scale(win, from_ = 1, to = 20, resolution = 1)
select.pack()
select.set(5) # встановлюємо початкову позицію на шкалі
# створюємо кнопку
btn = tkinter.Button(win, text = "Зґенерувати", command = createTable)
btn.pack()
# створюємо список текстових міток для таблиці множення
table = [None] * 10
for x in range(10) :
    table[x] = tkinter.Label(win, text = "", width = 20)
    table[x].pack()

# запускаємо цикл опитування подій
win.mainloop()
