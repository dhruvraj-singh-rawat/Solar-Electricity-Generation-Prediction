from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

win =Tk()
win.title('Solar I-O')
win.geometry('1024x640')


def donothing():
    print("i am doing nothing")

def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")


menu=Menu(win)
win.config(menu=menu)

#Title Bar Declaration
submenu=Menu(menu)
menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New Project",command=donothing)
submenu.add_command(label="Save",command=donothing)
submenu.add_separator()
submenu.add_command(label="Exit",command=donothing)

editmenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Redo",command=donothing)

## Main Body
ProjectHeading =Label(win,text="Solar-Panel IO Predictor",fg="black")
ProjectHeading.config(font=("Calibri", 24))
ProjectHeading.pack(fill=X)

#Button Declaration
button_1=Button(win,text="Choose File",command = OpenFile)
button_1.pack()



win.mainloop()