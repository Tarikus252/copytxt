from re import L
import clipboard as clip
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import keyboard
import time


#File Selector
Tk().withdraw() 
filepath = askopenfilename()
print("Selected file: " + filepath)


curline = 0
hotkey = "ctrl + v"
thisline = 0
file = open(filepath, 'r')
line = file.readlines()
print(line)

#Count Lines
while True: 
        if keyboard.is_pressed(L):
                file.close()
                exit()
        if keyboard.is_pressed(hotkey):
                thisline = line[curline]
                clip.copy(thisline)
                print(line[curline])
                curline += 1
                time.sleep(1)

