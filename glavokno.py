from tkinter import *
#*******************************************************
# МЕТОДЫ И ФУНКЦИИ
#*******************************************************

#Метод вывода лошадей
def horsePlaseInWindow():
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x01), y=100)
    horse03.place(x=int(x01), y=180)
    horse04.place(x=int(x01), y=260)

#Строка чата
def insertText(s):
    textDiary.insert(INSERT, s + "\n")
    textDiary.see(END)



root = Tk()
#Значение переменных
x01 = 20
x02 = 20
x03 = 20
x04 = 20

#*************************************************************
#ФОРМИРУЕМ ВСЕ ЭЛЕМЕНТЫ ОКНА
#*************************************************************

#размеры окна
WIDTH = 1024
HEIGHT = 600
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
#Заголовок
root.title("ИППОДРОМ")
#Запрет на изменение размеров
root.resizable(False, False)
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
#Добавление изображений фона и лошадей
road_image = PhotoImage(file="road.png")
road = Label(root, image=road_image)
road.place(x=0, y=17)
#Выводим лошадей
# x01 = 20 #координата для первой лошади
horse01_image = PhotoImage(file="horse01.png")
horse01 = Label(root, image=horse01_image)

horse02_image = PhotoImage(file="horse02.png")
horse02 = Label(root, image=horse02_image)

horse03_image = PhotoImage(file="horse03.png")
horse03 = Label(root, image=horse03_image)

horse04_image = PhotoImage(file="horse04.png")
horse04 = Label(root, image=horse04_image)
# horse01.place(x=int(x01), y=20)
horsePlaseInWindow()

#Кнопака старт
startButton = Button(text="СТАРТ", font="arial 20", width=61, background="#37AA37")
startButton.place(x=20, y=370)

#Чат с информацией
textDiary = Text(width=70, height=8, wrap=WORD)
textDiary.place(x=430, y=450)
scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=990, y=450, height=132)
textDiary["yscrollcommand"] = scroll.set



root.mainloop()
