# -*- coding: utf-8 -*-
"""
Created on Sun May 23 05:30:58 2021

@author: Genedy
"""

# =============================================================================
# Edit Options Bar
# =============================================================================
from tkinter import Frame, Button, LEFT ,Entry
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
        self.flipping_button = Button(self, text="Flipping")
        self.transform_button = Button(self, text="transformation")
        self.clear_button = Button(self, text="Clear")
        
        self.new_button.bind("<ButtonRelease>", self.new_button_released)
        self.save_button.bind("<ButtonRelease>", self.save_button_released)
        self.save_as_button.bind("<ButtonRelease>", self.save_as_button_released)
# =============================================================================
#         self.rotate_button.bind("<ButtonRelease>", self.rotate_button_released)
#         self.crop_button.bind("<ButtonRelease>", self.crop_button_released)
#         self.flipping_button.bind("<ButtonRelease>", self.flipping_button_released)
#         self.transform_button.bind("<ButtonRelease>", self.transform_button_released)
# =============================================================================
        self.clear_button.bind("<ButtonRelease>", self.clear_button_released)
        
        self.new_button.pack(side=LEFT)
        self.save_button.pack(side=LEFT)
        self.save_as_button.pack(side=LEFT)
        self.rotate_button.pack(side = LEFT)
#        self.angle.pack(side=LEFT)
        self.crop_button.pack(side=LEFT)
        self.flipping_button.pack(side=LEFT)
        self.transform_button.pack(side=LEFT)
        self.clear_button.pack()
        
    
    def new_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.new_button:
            filename = filedialog.askopenfilename()
            image = cv2.imread(filename)

            if image is not None:
                self.master.filename = filename
                print(filename)
                self.master.original_image = image.copy()
                self.master.processed_image = image.copy()
                self.master.image_viewer.show_image()
                self.master.is_image_selected = True
                
    def save_button_released(self, event):
        print("save action")

    def save_as_button_released(self, event):
        print("save as action")
                
    def clear_button_released(self, event):
        print("Clear Images")
