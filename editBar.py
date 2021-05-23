# -*- coding: utf-8 -*-
"""
Created on Sun May 23 05:30:58 2021

@author: Genedy
"""

# =============================================================================
# Edit Options Bar
# =============================================================================
from tkinter import Frame, Button, LEFT
from tkinter import filedialog
import cv2

class EditBar(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        
        self.new_button = Button(self, text="New")
        self.save_button = Button(self, text="Save")
        self.save_as_button = Button(self, text="Save As")
        self.rotate_button = Button(self, text="Rotate")
        self.crop_button = Button(self, text="Crop")
        self.filter_button = Button(self, text="Filter")
        self.adjust_button = Button(self, text="Adjust")
        self.clear_button = Button(self, text="Clear")
        
        self.new_button.pack(side=LEFT)
        self.save_button.pack(side=LEFT)
        self.save_as_button.pack(side=LEFT)
        self.rotate_button.pack(side = LEFT)
        self.crop_button.pack(side=LEFT)
        self.filter_button.pack(side=LEFT)
        self.adjust_button.pack(side=LEFT)
        self.clear_button.pack()