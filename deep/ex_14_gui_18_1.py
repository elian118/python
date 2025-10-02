import tkinter
from tkinter import messagebox

root = tkinter.Tk()

menubar = tkinter.Menu(root)
root['menu'] = menubar

menu_file = tkinter.Menu(menubar, tearoff = 0)
menu_edit = tkinter.Menu(menubar, tearoff = 0)
menu_help = tkinter.Menu(menubar, tearoff = 0)

menubar.add_cascade(label = 'File', menu = menu_file)
menubar.add_cascade(label = 'Edit', menu = menu_edit)
menubar.add_cascade(label = 'Help', menu = menu_help)

menu_file.add_command(label = 'open')
menu_file.add_command(label = 'save as')
menu_file.add_command(label = 'Exit')


root.mainloop()