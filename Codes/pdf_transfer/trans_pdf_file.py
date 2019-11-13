import os
import serial
from tkinter import Tk
from tkinter.filedialog import askopenfilename

root = Tk()
ftypes = [('All files',"*.*")]
ttl  = "Title"
dir1 = 'C:\\'
root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
print (root.fileName)

# file save location - works best with gui path picker
save_path = os.path.join(os.path.expanduser('~'),root.fileName) 
ser  = serial.Serial('/dev/ttyUSB0',4800,timeout=0)
# read any file
base_path = os.path.basename(root.fileName)
filew = open(os.path.join(save_path,base_path),"rb")

image = filer.read()
#print(base_path)
ser.write(image)
print(image)
ser.close()
filer.close()
