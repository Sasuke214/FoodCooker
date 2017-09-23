import speech_recognition as sr
from gtts import gTTS
import pygame
from tkinter import *

# obtain audio from the microphone
r = sr.Recognizer()
ind=0
SONG_END=pygame.USEREVENT+1
def Speak(word):
    global ind
    pygame.mixer.music.set_endevent(SONG_END)
    tts=gTTS(text=str(word),lang='en')
    name='song'+str(ind)+'.mp3'
    ind+=1
    tts.save(name)
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    for e in pygame.event.get():
            if e.type==SONG_END:
                print('ok')
                break
    
def Listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        word=r.recognize_google(audio)
        return str(word)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def PatternSearch(str1,str2):
       str1=str1.lower()
       str2=str2.lower()
       length2=len(str2)
       length1=len(str1)
       for i in range(0,len(str1)):
            j=0
            temp=i
            while j<length2 and i<length1 and str1[i]==str2[j]:
                 i+=1
                 j+=1
            if j==length2:
                 return 1
            else:
                 i=temp
            i+=1
       return 0
    
def TestCases():
    while(1):
        wrd=Listen()
        print(wrd)
        wrd=str(wrd)
        print(PatternSearch(wrd,'let'))
        print(PatternSearch(wrd,'Start'))
        if PatternSearch(wrd,'let') and PatternSearch(wrd,'Start'):
            Speak("Okay Let's Get Started, But Before That,What's Your name?")
            name=Listen()
            Speak("Okay"+str(name)+",So,What You Wanna Cook Today?")
            name=Listen()
            
            break
        else:
            print('continue')
        
root=Tk()
pygame.init()
pygame.mixer.init()  
btn=Button(root,text='ok',command=TestCases)
btn.pack()
#TestCases()
root.mainloop()
