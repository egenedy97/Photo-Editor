# -*- coding: utf-8 -*-
"""
Created on Sun May 23 05:10:04 2021

@author: Genedy
"""
import tkinter as tk
from tkinter import ttk
from editBar import EditBar
from imageViewer import ImageViewer
from option import OptionBar

class Main(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Assignment1-PhotoEditor")
        self.filename = ""
        self.original_image = None
        self.processed_image = None
        self.is_image_selected = False
        self.is_crop_state = False
        self.is_transform_state = False 
        self.optionBar = OptionBar(master = self)
        self.editBar = EditBar(master = self)
        sep = ttk.Separator(master=self, orient=tk.HORIZONTAL)
        sep2 = ttk.Separator(master=self, orient=tk.HORIZONTAL)
        self.image_viewer = ImageViewer(master=self)
        self.optionBar.pack(pady= 10)
        sep2.pack(fill=tk.X , padx =20 , pady=5)
        self.editBar.pack(pady=10)
        sep.pack(fill=tk.X , padx =20 , pady=5)
        self.image_viewer.pack(fill=tk.BOTH, padx=20, pady=10, expand=1)
        
