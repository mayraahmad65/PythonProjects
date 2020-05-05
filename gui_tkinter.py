# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:14:36 2020

@author: Mayra
"""
import tkinter as tk
parent = tk.Tk()
parent.title("welcome")
parent.geometry('600x300')
my_label = tk.Label(parent,text="Label widget", font=("Times New Roman", 24))
my_label.grid(column=0, row=0)
parent.mainloop()
