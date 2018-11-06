from tkinter import *
from add_to_base import add_to_base
from get_from_base import get_from_base
from edit_link import edit_link

class MyGUI:

    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Context")
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
        self.but_4 = Button(self.main_window, text = 'Clean source', width=38, command = self.clean_source)
        self.but_4.pack()
        self.counter = 2

    def add_to_base(self):
        add_to_base(self.entry_1.get(), self.txt_1.get("1.0",END), self.entry_2.get())
        self.counter += 1
        exec("self.label_" + str(self.counter) + " = Label(self.main_window, text = '" + self.entry_1.get() + "', anchor=W, width=40)")
        exec("self.label_" + str(self.counter) + ".pack()")
        exec("self.label_" + str(self.counter) + ".bind('<Button-1>', lambda x, self = self: self.set_text(self.label_" + str(self.counter) +  ".cget('text')))")
        self.entry_1.delete(0, END)
        self.txt_1.delete('1.0', END)

    def get_from_base(self):
        list_of_links = get_from_base(self.entry_1.get())
        list_of_links.sort()
        for name in list_of_links:
            self.txt_1.insert(END, name + "\n")

    def edit_link():
        pass

    def clean_source(self):
        self.entry_2.delete(0, END)

    def set_text(self, text):
        self.entry_1.delete(0,END)
        self.entry_1.insert(0,text)
        return

counter = 0
main_window = Tk()
gui = MyGUI(main_window)
main_window.mainloop()
