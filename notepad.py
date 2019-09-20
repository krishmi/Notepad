from tkinter import *
from tkinter import ttk,filedialog

def newFile():
	pass

def openFile():
	filename = filedialog.askopenfilename(initialdir='home/', title="Select file..")
	tab = Text(notebook)
	notebook.add(tab1, text=filename)
	with open(filename) as f:
		text = f.read()
		tab.insert(INSERT, text)

def closeFile():
	pass

#root
root = Tk()
root.title('Notepad')
mainframe = ttk.Frame(root, height=500, width=500)
mainframe.grid(row=0, column=0, sticky="nwes")
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

#Menu
root.option_add('*tearOff', FALSE)
menubar = Menu(mainframe)
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')

menu_file.add_command(label='New', command=newFile)
menu_file.add_command(label='Open...', command=openFile)
menu_file.add_command(label='Close', command=closeFile)

#Text file tabs
notebook = ttk.Notebook(mainframe)
tab1 = Text(notebook)
notebook.add(tab1, text='Untitled1')
notebook.grid()

#root configuration
root.config(menu=menubar)
root.mainloop()