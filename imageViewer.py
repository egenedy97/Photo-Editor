
from tkinter import Frame, Canvas, CENTER, ROUND
from PIL import Image, ImageTk
import cv2
import imutils 
import numpy as np

class ImageViewer(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master=master, bg="gray", width=600, height=400)
        
        self.shown_image = None 
        self.x = 0
        self.y = 0
        self.crop_start_x = 0 
        self.crop_start_y = 0
        self.crop_end_x = 0
        self.crop_end_y = 0
        self.rectangle_id = 0
        self.ratio = 0
        self.coord = []
        self.dot =[]
        self.canvas = Canvas(self, bg="gray", width=1000, height=600)
        self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    
    def show_image(self, img=None):
        self.clear_canvas()

        if img is None:
            image = self.master.processedImage.copy()
        else:
            image = img

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels = image.shape
        ratio = height / width

        new_width = width
        new_height = height

        if height > self.winfo_height() or width > self.winfo_width():
            if ratio < 1:
                new_width = self.winfo_width()
                new_height = int(new_width * ratio)
            else:
                new_height = self.winfo_height()
                new_width = int(new_height * (width / height))

        self.shown_image = cv2.resize(image, (new_width, new_height))
        self.shown_image = ImageTk.PhotoImage(Image.fromarray(self.shown_image))

        self.ratio = height / new_height

        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(new_width / 2, new_height / 2, anchor=CENTER, image=self.shown_image)
    
    
    def ActiveCropping(self):
        self.canvas.bind("<ButtonPress>", self.start_crop)
        self.canvas.bind("<B1-Motion>", self.crop)
        self.canvas.bind("<ButtonRelease>", self.end_crop)

        self.master.cropState = True
        
    
    def DeactiveCropping(self):
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")

        self.master.cropState = False
    
    def start_crop(self, event):
        self.crop_start_x = event.x
        self.crop_start_y = event.y
    
    
    def crop(self, event):
        if self.rectangle_id:
            self.canvas.delete(self.rectangle_id)

        self.crop_end_x = event.x
        self.crop_end_y = event.y

        self.rectangle_id = self.canvas.create_rectangle(self.crop_start_x, self.crop_start_y,
                                                         self.crop_end_x, self.crop_end_y, width=1)

    def end_crop(self, event):
        if self.crop_start_x <= self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x > self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x <= self.crop_end_x and self.crop_start_y > self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)
        else:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)

        x = slice(start_x, end_x, 1)
        y = slice(start_y, end_y, 1)

        self.master.processedImage = self.master.processedImage[y, x]

        self.show_image()

    def flippingImage(self ,var ):       
        self.master.processedImage = cv2.flip(self.master.processedImage,var)
        self.show_image()

    def RotatingImage(self , val) :
        self.master.processedImage = imutils.rotate(self.master.processedImage, angle=val)
        self.show_image() 
    
        
    def EqualizeImage(self):
       
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        self.master.processedImage = clahe.apply(self.master.processedImage)
        self.show_image() 
    
    def ActiveTransform(self) :
        self.canvas.bind("<Button 1>",self.insertCoords)
        self.canvas.bind("<Button 3>",self.removeCoords)
    
    def DeactiveTransform(self):
        self.canvas.unbind("<Button 1>",self.insertCoords)
        self.canvas.unbind("<Button 3>",self.removeCoords)
        
    def insertCoords(self ,event):
        self.coord.append([event.x, event.y])
        r=3
        self.dot.append(self.canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r, fill="#ff0000"))         #print circle
        if (len(self.coord) == 4):
            self.Transformer()
            self.canvas.delete("all")
            self.canvas.create_image(0,0,image=self.result,anchor="nw")
            self.master.processedImage = self.result    
            
    def removeCoords(self, event=None):
        del self.coord[-1]
        self.canvas.delete(self.dot[-1])
        del self.dot[-1]
        
        
    def Transformer(self):
        cv2.circle(self.master.processedImage , tuple(self.coord[0]), 5, (0, 0, 255), -1)
        cv2.circle(self.master.processedImage , tuple(self.coord[1]), 5, (0, 0, 255), -1)
        cv2.circle(self.master.processedImage , tuple(self.coord[2]), 5, (0, 0, 255), -1)
        cv2.circle(self.master.processedImage , tuple(self.coord[3]), 5, (0, 0, 255), -1)
        
                
        widthA = np.sqrt(((self.coord[3][0] - self.coord[2][0]) ** 2) + ((self.coord[3][1] - self.coord[2][1]) ** 2))
        widthB = np.sqrt(((self.coord[1][0] - self.coord[0][0]) ** 2) + ((self.coord[1][1] - self.coord[0][1]) ** 2))
        maxWidth = max(int(widthA), int(widthB))
         
        heightA = np.sqrt(((self.coord[1][0] - self.coord[3][0]) ** 2) + ((self.coord[1][1] - self.coord[3][1]) ** 2))
        heightB = np.sqrt(((self.coord[0][0] - self.coord[2][0]) ** 2) + ((self.coord[0][1] - self.coord[2][1]) ** 2))
        maxHeight = max(int(heightA), int(heightB))
     
        print(self.coord)
        
        pts1 = np.float32(self.coord)    
        pts2 = np.float32([[0, 0], [maxWidth-1, 0], [0, maxHeight-1], [maxWidth-1, maxHeight-1]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        self.result_cv = cv2.warpPerspective(self.master.processedImage, matrix, (maxWidth,maxHeight))
        result_rgb = cv2.cvtColor(self.result_cv, cv2.COLOR_BGR2RGB)
        self.result = ImageTk.PhotoImage(image = Image.fromarray(result_rgb))
        
            
    def clear_canvas(self):
        self.canvas.delete("all")
        
        
        
        