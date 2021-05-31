from tkinter import Frame, Button, LEFT ,Entry , Text , Label  
from tkinter import filedialog
import cv2

class EditBar(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master)
        self.new_button = Button(self, text="New")
        self.save_button = Button(self, text="Save")
        self.save_as_button = Button(self, text="Save As")
        self.crop_button = Button(self, text="Crop")
        self.rotate_button = Button(self, text="Rotate")
        self.flipping_button = Button(self, text="Flipping")
        self.transform_button = Button(self, text="transformation")
        self.equalizeHist = Button(self , text = "Equalize Hist")
        self.clear_button = Button(self, text="Clear")
        
        
        self.new_button.bind("<ButtonRelease>", self.new_button_released)
        self.save_button.bind("<ButtonRelease>", self.save_button_released)
        self.save_as_button.bind("<ButtonRelease>", self.save_as_button_released)
        self.crop_button.bind("<ButtonRelease>", self.crop_button_released)
        self.flipping_button.bind("<ButtonRelease>", self.flipping_button_released)
        self.rotate_button.bind("<ButtonRelease>", self.rotate_button_released)
        self.equalizeHist.bind("<ButtonRelease>",self.equalizeHist_button_released)
        self.transform_button.bind("<ButtonRelease>", self.transform_button_released)

        self.clear_button.bind("<ButtonRelease>", self.clear_button_released)
        self.new_button.pack(side=LEFT)
        self.save_button.pack(side=LEFT)
        self.save_as_button.pack(side=LEFT)
        self.rotate_button.pack(side = LEFT)
        self.crop_button.pack(side=LEFT)
        self.flipping_button.pack(side=LEFT)
        self.transform_button.pack(side=LEFT)
        self.equalizeHist.pack(side = LEFT)
        self.clear_button.pack()
        
    
    def new_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.new_button:
            if self.master.cropState:
                self.master.image_viewer.DeactiveCropping()
                
            filename = filedialog.askopenfilename()
            image = cv2.imread(filename)

            if image is not None:
                self.master.filename = filename
                self.master.originalImage = image.copy()
                self.master.processedImage = image.copy()
                self.master.image_viewer.show_image()
                self.master.selectedImage = True
                
    def save_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_button: 
            if self.master.selectedImage:
                if self.master.cropState:
                    self.master.image_viewer.DeactiveCropping()
                saving_image = self.master.processedImage
                image_filename = self.master.filename
                cv2.imwrite(image_filename, saving_image)
                
    def save_as_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.save_as_button:
            if self.master.selectedImage:
                if self.master.cropState:
                    self.master.image_viewer.DeactiveCropping()
                original = self.master.filename.split('.')[-1]
                filename = filedialog.asksaveasfilename()
                filename = filename + "." + original

                save_image = self.master.processedImage
                cv2.imwrite(filename, save_image)

                self.master.filename = filename
                
    def flipping_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.flipping_button:
            if self.master.selectedImage:
                if self.master.cropState:
                    self.master.image_viewer.DeactiveCropping()
                else:
                    self.master.image_viewer.flippingImage(self.master.optionBar.getComboxValue())
            
    def rotate_button_released(self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.rotate_button:
            if self.master.selectedImage:
                if self.master.cropState:
                    self.master.image_viewer.DeactiveCropping()
                else:
                    self.master.image_viewer.RotatingImage(self.master.optionBar.getAngleValue())
    
    def crop_button_released (self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.crop_button:
            if self.master.selectedImage:
                if self.master.cropState:
                    self.master.image_viewer.DeactiveCropping()
                else:
                    self.master.image_viewer.ActiveCropping()
                    
    def transform_button_released (self, event):
        if self.winfo_containing(event.x_root, event.y_root) == self.transform_button:
            if self.master.selectedImage :
                if self.master.cropState:
                    self.master.image_viewer.DeactiveCropping()
                else:
                    self.master.image_viewer.ActiveTransform()
                    
                    
                    
    def equalizeHist_button_released(self ,event):
        if self.winfo_containing(event.x_root, event.y_root) == self.equalizeHist :
            if self.master.selectedImage :
                if self.master.cropState:
                    self.master.image_viewer.DeactiveCropping()
                else:
                    self.master.image_viewer.EqualizeImage()
                
                    
    def clear_button_released(self, event):
         self.master.processedImage = self.master.originalImage.copy()
         self.master.image_viewer.show_image()
