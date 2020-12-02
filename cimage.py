#!/usr/bin/env python
import sys, os
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import varVision as globalVar

class CImage:
    def __init__(self, pathToImage):
        self.path = pathToImage
        self.FileCount = 0
        self.Files = []
        self.updateImagePath()
        self.bProgressIsShown = False
        self.bImageIsShown = False
        self.startUpScreen = globalVar.startUpScreen
        self.mainWindow = Tk()
        self.w = self.mainWindow.winfo_screenwidth()
        self.h = self.mainWindow.winfo_screenheight()
        self.mainWindow.overrideredirect(True)
        self.mainWindow.geometry("%dx%d+0+0" % (self.w, self.h))
        self.mainWindow.focus_set()
        self.mainWindow.configure(background='black',  cursor="none")
        self.showStartup()


    def updateImagePath(self):
        print("updateImagePath %s" % self.path)
        self.FileCount = 0
        self.Files = []
        for r, d, f in os.walk(self.path):
            for file in f:
                if '.jpg' in file:
                    self.Files.append(os.path.join(r, file))
                    self.FileCount = self.FileCount + 1
        print("self.FileCount %s" % self.FileCount)
        print("self.Files %s" % self.Files)


    def showProgressbar(self, Title):

        self.bProgressIsShown = True
        # Label für Progressbar
        self.panel = Label(self.mainWindow, text=Title)
        self.panel.pack(padx=5, pady=10, side=LEFT)

        # Progress bar widget
        self.progress = Progressbar(self.mainWindow, orient = HORIZONTAL, length = self.w, mode = 'determinate')
        self.progress.pack(padx=5, pady=10, side=LEFT)
        self.progress['value'] = 0

        self.mainWindow.update_idletasks()
        self.mainWindow.update()


    def updateProgressbar(self, value):
        self.progress['value'] = value
        self.mainWindow.update_idletasks()
        self.mainWindow.update()


    def clearInfoWidgets(self):
        print("clearInfoWidgets")
        self.startScreen.destroy()
        if self.bProgressIsShown:
            self.panel.destroy()
            self.progress.destroy()

    def showStartup(self):
        print("showStartup")
        Imagefile = Image.open(self.startUpScreen)
        imgWidth, imgHeight = Imagefile.size
        ratio = min(self.w/imgWidth, self.h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        picture = ImageTk.PhotoImage(Imagefile)
        self.startScreen = Label(self.mainWindow)
        self.startScreen.place(relx = 0.5, rely = 0.5,  anchor = "center")
        self.startScreen.configure(image=picture, cursor="none")
        self.startScreen.image = picture
        self.mainWindow.update_idletasks()
        self.mainWindow.update()

    def showImage(self, pathToImage):
        print("showImage: " + pathToImage)
        #cleanup
        if self.bImageIsShown:
            self.imageLabel.destroy()
        Imagefile = Image.open(pathToImage)
        imgWidth, imgHeight = Imagefile.size
        ratio = min(self.w/imgWidth, self.h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        Imagefile = Imagefile.resize((imgWidth,imgHeight), Image.ANTIALIAS)
        picture = ImageTk.PhotoImage(Imagefile)
        self.imageLabel = Label(self.mainWindow)
        self.imageLabel.place(relx = 0.5, rely = 0.5,  anchor = "center")
        self.imageLabel.configure(image=picture, cursor="none")
        self.imageLabel.image = picture
        self.mainWindow.update_idletasks()
        self.mainWindow.update()
        self.bImageIsShown = True


    def showText(self, stext):
        print(stext)
        panel = Label(self.mainWindow, text=stext)
        panel.place(relx = 0.5, rely = 0.5,  anchor = "center")
        self.mainWindow.update_idletasks()
        self.mainWindow.update()
