#!/usr/bin/python
from os import chdir
from os import path
import glob
import re

class FolderListing:

    @property
    def folderlist(self):
        return self.folder_list
   
    def __init__(self):
        self.folder_list = []

        self.userPath = ""
        self.sysPath = ""
        self.test = 50

        if self.checkPath(path.expanduser("~/.config/awesome/themes/")):
            self.userPath = path.expanduser("~/.config/awesome/themes/*")
            
        if self.checkPath("/usr/share/awesome/themes/"):
            self.sysPath = "/usr/share/awesome/themes/*"

        i=0
        for filename in glob.glob(self.userPath):
            if self.checkPath(filename):
                print(i, filename) 
                self.folder_list.append(filename)
                i=i+1
                
        for filename in glob.glob(self.sysPath):
            if self.checkPath(filename):
                print(i, filename) 
                self.folder_list.append(filename)
                i=i+1

                
    def checkPath(self, p):
        if(path.exists(p) and path.isdir(p)):
            return True
        else:
            return False

    def convertStr(self, s):
        try:
            result = int(s)
            if result<0 or result>=len(self.folder_list):
                print("Choisissez un nombre parmi ceux proposés !")
                result = -1
        except ValueError:
            result = -1
            print("Choisissez un nombre parmi ceux proposés !")
        return result

    def defineTheme(self, p):
        #rcLuaOld = open(path.expanduser("~/.config/awesome/rc.lua"), "r")
        f = open(path.expanduser("~/.config/awesome/rc.lua"), "r")
        rcLuaOld = f.read()
        f.close()
        
        rcLuaNew = re.sub('(beautiful\\.init)'+'(\\()'+'.*?'+'(\\))' ,"beautiful.init("+"\""+p+"/theme.lua\")", rcLuaOld)
        
        f = open(path.expanduser("~/.config/awesome/rc.lua"), "w")
        f.write(rcLuaNew)
        f.close()
        


        def commandline(self):
            inputVar = input("Number of theme to install (0 par defaut) : ")
            iv = self.convertStr(inputVar)

            while iv==-1 or iv<0 or iv>=len(self.folder_list):
                inputVar = input("Number of theme to install (0 par defaut) : ")
                iv = self.convertStr(inputVar)

            print("ok")
            self.defineTheme(self.folder_list[iv])

