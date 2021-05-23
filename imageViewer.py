# -*- coding: utf-8 -*-
"""
Created on Sun May 23 05:55:48 2021

@author: Genedy
"""

from tkinter import Frame, Canvas, CENTER, ROUND
from PIL import Image, ImageTk
import cv2

class ImageViewer(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master, bg="gray", width=600, height=400)
        
        self.shown_image = None 
        self.x = 0
        self.y = 0 
        self.crop_start_x = 0 
        self.crop_start_y = 0
        self.canvas = Canvas(self, bg="gray", width=600, height=400)
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)