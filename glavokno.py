from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#*******************************************************
# МЕТОДЫ И ФУНКЦИИ
#*******************************************************

#ФУНКЦИЯ РАСЧЕТА СТАВКИ
#вызыввается каждый раз при выборе любого Combobox


#Функция расчета остстака от предыдущей ставки
def refreshCombo(eventOject):
    summ = summ01.get() + summ02.get() + summ03.get() + summ04.get()
    labelAllMoney["text"] = f"у вас на счету: {int(money - summ)} {valuta}"

    stavka01["values"] = getValues(int(money - summ02.get() - summ03.get() - summ04.get()))
    stavka02["values"] = getValues(int(money - summ01.get() - summ03.get() - summ04.get()))
    stavka03["values"] = getValues(int(money - summ02.get() - summ01.get() - summ04.get()))
    stavka04["values"] = getValues(int(money - summ02.get() - summ03.get() - summ01.get()))

    if (summ01.get() > 0):
        horse01Game.set(True)
    else:
        horse01Game.set(False)

    if (summ02.get() > 0):
        horse02Game.set(True)
    else:
        horse02Game.set(False)

    if (summ03.get() > 0):
        horse03Game.set(True)
    else:
        horse03Game.set(False)

    if (summ04.get() > 0):
        horse04Game.set(True)
    else:
        horse04Game.set(False)
#Список занчений для Combobox

def getValues(summa):
    value = []
    if (summa > 9):
        for i in range(0, 11):
            value.append(i * (int(summa) // 10))
    else:
        value.append(0)
        if (summa > 0):
            value.append(summa)
    return value

#Информация о средствах игрока
def loadMoney():
    try:
        f = open("money.txt", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение {defaultMoney} {valuta}")
        m = defaultMoney
    return m

def saveMoney(moneyToSave):
    try:
        f = open("money.txt", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        print(f"Ошибка создания файла, наш Ипподром закрывается!")
        quit(0)



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
#********************************************
#Значение переменных
#********************************************

WIDTH = 1024
HEIGHT = 600

x01 = 20
x02 = 20
x03 = 20
x04 = 20
#Клички лошадей
nameHorse01 = "Ананас"
nameHorse02 = "Сталкер"
nameHorse03 = "Пирожок"
nameHorse04 = "Копытце"

defaultMoney = 10000
money = 0
valuta = "руб."

#*************************************************************
#ФОРМИРУЕМ ВСЕ ЭЛЕМЕНТЫ ОКНА
#*************************************************************

#размеры окна

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

money = loadMoney()
if (money <= 0):
    messagebox.showinfo("Стоп!", "На ипподром без денег входить нельзя!")
    quit(0)

labelAllMoney = Label(text=f"Осталось средств: {money} {valuta}.", font="Arial 12")
labelAllMoney.place(x=20, y=565)

#Текст и чекбоксы для лошадей.

labelHorse01 = Label(text="Ставка на лошать №1")
labelHorse01.place(x=20, y=450)

labelHorse02 = Label(text="Ставка на лошать №2")
labelHorse02.place(x=20, y=480)

labelHorse03 = Label(text="Ставка на лошать №3")
labelHorse03.place(x=20, y=510)

labelHorse04 = Label(text="Ставка на лошать №4")
labelHorse04.place(x=20, y=540)

#Чекбоксы для лошадок
horse01Game = BooleanVar()
horse01Game.set(0)
horseCheck01 = Checkbutton(text=nameHorse01, variable=horse01Game, onvalue=1, offvalue=0)
horseCheck01.place(x=150, y=448)

horse02Game = BooleanVar()
horse02Game.set(0)
horseCheck02 = Checkbutton(text=nameHorse02, variable=horse02Game, onvalue=1, offvalue=0)
horseCheck02.place(x=150, y=478)

horse03Game = BooleanVar()
horse03Game.set(0)
horseCheck03 = Checkbutton(text=nameHorse03, variable=horse03Game, onvalue=1, offvalue=0)
horseCheck03.place(x=150, y=508)

horse04Game = BooleanVar()
horse04Game.set(0)
horseCheck04 = Checkbutton(text=nameHorse04, variable=horse04Game, onvalue=1, offvalue=0)
horseCheck04.place(x=150, y=538)

#Выпадающий список
stavka01 = ttk.Combobox(root)
stavka02 = ttk.Combobox(root)
stavka03 = ttk.Combobox(root)
stavka04 = ttk.Combobox(root)

#Задаем атрибут только чтение

stavka01["state"] = "readonly"
stavka01.place(x=280, y=450)

stavka02["state"] = "readonly"
stavka02.place(x=280, y=480)

stavka03["state"] = "readonly"
stavka03.place(x=280, y=510)

stavka04["state"] = "readonly"
stavka04.place(x=280, y=540)

#Определяем переменные для хранения значений Combobox

summ01 = IntVar()
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

#привязываем переменные Combobox

stavka01["textvariable"] = summ01
stavka02["textvariable"] = summ02
stavka03["textvariable"] = summ03
stavka04["textvariable"] = summ04

stavka01.bind("<<ComboboxSelected>>", refreshCombo)
stavka02.bind("<<ComboboxSelected>>", refreshCombo)
stavka03.bind("<<ComboboxSelected>>", refreshCombo)
stavka04.bind("<<ComboboxSelected>>", refreshCombo)

#Обновляем занчение combobox

refreshCombo("")

#устанавливаем самое первое значение списка

stavka01.current(0)
stavka02.current(0)
stavka03.current(0)
stavka04.current(0)

root.mainloop()
