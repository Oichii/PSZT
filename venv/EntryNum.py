from tkinter import *
import tkinter.ttk as ttk

class EntryNum(ttk.Entry):
    def __init__(self, master, text=''):
        super().__init__(master, validate='key', validatecommand=(master.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))
        self.insert(END, text)

    def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if len(value_if_allowed) == 0:
            return True
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
        
    def getNum(self):
        if len(self.get()) == 0:
            return 0
        else:
            return int(self.get())
