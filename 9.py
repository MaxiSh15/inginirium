from tkinter import *


def change_text():
    user_name = name_entry.get()
    if user_name != '':

        name_text['text'] = 'Hello, ' + user_name + '!'


root = Tk()
root.geometry("400x300")
root.title("Hello user!")
root.config(bg='grey')


name_text = Label(root, text='Please, enter your name!',
                  bg='grey', fg='white', font=('Calibri', 24))
name_text.pack(side='top', anchor='n')

name_entry = Entry(root)
name_entry.pack(anchor='center', pady=50)

change_name = Button(root, text='Change name', command=change_text)
change_name.pack(side='bottom', anchor='s')


root.mainloop()
