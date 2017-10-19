from tkinter import *
#from PIL import Image,ImageTk
import threading
import Database as dbase
import time
import PIL.Image
import PIL.ImageTk
#from gtts import gTTS
import gtts
import pygame
import tkinter
import tkinter.dialog
from tkinter import messagebox



image1=None
image2=None
image3=None

secondtop=None
secondbottom=None

thirdcontroller=None

fourthimage=None
nextBtnImage=None

ingredientsList=[]
mainItem=''

ind=0

class Brain:
         def __init__(self):
                  #threading.Thread(target=self.GUIStuffs).start()
                  self.GUIStuffs()
                  
         def Speak(self,word):
                  SONG_END=pygame.USEREVENT+1
                  
                  pygame.mixer.music.set_endevent(SONG_END)  
                  global ind
                  pygame.mixer.music.set_endevent(SONG_END)
                  tts=gtts.gTTS(text=str(word),lang='en')
                  name='song'+str(ind)+'.mp3'
                  ind+=1
                  tts.save(name)
                  pygame.mixer.music.load(name)
                  pygame.mixer.music.play()
                  marker=0
                  while(1):
                           for e in pygame.event.get():
                                 if e.type==SONG_END:
                                     marker=1
                                     break
                           if marker==1:
                               break


         def FinalOp(self,recepies):
                  s1=1
                  for g in recepies:
                           step,gas,activity,staytime=g.split(',')

                           WaitTime=float(staytime)

                           t1=step
                           t2= 'And turn the gas to '+gas
                           t3='after that '+activity
                           t4=' ok then wait for '+staytime+' Seconds'
                           temptext=step+' And turn the gas to '+gas+'  after that '+activity+'  , ok then wait for '+staytime+' Seconds'
                           #self.Speak(temptext)

                           self.Speak(t1)
                           self.Speak(t2)
                           self.Speak(t3)
                           self.Speak(t4)

                           
                           self.T.insert(END,'step '+str(s1)+': '+temptext+'\n')
                           s1+=1
                           time.sleep(WaitTime)
                  messagebox.showinfo(title="Finished",message="Food successfully coooked")
                  self.root.destroy()
                           
                  
                    
         def SixthPage(self):
                  self.frame4.pack_forget()
                  self.frame5.pack()
                  recepies=dbase.RetrieveRecepie(mainItem)
                  self.T=Text(self.frame5,height=30)
                  self.T.pack()
                  threading.Thread(target=self.FinalOp,args=(recepies,)).start()
                  


         def FifthPage(self):
                  self.frame3.pack_forget()
                  self.frame4.pack()
                  T=Text(self.frame4,height=28)
                  T.pack()

         
                  
                  nextBtn=Button(self.frame4,text='Next',command=self.SixthPage)
                  nextBtn.pack()
                  
                  textcombo=''
                  for a in ingredientsList:
                           textcombo+=a+'\n'
                  T.insert(END,textcombo)
                  T.config(state=DISABLED)

                  nextBtn['state']='disabled'

                  ComputerIns="so you are preparing "+mainItem+" today here are the ingredients you should make ready before going to next step,once you are done click on the next button to start cooking today's dish"
                  self.Speak(ComputerIns)
                  nextBtn['state']='normal'
                  
                  
         def ClickOnItem(self,evt):
                  global ingredientsList,mainItem
                  w=evt.widget
                  index=int(w.curselection()[0])
                  value=w.get(index)
                  ingredients=dbase.RetrieveIngredients(value)
                  mainItem=value
                  ingredientsList=ingredients
                  threading.Thread(target=self.FifthPage).start()
                  #self.FifthPage()
                  
         def FourthPage(self):
                  global fourthimage
                  try:
                           self.frame2.pack_forget()
                           self.frame1.pack_forget()
                  except:
                           
                           self.frame1.pack_forget()
                           
                  self.frame3.pack()

                  MenuItems=dbase.RetrieveMenu()
                  
                  fourthimage=PIL.ImageTk.PhotoImage(file='Menu.png')

                  lbl=Label(self.frame3,text="MENU",image=fourthimage)

                  lbl.pack()
                  
                  lstbox=Listbox(self.frame3,width=640,height=280)
                  #lstbox.grid(row=1,column=0)
                  lstbox.pack()
                  
                  for i in MenuItems:
                           lstbox.insert(END,i)
                  lstbox.bind('<<ListboxSelect>>',self.ClickOnItem)

                  ComputerText='Okay now you are ready to see our menu, select any item that you wanna cook today '
                  self.Speak(ComputerText)
         
         def ThirdPage(self):
                  global thirdcontroller
                  Tips_text="Okay so you are new user then look carefully to the picture describing you the stove flames level which will be useful in later cooking instructions, After you are done you can click on the picture"
                  

                  self.frame1.pack_forget()
                  self.frame2.pack()

                  thirdcontroller=PIL.ImageTk.PhotoImage(file='controller.png')
                  thirdbutton=Button(self.frame2,borderwidth=0,image=thirdcontroller,highlightthickness=0,command=self.FourthPage)
                  thirdbutton.pack()
                  thirdbutton['state']='disabled'
                  self.Speak(Tips_text)
                  thirdbutton['state']='normal'
                  
         
         def SecondPage(self):
                  global image2,secondtop,secondbottom
                  
                  self.frame0.pack_forget()
                  self.frame1.pack()
                  
                  ##Second Page
                  Greetings_Text='Hello, Welcome to cooking guide, you can click on the screen for next step based on given instructions , new if you are new user and old if you are an old user' 
                  

                  
                  
                  secondtop=PIL.ImageTk.PhotoImage(file='secondtop.png')
                  secondbottom=PIL.ImageTk.PhotoImage(file='secondbottom.png')

                  topbtn=Button(self.frame1,borderwidth=0,image=secondtop,highlightthickness=0,command=self.ThirdPage)
                  topbtn.pack()

                  downbtn=Button(self.frame1,borderwidth=0,image=secondbottom,highlightthickness=0,command=self.FourthPage)
                  downbtn.pack()
                  topbtn['state']='disabled'
                  downbtn['state']='disabled'
                  
                  self.Speak(Greetings_Text)
                  topbtn['state']='normal'
                  downbtn['state']='normal'

                  ##
                  
         def FrontPage(self):
                  global image1
                  #self.frame9.grid_forget()
                  self.frame0.pack()
                  image1=PhotoImage(file='first.png')
                  BtnStart=Button(self.frame0,borderwidth=0,image=image1,highlightthickness=0,command=self.SecondPage)
                  BtnStart.pack()
                  
                  ##
         def TempButton(self):
                  self.frame9=Frame(self.root)
                  self.frame9.pack()
                  tempbtn=Button(self.frame9,text='start',command=self.FrontPage)
                  tempbtn.pack()
                  

         def GUIStuffs(self):
                  self.root=Tk()
                  self.root.title('Foody')

                  screen_width=self.root.winfo_screenwidth()
                  screen_height=self.root.winfo_screenheight()

                  x=(screen_width/2)-(640/2)
                  y=(screen_height/2)-(480/2)
                  
                  
                  self.root.geometry('%dx%d+%d+%d'%(640,480,x,y))

                  self.root.resizable(0,0)
                  self.root.configure(background='#008080')
                  self.frame0=Frame(self.root)
                  self.frame1=Frame(self.root)
                  self.frame2=Frame(self.root)
                  self.frame3=Frame(self.root)
                  self.frame4=Frame(self.root)
                  self.frame5=Frame(self.root)
                  self.FrontPage()
                  self.root.mainloop()

pygame.init()
pygame.mixer.init()
b=Brain()

