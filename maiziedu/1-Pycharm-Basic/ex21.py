# -*- coding: utf-8 -*-
"""
GUI： Graphical User Interface
tkinter: GUI library for Python
GUI Example
"""
from EasyTkinter import *                                       # python2.7 查无此包
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

# tkinter GUI Input Output Example
# 设置GUI
root = Tk()
w = Label(root, text = "Label Title")
w.pack()

# 欢迎消息
mb.showinfo("Welcome", "Welcome Message")
guess = dl.askinteger("Number", "Enter a number")

output = 'This is output message'
mb.showinfo("Output: ", output)
