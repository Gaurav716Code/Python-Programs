from tkinter import *

root = Tk()
root.title("F113 Gaurav Vishwakarma : Entry Widget")
##root.geometry("400x400")
L1 = Label(root, text="username")
L1.pack(side = LEFT)
E1 = Entry(root, bd=6)
E1.pack(side = RIGHT)

root.mainloop()
