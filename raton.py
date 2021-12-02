# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 08:06:57 2021

@author: Francisco
"""

import win32api
from time import sleep

savedpos = win32api.GetCursorPos()
count = 0
while(True):

    curpos = win32api.GetCursorPos()
    if savedpos != curpos:
        count = count +1
        savedpos = curpos
        print("Mouse Movement # ", count)
    sleep(0.05)