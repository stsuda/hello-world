#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:12:37 2019

@author: Lorenzo Aldeco and Andres Jurado
"""

from pygame import mixer
import time, os

os.system("pip install pygame")  

mixer.init()
file = 'sounds/chinese-gong-daniel_simon.mp3'
mixer.music.load(file)

while True:
    mixer.music.play()
    time.sleep(15)
