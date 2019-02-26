import tkinter as tk
from tkinter import filedialog ##filedialog is tkinter dialog module needs to be imported seperetly
import tkinter.messagebox

a = 1

filename = ""

def NewFile():
	T.delete(1.0, tk.END)

def OpenFile():
	T.delete(1.0, tk.END)
	print("open file!")
	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
	f = open(root.filename) ##opening file choosen from dialog
	T.insert(1.0, f.read()) ##insert to text widget choosen file

def About():
	print("simple text editor")

def SaveFile():
        if root.filename == "no_file":
                self.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file", filetypes = (("text files","*.txt"),("all files","*.*")))
                if root.filename is None:
                        return
                f = open(filename, "w") ##opens file
                f.write(T.get(1.0, "end")) ##write to file till EOF
                f.close() ##closes the file
	
def SaveAsFile():
	root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file", filetypes = (("text files","*.txt"),("all files","*.*")))
	f = open(root.filename, "w")
	f.write(T.get(1.0, "end"))
	f.close()
	
def AddLine(event): ##needs to be event to pass the key
	global a
	a=a+1
	print (23)
	L["text"] = ("Rows: %s" %(a))

def AskQuit():
	if tkinter.messagebox.askokcancel("Quit", "Do you really want to quit?"):
		root.destroy()


root = tk.Tk()
root.title("Notepad --")
root.protocol("WM_DELETE_WINDOW", AskQuit)


root.geometry("500x500") ##sets window initial size 
menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open..", command=OpenFile)
filemenu.add_command(label="Save..", command=SaveFile)
filemenu.add_command(label="Save as..", command=SaveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=About)


T = tk.Text(root, height=1, width=100)
T.pack(expand = tk.YES, fill = tk.BOTH) ## expand - expand in y axis, fill - expand in x axis

L = tk.Label(root, height=1, relief=tk.RIDGE, text="Row: " + str(a), anchor="e")
L.pack(fill = tk.BOTH)

T.bind("<Return>",AddLine) ##counting enter presses

if __name__ == '__main__':
	tk.mainloop()
