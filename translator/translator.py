from tkinter import *
from tkinter import ttk
from translate import Translator

# Translator function
def translate():
    translator = Translator(from_lang=lan1.get(), to_lang=lan2.get())
    translation = translator.translate(var.get())
    var1.set(translation)

# Tkinter root Window with title
root = Tk()
root.title("Translator")

# Creating a Frame and Grid to hold the Content
mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Variables for dropdown list
lan1 = StringVar(root)
lan2 = StringVar(root)

# Choices to show in dropdown menu
choices = {'English', 'French', 'Chinese', 'Spanish', 'German'}
# Default selection for dropdown lists
lan1.set('English')
lan2.set('Spanish')

# Creating dropdown and arranging in the grid
lan1menu = ttk.Combobox(mainframe, textvariable=lan1, values=list(choices))
Label(mainframe, text="Select source language").grid(row=0, column=0, padx=10, pady=10)
lan1menu.grid(row=1, column=0, padx=10, pady=10)

lan2menu = ttk.Combobox(mainframe, textvariable=lan2, values=list(choices))
Label(mainframe, text="Select target language").grid(row=0, column=1, padx=10, pady=10)
lan2menu.grid(row=1, column=1, padx=10, pady=10)

# Text Box to take user input
Label(mainframe, text="Enter text").grid(row=2, column=0, padx=10, pady=10)
var = StringVar()
textbox = Entry(mainframe, textvariable=var).grid(row=3, column=0, padx=10, pady=10)

# Textbox to show output
# Label can also be used
Label(mainframe, text="Output").grid(row=2, column=1, padx=10, pady=10)
var1 = StringVar()
textbox = Entry(mainframe, textvariable=var1, state='readonly').grid(row=3, column=1, padx=10, pady=10)

# Creating a button to call Translator function
b = Button(mainframe, text='Translate', command=translate).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
