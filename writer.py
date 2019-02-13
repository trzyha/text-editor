import tkinter as tk

def NewFile():
	print("new file!!")

def OpenFile():
	print("open file!")

def About():
	print("simple text editor")

root = tk.Tk()

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open..", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
helpmenu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=About)


T = tk.Text(root, height=3, width=30)
T.pack()


if __name__ == '__main__':
	tk.mainloop()
