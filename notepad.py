from tkinter import *
from tkinter import ttk,filedialog

def newFile():
	tab = Text(notebook)
	notebook.add(tab, text='Untitled'+str(notebook.index('end')))
	notebook.select(notebook.index('end')-1)

def openFile():
	filename = filedialog.askopenfilename(initialdir='home/', title="Select file..")
	tab = Text(notebook)
	notebook.add(tab, text=filename)
	with open(filename) as f:
		text = f.read()
		tab.insert(INSERT, text)
		notebook.select(notebook.index('end')-1)

def closeFile():
	if notebook.index(notebook.select()) != 0:
		notebook.forget(notebook.index(notebook.select()))
	else:
		tab = Text(notebook)
		notebook.add(tab, text='Untitled')
		notebook.forget(0)

#root
root = Tk()
root.title('Notepad')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#main
mainframe = ttk.Frame(root, height=500, width=500)
mainframe.grid(row=0, column=0, sticky="nwes")
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)

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

root.config(menu=menubar)

#Text file tabs
notebook = ttk.Notebook(mainframe)
tab = Text(notebook)
notebook.add(tab, text='Untitled')
notebook.grid(sticky="nwes")


#root configuration
root.mainloop()