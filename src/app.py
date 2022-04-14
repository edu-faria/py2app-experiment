import os
from tkinter import filedialog
from tkinter import *

def get_size(start_path):
    global folder_size
    global structure_data

    # Level 1
    dirpath, dirnames, filenames = next(os.walk(start_path))
    structure_data.append({"path": dirpath, "size": sizing(dirpath)})

    #for i in range(2): # Going two level deeper
    for item in structure_data:
        #print(item)
        dirpath, dirnames, filenames = next(os.walk(item["path"]))
        for subdir in dirnames:
            structure_data.append({"path": os.path.join(dirpath, subdir), "size": sizing(os.path.join(dirpath, subdir))})

# [{'path': '/Users/edefari/Documents/temp', 'size': 57497}, 
#     {'path': '/Users/edefari/Documents/temp/BBB', 'size': 6161}, 
#     {'path': '/Users/edefari/Documents/temp/CCC', 'size': 6161}, 
#     {'path': '/Users/edefari/Documents/temp/AAA', 'size': 36966}, 
#         {'path': '/Users/edefari/Documents/temp/AAA/AA2', 'size': 6161}, 
#         {'path': '/Users/edefari/Documents/temp/AAA/AA1', 'size': 24644}, 
#             {'path': '/Users/edefari/Documents/temp/AAA/AA1/A11', 'size': 6161}, 
#             {'path': '/Users/edefari/Documents/temp/AAA/AA1/A12', 'size': 12322}, 
#                 {'path': '/Users/edefari/Documents/temp/AAA/AA1/A12/211', 'size': 6161}]


    # Check dir size
    # Include dir, path and size as dictionary on list
    # Reduce level
    # If not last dir:
        # Check size of each subdir and handle files as folders (Files)
        # Until 75% show folders, the rest as other
        # Include dir, path and size as directory on list

    print (structure_data)


def sizing(path_to_check):
    global folder_size
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path_to_check):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    folder_size.set(total_size/1024/1024)
    return(total_size)

def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    get_size(filename) #Calculates the size and refresh the UI

root = Tk()
folder_path = StringVar() #Needed to browse directory
folder_size = StringVar()
structure_data = []
root.title("Version sizing report")

Label(root, text="Select the path to be checked").pack()
Label(root, textvariable=folder_path).pack()
Button(root, text="Choose folder", command=browse_button).pack()
Label(root, text="Size in MB:").pack()
Label(root, textvariable=folder_size).pack()

root.mainloop()

