#for python 3.4 and above
from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk()
ftypes = [('All files',"*.*")]
ttl  = "Title"
dir1 = 'C:\\'
root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
print("File: ",root.fileName)

