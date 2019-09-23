import os
import serial
from Tkinter import *
			#str(var.get()) gives the extension of the file
def sel():
   selection = "You selected the option" + str(var.get())
   label.config(text = selection)

root = Tk()
#w = Tk.Label(root, text="Select the file extension")
var = StringVar()
R1 = Radiobutton(root, text=".pdf",padx =120, variable=var, value=".pdf",
				  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text=".txt",padx =120, variable=var, value=".txt",
				  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text=".png",padx =120, variable=var, value=".png",
				  command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack() 
root.mainloop()
save_path = os.path.join(os.path.expanduser('~'),'Desktop/LiFi-master/Recieved_files') 
ser  = serial.Serial('/dev/ttyUSB1',4800,timeout=0)
			#extension of file is added to the basepath
base_path = os.path.basename("received"+str(var.get()))			
print("base path")
file = open(os.path.join(save_path,base_path),"wb")
print("file open")

while 1:
	if ser.inWaiting():
		readf = ser.read()
	print("written")
	file.write(readf)
	print("Receiving File...")	
	file.flush()
file.close()
ser.close()
