#!/usr/bin/python
import argparse
from gi.repository import Gtk
from os import path
import themeChooser

class Handler:

    def __init__(self, fol):
        self.f = fol
        
    def on_mainWindow_quit(self, *args):
        Gtk.main_quit(*args)

    def on_comboboxAwesomeTheme_changed(self, widget):
        self.f.defineTheme(self.f.folderlist[int(widget.get_active_id())])
        

def main():

    f = themeChooser.FolderListing()
    
    builder = Gtk.Builder()
    builder.add_from_file("ui.glade")
    builder.connect_signals(Handler(f))
    
    comboboxAwesomeTheme = builder.get_object("comboboxAwesomeTheme")
    
    i = 0
    for name in f.folderlist:
        comboboxAwesomeTheme.append(str(i), path.basename(name))
        i+=1
    
    comboboxAwesomeTheme.set_active(0)
    
    window = builder.get_object("mainWindow")
    window.show_all()

    Gtk.main()



if  __name__ =='__main__':
    main()
