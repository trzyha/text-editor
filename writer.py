import tkinter as tk
from tkinter import filedialog ##filedialog is tkinter dialog module needs to be imported seperetly

def NewFile():
	T.delete(1.0, tk.END)

def OpenFile():
	print("open file!")
	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
	f = open(root.filename) ##opening file choosen from dialog
	T.insert(1.0, f.read()) ##insert to text widget choosen file

def About():
	print("simple text editor")

def Save():
	print("save")

def SaveAs():
	root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
	f = open(root.filename)
	

root = tk.Tk()

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open..", command=OpenFile)
filemenu.add_command(label="Save..", command=OpenFile)
filemenu.add_command(label="Save as..", command=SaveAs)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=About)


T = tk.Text(root, height=30, width=100)
T.pack(expand = tk.YES, fill = tk.BOTH) ## expand - expand in y axis, fill - expand in x axis


if __name__ == '__main__':
	tk.mainloop()
