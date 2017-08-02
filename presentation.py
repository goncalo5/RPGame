from Tkinter import *


class Presentation(object):
    def __init__(self):
        # initiate settings.screen
        self.root = Tk()
        self.root.title('RPGame')
        self.root.geometry(settings.SCREEN)
        self.root.configure(background='black')

        self.root.mainloop()
