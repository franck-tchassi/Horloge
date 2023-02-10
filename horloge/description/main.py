from tkinter import*
from time import strftime
import time
import datetime


  
root = Tk()
root.title('Horloge')
  

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
    
  

lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
  

lbl.pack(anchor = 'center')
time()

quitter = Button(root,background='blue',  text='fermer', command=quit).pack()
  
mainloop()