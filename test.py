import SpeechRecognitionCore as src
import TextToSpeechCore as ttc
import random
from tkinter import *
import os
from PIL import ImageTk, Image

import threading

songsval=0

mem=''

def Tutorial():
         #show images regarding gas
         path=os.path.join(os.getcwd(),'as.png')
         img=ImageTk.PhotoImage(Image.open(path))
         panel=Label(root,image=img)
         panel.pack()
         
         
def Start():
         global mem
         mem=input('are you a new member or an old?')
         while mem!='old' and mem!='new':
                  print('please enter correct value')
                  mem=input('are you a new member or an old?')         
         if mem=='new':
                  Tutorial()
         else:
                  print('no tutorial')
                  
         item=input('what you wanna cook today?')
         ans=input()
         keywords=['what','available','today']

         ans=list(ans)
         if keywords in ans:
                  print('ok')

         
         #search item in database
         

def OkPressed():
         threading.Thread(target=Start).start()

root=Tk()
root.title('Foody')
root.geometry('1024x768')
root.configure(background='grey')

btn=Button(text='ok',command=OkPressed)
btn.pack()
root.mainloop()
