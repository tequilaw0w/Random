import random
from tkinter import *


class app():
    def __init__(self):
        self.root = Tk()
        self.root.title("random")
        self.root.minsize(400, 300)
        self.create_random_box()
        self.create_result_label()
        self.root.mainloop()


    def create_random_box(self):
        self.random_box = Label()
        self.random_btn = Button(text='Рандом')
        self.random_btn.bind('<Button>', self.get_random) #забиндили свзяь "нажатие кнопки с функцией гетрандом"
        self.random_box.pack()
        self.random_btn.pack()


    def create_result_label(self):
        empty_label = Label()
        empty_label.pack()
        self.random_label = Label()
        self.random_label.pack()


    def get_random(self, event):
        club_members = ['Artem', 'Stepan', 'Marina']
        message = random.choice(club_members)
        self.random_label.config(text=message)



app()
