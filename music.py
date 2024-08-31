from tkinter import *
from pygame import mixer


mixer.init()

mixer.music.load('kbc.mp3')
mixer.music.play(-1)



root=Tk()
root.geometry('1270x652+0+0')
root.title('who wants to be millionaire')
root.config(bg='black')

centerImage=PhotoImage(file='Center.png')
leftframe=Frame(root,bg='black',padx=100)
leftframe.grid(row=0,column=0)

centerFrame=Frame(leftframe,bg='black',pady=100,padx=100)
centerFrame.grid(row=1,column=0)


logolable=Label(centerFrame,image=centerImage,bg='black',width=350,height=250)
logolable.grid(row=1,column=2)








root.mainloop()