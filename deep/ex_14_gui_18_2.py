import tkinter
from tkinter import filedialog

root = tkinter.Tk()

menubar = tkinter.Menu(root)
root.geometry('200x100')

f = None

filepath = tkinter.StringVar()
filepath.set("filepath")

def openfile():
    global f
    f = filedialog.askopenfile('rb')
    filepath.set(f.name)
     
def saveasfile():
    global f
    a = f.read()
    if a is None:
        return
    else:
        save_f = filedialog.asksaveasfile("wb")
        filepath.set(save_f.name)
        save_f.write(a)
    f.close()
    save_f.close()

def exit():
    root.quit()

label_path = tkinter.Label(root, textvariable = filepath)
label_path.grid(row = 0, column = 0)

menubar = tkinter.Menu(root)
root['menu'] = menubar

menu_file = tkinter.Menu(menubar, tearoff = 0)
menu_edit = tkinter.Menu(menubar, tearoff = 0)
menu_help = tkinter.Menu(menubar, tearoff = 0)

menubar.add_cascade(label = 'File', menu = menu_file)
menubar.add_cascade(label = 'Edit', menu = menu_edit)
menubar.add_cascade(label = 'Help', menu = menu_help)

menu_file.add_command(label = 'open', command = openfile)
menu_file.add_command(label = 'save as', command = saveasfile)
menu_file.add_command(label = 'Exit', command = exit)


root.mainloop()