# -*- coding: utf-8 -*-
"""
GUI from tkinter
逻辑层
"""

# 设置GUI
root = Tk()
w = Label(root, text = "Guess Number Game")
w.pack()

# 欢迎消息
mb.showinfo("Welcome", "Welcome to Guess Number Game")

# 处理信息
number = 59

while True:
# 让用户输入信息:
    guess = dl.askinteger("Number", "What's your guess?")

    if guess == number:
        output = 'Bingo! you guessed it right, but you do not win any prizes!'
        mb.showinfo("Hint: ", output)
        break
    elif guess < number:
        output = 'No, the number is a  higer than that'
        mb.showinfo("Hint: ", output)
    else:
        output = 'No, the number is a  lower than that'
        mb.showinfo("Hint: ", output)

print('Done')
