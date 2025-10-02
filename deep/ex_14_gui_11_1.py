import tkinter

def callback():
    root.title('Hello Python')

root = tkinter.Tk()
frame = tkinter.Frame(root, padx = 100, pady = 50)
frame.pack()

label = tkinter.Label(frame, text = 'click')
label.pack()
button = tkinter.Button(frame, text = 'Click')
button.pack()

button.bind("<ButtonPress-1>", lambda e: callback())
button.bind("<Double-1>", lambda e: root.title("Mouse Double Click"))
button.bind("<ButtonPress-3>", lambda e: root.title("Mouse Right Click"))
label.bind("<Double-2>", lambda e: root.title("tkinter Label event")) # 라벨 위에서 마우스 휠 버튼을 더블 클릭하면 반영됨

root.mainloop()