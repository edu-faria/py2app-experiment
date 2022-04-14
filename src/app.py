import os
from tkinter import filedialog
from tkinter import *

def get_size(start_path):
    global folder_size
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        print("Dirpath: " + str(dirpath))
        print("Dirname: " + str(dirnames))
        print("Filename: " + str(filenames))
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    folder_size.set(total_size/1024/1024)

def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    get_size(filename) #Calculates the size and refresh the UI

root = Tk()
folder_path = StringVar() #Needed to browse directory
folder_size = StringVar()
root.title("Size checker")

Label(root, text="Select the path to be checked").pack()
Label(root, textvariable=folder_path).pack()
Button(root, text="Choose folder", command=browse_button).pack()
Label(root, text="Size in MB:").pack()
Label(root, textvariable=folder_size).pack()

root.mainloop()

