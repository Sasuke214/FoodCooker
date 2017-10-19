from gtts import gTTS
import pygame
from tkinter import *

pygame.init()
pygame.mixer.init()
SONG_END=pygame.USEREVENT+1
def Speak(word='hello',songval=0):
    
    pygame.mixer.music.set_endevent(SONG_END)
    while True:
        try:
            tts=gTTS(text=str(word),lang='en')        
            name='song'+str(songval)+'.mp3'
            tts.save(name)
            break
        except:
            print('try again')
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    while True:
        for e in pygame.event.get():
                if e.type==SONG_END:
                    return   

def CallSpeak():
         Speak('hey how u doing')

##pygame.init()
##pygame.mixer.init()
##root=Tk()
##Btn=Button(text='Ok',command=CallSpeak)
##Btn.pack()
##root.mainloop()
