#!/usr/bin/python
from os import chdir
from os import path
import glob
import re

class FolderListing:

    @property
    def folderList(self):
        return self.folder_list
   
    @property
    def actualTheme(self):
        return self.actual_theme
    
    @property
    def rcLua(self):
        return self.rc_lua

    def __init__(self):
        self.folder_list = []

        self.userPath = ""
        self.sysPath = ""
        self.actual_theme = self.extractActualTheme()
        self.rc_lua = path.expanduser("~/.config/awesome/rc.lua")
        
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
        f = open(self.rc_lua, "r")
        rcLuaOld = f.read()
        f.close()
        
        rcLuaNew = re.sub('(beautiful\\.init)'+'(\\()'+'.*?'+'(\\))' ,"beautiful.init("+"\""+p+"/theme.lua\")", rcLuaOld)
        
        f = open(self.rc_lua, "w")
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


    def extractActualTheme(self):
        f = open(self.rc_lua, "r")
        re1='(beautiful\\.init)'	# Fully Qualified Domain Name 1
        re2='(\\()'	# Any Single Character 1
        re3='.*?'	# Non-greedy match on filler
        re4='((?:\\/[\\w\\.\\-]+)+)'	# Unix Path 1
        re5='.*?'	# Non-greedy match on filler
        re6='(\\))'	# Any Single Character 2
        
        rg = re.compile(re1+re2+re3+re4+re5+re6,re.IGNORECASE|re.DOTALL)

        rcLua = f.read()

        f.close()
        m = rg.search(rcLua)

        if m:
            fqdn1=m.group(1)
            c1=m.group(2)
            unixpath1=m.group(3)
            c2=m.group(4)
            print ("("+fqdn1+")"+"("+c1+")"+"("+unixpath1+")"+"("+c2+")"+"\n")
        return unixpath1
