import tkinter as tk
from tkinter import filedialog
from PIL import Image

root=tk.Tk()

canvas1=tk.Canvas(root,width=300,height=250,bg='azure3',relief='raised')
canvas1.pack()

label1=tk.Label(root, text='File Conversion Tool', bg='azure3')
label1.config(font=('helvetica',20))
canvas1.create_window(150,60,window=label1)

def getPNG():
    global im1
    import_file_path=filedialog.askopenfilename()
    im1=Image.open(import_file_path)
    import_file_path = filedialog.askopenfilename()
    im1=Image.open(import_file_path)

browseButton_PNG =tk.Button(text= "    Import PNG or JPG File    ", command=getPNG, bg='royalblue', fg='white',font=('helvetica',12,'bold'))
canvas1.create_window(150,110, window=browseButton_PNG)

def convertToJPG():
    global im1
    export_file_path=filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)

saveAsButton_JPG= tk.Button(text='Convert PNG to JPG', command=convertToJPG, bg='royalblue', fg='white',font=('helvetica',12,'bold'))
canvas1.create_window(150,160,window=saveAsButton_JPG)

def convertToPNG():
    global im1
    export_file_path1=filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path1)

saveAsButton_PNG=tk.Button(text='Convert JPG to PNG', command=convertToPNG, bg='royalblue', fg='white',font=('helvetica',12,'bold'))
canvas1.create_window(150,210,window=saveAsButton_PNG)
    
root.mainloop()
