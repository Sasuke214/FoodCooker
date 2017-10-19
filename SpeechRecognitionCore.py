import speech_recognition as sr
from gtts import gTTS
import pygame
from tkinter import *

r = sr.Recognizer()

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


