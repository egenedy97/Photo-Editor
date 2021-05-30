# -*- coding: utf-8 -*-
"""
Created on Sun May 30 10:24:19 2021

@author: Genedy
"""
from tkinter import Frame, Button, LEFT ,Entry , Text , Label 
from tkinter.ttk import Combobox
import cv2

class OptionBar(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.angleLabel = Label(self, text = "Angle:")
        self.flipDirection = Label(self, text ="Direction Flip : ")
        self.data = ( 0 ,1 )
        self.array = []
        for val in range(0,360):
            self.array.append(val)
            
        self.data2 = tuple(self.array)
        self.cb = Combobox(self , values = self.data)
        self.cb2 = Combobox(self , values = self.data2)
        self.angleLabel.pack(pady = 10)
        self.flipDirection.pack() 
        self.cb.pack()
        self.cb.set(1)
        self.cb2.pack()
        self.cb2.set(45)
        
    def getComboxValue (self):
        return int(self.cb.get())
    
    def getAngleValue (self):
        return int(self.cb2.get())
    