import tkinter

root = tkinter.Tk()
bt = tkinter.Button(root, text="Quit")
bt.grid(row=2, column=2)
root.geometry("100x100")
root.minsize(100, 100)
root.maxsize(100, 100)

# frame = tkinter.Frame(root, height=100, width=100, relief='sunken',
#                       bd=2, bg='#D9E5FF')
# frame.pack()  # 배치관리자 pack 호출
root.mainloop()  # root와 그에 포함된 자식부품들의 상태를 계속해서 갱신한다.
