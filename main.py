from tkinter import *
from add_to_base import add_to_base
from get_from_base import get_from_base
from edit_link import edit_link
from keywords_extraction import keywords_extraction

class MyGUI:

    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Context")
        self.main_window.configure(background='green')
        self.label_1 = Label(self.main_window, text = 'Link', width=45, bg="green")
        self.label_1.pack()
        self.entry_1 = Entry(self.main_window, width = 45)
        self.entry_1.pack()
        self.but_1 = Button(self.main_window, text = 'Keywords Extaction', width=38, command = self.keywords_extraction, bg="green")
        self.but_1.pack()
        self.but_2 = Button(self.main_window, text = 'Add to base', width=38, command = self.add_to_base, bg="green")
        self.but_2.pack()
        self.but_3 = Button(self.main_window, text = 'Get from base', width=38, command = self.get_from_base, bg="green")    
        self.but_3.pack()
        self.but_4 = Button(self.main_window, text = 'Edit link', width=38, command = self.edit_link, bg="green")    
        self.but_4.pack()
        self.txt_1 = Text(self.main_window, height=10, width=40)
        self.txt_1.pack()
        self.label_2 = Label(self.main_window, text = 'Source', width=45, bg="green")
        self.label_2.pack()
        self.entry_2 = Entry(self.main_window, width = 45)
        self.entry_2.pack()
        self.but_5 = Button(self.main_window, text = 'Clean source', width=38, command = self.clean_source, bg="green")
        self.but_5.pack()
        self.but_6 = Button(self.main_window, text = 'Clean history', width=38, command = self.clean_history, bg="green")
        self.but_6.pack()
        self.counter = 2

    def add_to_base(self):
        add_to_base(self.entry_1.get().lower(), self.txt_1.get("1.0",END), self.entry_2.get())
        self.counter += 1
        exec("self.label_" + str(self.counter) + " = Label(self.main_window, text = '" + self.entry_1.get() + "', anchor=W, width=40, bg='green')")
        exec("self.label_" + str(self.counter) + ".pack()")
        exec("self.label_" + str(self.counter) + ".bind('<Button-1>', lambda x, self = self: self.set_text(self.label_" + str(self.counter) +  ".cget('text')))")
        self.entry_1.delete(0, END)
        self.txt_1.delete('1.0', END)

    def get_from_base(self):
        self.txt_1.delete('1.0', END)
        list_of_links = get_from_base(self.entry_1.get().lower())
        for name in list_of_links:
            self.txt_1.insert(END, name + "\n")

    def edit_link(self):
        links, text, source = edit_link(self.entry_1.get())
        self.entry_1.delete(0, END)
        self.entry_1.insert(0, links)
        self.txt_1.delete('1.0', END)
        self.txt_1.insert(END, text)
        self.entry_2.delete(0, END)
        self.entry_2.insert(0, source)
        

    def clean_source(self):
        self.entry_2.delete(0, END)

    def clean_history(self):
        self.counter = 2
        if hasattr(self, 'label_3'):
            self.label_3.pack_forget()
        if hasattr(self, 'label_4'):
            self.label_4.pack_forget()
        if hasattr(self, 'label_5'):
            self.label_5.pack_forget()
        if hasattr(self, 'label_6'):
            self.label_6.pack_forget()
        if hasattr(self, 'label_7'):
            self.label_7.pack_forget()
        if hasattr(self, 'label_8'):
            self.label_8.pack_forget()
        if hasattr(self, 'label_9'):
            self.label_9.pack_forget()
        if hasattr(self, 'label_10'):
            self.label_10.pack_forget()
        if hasattr(self, 'label_11'):
            self.label_11.pack_forget()
        if hasattr(self, 'label_12'):
            self.label_12.pack_forget()
        if hasattr(self, 'label_13'):
            self.label_13.pack_forget()
        if hasattr(self, 'label_14'):
            self.label_14.pack_forget()
        if hasattr(self, 'label_15'):
            self.label_15.pack_forget()
        if hasattr(self, 'label_16'):
            self.label_16.pack_forget()
        if hasattr(self, 'label_17'):
            self.label_17.pack_forget()
        

    def set_text(self, text):
        self.entry_1.delete(0,END)
        self.entry_1.insert(0,text)
        return

    def keywords_extraction(self):
        text, links = keywords_extraction(self.txt_1.get("1.0",END))
        self.entry_1.delete(0, END)
        self.entry_1.insert(0, links)
        self.txt_1.delete('1.0', END)
        self.txt_1.insert(END, text)

counter = 0
main_window = Tk()
gui = MyGUI(main_window)
main_window.mainloop()
