#!/usr/bin/env python
import sys, os
import time

#include my modules
import varVision as varGlobal
import cimage

try:
    MyApp = cimage.CImage(varGlobal.pathToImages)
    assert (MyApp.FileCount != 0), "no files found in image path"
    time.sleep(0.5)
    MyApp.clearInfoWidgets()


    while True:
        MyApp.updateImagePath()

        index = 0
        while index < MyApp.FileCount:
            MyApp.showImage(MyApp.Files[index])
            index = index + 1
            time.sleep(varGlobal.timeToNextImage)

except Exception as e:
    print(e)
