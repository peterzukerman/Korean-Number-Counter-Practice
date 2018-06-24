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
    0 : ["students", "명"], # native
    1 : ["dogs", "마리"], # native
    2 : ["books", "권"], # native
    3 : ["things", "개"], # native
    4 : ["chapters", "과"], # sino
    5 : ["floors", "층"], # sino
    6 : ["won", "원"], # sino
}


def questionGenerator(number, counter):
    return "" + str(number) + " " + counter[0]

def answerGenerator(number, counter):
    if counter[0] in [1, 2, 3]:
        dictToUse = NativeNumbers
    else:
        dictToUse = SinoNumbers

    numbersArray = [int(x) for x in str(number)]
    if len(numbersArray) == 2 and number != 10:
        if number >= 40:
            return "" + SinoNumbers[numbersArray[0]] + SinoNumbers[10] + " " + SinoNumbers[numbersArray[1]] + " " + counter[1]
        else:
            return "" + dictToUse[numbersArray[0]] + dictToUse[10] + " " + dictToUse[numbersArray[1]] + " " + counter[1]
    elif len(numbersArray) == 3 and number != 100:
        if numbersArray[1] == 0:
            return "" + SinoNumbers[numbersArray[0]] + SinoNumbers[100] + " " + SinoNumbers[0] + " " + counter[1]
        else:
            return "" + SinoNumbers[numbersArray[0]] + SinoNumbers[100] + " " + SinoNumbers[numbersArray[1]] + SinoNumbers[10] + " " + SinoNumbers[numbersArray[2]] + " " + counter[1]
    return "" + dictToUse[number] + " " + counter[1]

def clicked():
    koreanLine.configure(text=answerGenerator(number, randomCounter))

def clicked2():
    global number
    number = randint(1, 1000)
    global randomCounter
    randomCounter = counterNouns[randint(0, 6)]
    koreanLine.configure(text=questionGenerator(number, randomCounter))

window = Tk()
window.title("Korean Number/Counter App")
window.geometry('350x200')

number = randint(1, 1000)
randomCounter = counterNouns[randint(0, 6)]
koreanLine = ttk.Label(window, text=questionGenerator(number, randomCounter), font=(50))
koreanLine.grid(column = 200, row = 100)
koreanLine.configure(anchor="center")

btn = Button(window, text="Show Answer", command=clicked)
next = Button(window, text="Next", command=clicked2)
btn.grid(column=200, row=150)
next.grid(column = 210, row = 150)
window.mainloop()
