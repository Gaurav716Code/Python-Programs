from tkinter import *

root = Tk()
root.title("F113 Gaurav Vishwakarma : LabelFrame")
root.geometry("300x300")
labelframe = LabelFrame(root, text="This is a LabelFrame")
labelframe.pack(fill="both", expand="yes")
 
left = Label(labelframe, text="content : F113 Gaurav Vishwakarma")
left.pack()
 
root.mainloop()
