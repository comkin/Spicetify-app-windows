import subprocess
import time
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from unittest import result
import os

ok = 'script 100% charged'

def script():
    
    subprocess.run(["powershell.exe","-Command","iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1 | iex"])
    time.sleep(3)
    os.system('cmd /c "spicetify upgrade spicetify backup apply"')
    time.sleep(3)
    os.system('cmd /c "spicetify backup apply"')
    time.sleep(3)
    showinfo(message=ok)

root = Tk()
root.title('Spicetify Patch v1.0')
root.geometry("300x150")
root.resizable(False, False)
root.iconbitmap('D:\Python_Personal_Project\icona.ico')

label = Label(text='premi il pulsante per patchare spotify',font=('Helvetica',12))
label.pack()


pb = ttk.Button( text="PATCH", command=script)
pb.pack(fill='x', expand=True, pady=10)


root.bind("Return",script)
root.mainloop()