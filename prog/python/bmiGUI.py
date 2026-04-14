import tkinter

win = tkinter.Tk()
win.geometry("450x480+50+5")
win.title("BMI INDEX")
win.config(bg = "#FFCCCC")

img = tkinter.PhotoImage(file="img.png")
img1 = tkinter.PhotoImage(file="img1.png")
img2 = tkinter.PhotoImage(file="img2.png")
img3 = tkinter.PhotoImage(file="img3.png")
img4 = tkinter.PhotoImage(file="img4.png")

def calculate() :
    pass

label_title = tkinter.Label(win, text = "ДІЗНАЙСЯ СВІЙ ІНДЕКС МАСИ ТІЛА",
                           width = 50, bg = "#584332", fg = "#ffffff")
label_title.place(x = 10, y = 10)
label_height = tkinter.Label(win, text = "Введи свій зріст:",
                             width = 15, bg = "#FFCCCC", fg = "#584332")
label_height.place(x = 10, y = 50)
entry_height = tkinter.Entry(win, width = 15)
entry_height.place(x = 150, y = 52)

label_img = tkinter.Label(win, image = img4, text = "Зображення")
label_img.place(x = 180, y = 120)

label_result = tkinter.Label(win, text = "Не визначено",
                             font = ("Arial", 24),
                             bg = "#FFCCCC", width = 23)
label_result.place(x = 10, y = 395)

btn_result = tkinter.Button(win, text = "Розрахувати",
                            bg = "#323030", fg="white",
                            command = calculate)
btn_result.place(x = 165, y = 430)



win.mainloop()