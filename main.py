from tkinter import *

class MyGUI:

    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Knowledge Constructor")
        self.label_1 = Label(self.main_window, text = 'Link', width=45)
        self.label_1.pack()
        self.entry_1 = Entry(self.main_window, width = 45)
        self.entry_1.pack()
        self.but_1 = Button(self.main_window, text = 'Add to base', width=38, command = self.add_to_base)
        self.but_1.pack()
        self.but_2 = Button(self.main_window, text = 'Get from base', width=38, command = self.get_from_base)    
        self.but_2.pack()
        self.but_3 = Button(self.main_window, text = 'Edit link', width=38, command = self.get_from_base)    
        self.but_3.pack()
        self.txt_1 = Text(self.main_window, height=10, width=34)
        self.txt_1.pack()
        self.label_2 = Label(self.main_window, text = 'Source', width=45)
        self.label_2.pack()
        self.entry_2 = Entry(self.main_window, width = 45)
        self.entry_2.pack()
        self.but_4 = Button(self.main_window, text = 'Clean Source', width=38, command = self.add_to_base)
        self.but_4.pack()
        self.label_3 = Label(self.main_window, text = 'object1, object2, object3', width=45)
        self.label_3.pack()
        self.label_3.bind("<Button-1>",self.open_url)

    def add_to_base():
        pass

    def get_from_base():
        pass

    def open_url(url):
        pass

counter = 0
main_window = Tk()
gui = MyGUI(main_window)
main_window.mainloop()
