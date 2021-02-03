from tkinter import *

root = Tk()
root.title("F113 Gaurav Vishwakarma : Text Widget")
root.geometry("400x300")
text = Text(root, relief=RAISED)
text.insert(INSERT, "Hello...")
text.insert(END, "Everyone...")
text.pack()
root.mainloop()
