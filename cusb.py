#!/usr/bin/env python
import sys, os
#import RPi.GPIO as GPIO
import time
import shutil
from shutil import ignore_patterns
from tkinter import Label
from datetime import datetime
import varVision as varGlobal

class CUsb:
    def __init__(self,CImage):
        print("INIT CUsb")
        self.CImage = CImage
        self.Files = []
        self.FileCount = 0
        self.Index = 0
        
    def checkforUSB(self):
        print("checkforUSB %s" % varGlobal.pathToUSB)
                
        #need to detect if usb stick is mounted
        usb_names = os.listdir(varGlobal.pathToUSB)
        
        for usbName in usb_names:
            if usbName == "visionUSB":
                print("found usb stick %s and will start transfer" % usbName)
                pathUSB = os.path.join(varGlobal.pathToUSB, usbName)
                
                sourcePathImages = os.path.join(pathUSB, "data")
                #copy image files
                print("copy images from %s to %s" % (sourcePathImages, varGlobal.pathToImages))
                self.clearDir(varGlobal.pathToImages)
                self.getFilestoCopy(sourcePathImages)
                self.CImage.showProgressbar("Copy Images:")
                self.transferDir(sourcePathImages, varGlobal.pathToImages)
                self.CImage.clearInfoWidgets()
        
        
                destPathCamera = os.path.join(os.path.join(varGlobal.pathToUSB, usbName), "cam")
                print("copy camera from %s to %s" % (varGlobal.pathCameraFiles, destPathCamera))
                self.getFilestoCopy(varGlobal.pathCameraFiles)
                self.CImage.showProgressbar("Copy Camera:")
                self.transferDir(varGlobal.pathCameraFiles, destPathCamera)
                #self.clearDir(varGlobal.pathCameraFiles)
                self.CImage.clearInfoWidgets()
                #we finished all transfers
                
            else:
                print("found no valid usbStick")
        
    def transferDir(self, src, dest):
        print("transfer files from %s to %s" % (src,dest))
        
        if os.path.isdir(src):
            if not os.path.isdir(dest):
                os.makedirs(dest)
            files = os.listdir(src)
                
            for f in files:
                    self.transferDir(os.path.join(src, f),os.path.join(dest, f))
        else:
            if(".jpg" in src):
                print("Copy cam ", src, " to ", dest)
                shutil.copyfile(src, dest)
                self.CImage.updateProgressbar((self.Index+1) / self.FileCount * 100)
                self.Index = self.Index + 1
                time.sleep(0.2)
            else:
                print("ignore file %s" % src)
            
        print("FileCount/Index: %s/%s" % (self.FileCount, self.Index))
        
            
    def clearDir(self, pathToClear):
        print("clearDir: " + pathToClear)
        for filename in os.listdir(pathToClear):
            file_path = os.path.join(pathToClear, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        
        
    def getFilestoCopy(self, pathToImages):
        print("getFilestoCopy %s" % pathToImages)
        self.FileCount = 0
        self.Index = 0
        self.Files = []
        for r, d, f in os.walk(pathToImages):
            for file in f:
                if '.jpg' in file:
                    self.Files.append(os.path.join(r, file))
                    self.FileCount = self.FileCount + 1
        print("self.FileCount %s" % self.FileCount)
        print("self.Files %s" % self.Files)


