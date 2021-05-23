# -*- coding: utf-8 -*-
"""
Created on Sun May 23 05:10:04 2021

@author: Genedy
"""
import tkinter as tk
from tkinter import ttk
from editBar import EditBar
from imageViewer import ImageViewer

class Main(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Basic Image Editor")
# =============================================================================
#       Option Bar
# =============================================================================
        self.editBar = EditBar(master = self)
# =============================================================================
#         Separator Object
# =============================================================================
        
        sep = ttk.Separator(master=self, orient=tk.HORIZONTAL)
# =============================================================================
#         Canvas For Images 
# =============================================================================
        self.image_viewer = ImageViewer(master=self)
        
        self.editBar.pack(pady=10)
        sep.pack(fill=tk.X , padx =20 , pady=5)
        self.image_viewer.pack(fill=tk.BOTH, padx=20, pady=10, expand=1)
