import sys
from random import randint
import random
import time
from tkinter import *
from tkinter import ttk

SinoNumbers = {
    0 : "",
    1 : "일",
    2 : "이",
    3 : "삼",
    4 : "사",
    5 : "오",
    6 : "육",
    7 : "칠",
    8 : "팔",
    9 : "구",
    10 : "십",
    100 : "백",
    1000 : "천",
    10000 : "만"
}

NativeNumbers = {
    0 : "",
    1 : "하나",
    2 : "둘",
    3 : "셋",
    4 : "넷",
    5 : "다섯",
    6 : "여섯",
    7 : "일곱",
    8 : "여덟",
    9 : "아홉",
    10 : "열",
    20 : "스물",
    30 : "서른",
}

counterNouns = {
    0 : ["students", "명"], #native
    1 : ["dogs", "마리"], #native
    2 : ["books", "권"], #native
    3 : ["things", "개"], #native
    4 : ["chapters", "과"], #sino
    5 : ["floors", "층"], #sino
    6 : ["won", "원"], #sino
}
number = 0
randomCounter = counterNouns[1]
dictToUse = SinoNumbers

def getDigit(digit, dictionary):
    if dictionary=="SinoNumbers":
        return SinoNumbers[digit]
    elif dictionary=="NativeNumbers":
        return NativeNumbers[digit]
    else:
        return

def setRandomVars():
    number = randint(1, 10)
    randomCounter = counterNouns[randint(0, 6)]

def questionGenerator():
    if randomCounter==0 or randomCounter==1 or randomCounter==2 or randomCounter==3:
        dictToUse = NativeNumbers
    else:
        dictToUse = SinoNumbers
    return "" + str(number) + " " + randomCounter[0]

def answerGenerator():
    return "" + dictToUse[number] + " " + randomCounter[1]

def clicked():
    koreanLine.configure(text=answerGenerator())

def clicked2():
    setRandomVars()
    koreanLine.configure(text=questionGenerator())

window = Tk()
window.title("Korean Number/Counter App")
window.geometry('350x200')

setRandomVars()

koreanLine = ttk.Label(window, text=questionGenerator(), font=(50))
koreanLine.grid(column = 200, row = 100)
koreanLine.configure(anchor="center")

btn = Button(window, text="Show Answer", command=clicked)
next = Button(window, text="Next", command=clicked2)
btn.grid(column=200, row=150)
next.grid(column = 210, row = 150)
window.mainloop()
