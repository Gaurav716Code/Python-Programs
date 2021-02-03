from tkinter import *


root = Tk()
root.title("F113 Gaurav Vishwakarma : Label")
root.geometry("200x200")
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set( "Gaurav Vishwakarma!!!" )
label.pack()
root.mainloop()
