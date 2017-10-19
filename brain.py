from tkinter import *
from PIL import Image,ImageTk
import threading
import Database as dbase
import time

image1=None
image2=None
image3=None

secondtop=None
secondbottom=None

thirdcontroller=None

fourthimage=None

ingredientsList=[]
mainItem=''

class Brain:
         def __init__(self):
                  threading.Thread(target=self.GUIStuffs).start()                  

         def SixthPage(self):
                  recepies=dbase.RetrieveRecepie(mainItem)
                  for g in recepies:
                           step,gas,activity,staytime=g.split(',')
                           print(step)
                           print('And turn the gas to'+gas)
                           print('umm '+activity)
                           WaitTime=float(staytime)
                           print('ok then wait for'+staytime+' Seconds')
                           time.sleep(WaitTime)
                  
                  

         def FifthPage(self):
                  self.frame3.grid_forget()
                  self.frame4.grid()
                  T=Text(self.frame4,height=25)
                  T.grid()
                  textcombo=''
                  for a in ingredientsList:
                           textcombo+=a+'\n'
                  T.insert(END,textcombo)
                  T.config(state=DISABLED)

                  nextBtn=Button(self.frame4,text='NExt',command=self.SixthPage)
                  nextBtn.grid()
                  
                  
         def ClickOnItem(self,evt):
                  global ingredientsList,mainItem
                  w=evt.widget
                  index=int(w.curselection()[0])
                  value=w.get(index)
                  ingredients=dbase.RetrieveIngredients(value)
                  mainItem=value
                  ingredientsList=ingredients
                  self.FifthPage()
                  
         def FourthPage(self):
                  global fourthimage
                  try:
                           self.frame2.grid_forget()
                           self.frame1.grid_forget()
                  except:
                           
                           self.frame1.grid_forget()
                           
                  self.frame3.grid(row=0)
                  MenuItems=dbase.RetrieveMenu()
                  
                  fourthimage=ImageTk.PhotoImage(file='Menu.png')
                  lbl=Label(self.frame3,image=fourthimage)
                  lbl.grid()
                  
                  lstbox=Listbox(self.frame3,width=640,height=280)
                  lstbox.grid(row=3,column=0)

                  for i in MenuItems:
                           lstbox.insert(END,i)
                  lstbox.bind('<<ListboxSelect>>',self.ClickOnItem)

                  
         
         def ThirdPage(self):
                  global thirdcontroller
                  self.frame1.grid_forget()
                  self.frame2.grid(row=0,column=0)

                  thirdcontroller=ImageTk.PhotoImage(file='controller.png')
                  thirdbutton=Button(self.frame2,borderwidth=0,image=thirdcontroller,highlightthickness=0,command=self.FourthPage)
                  thirdbutton.grid()
                  
         
         def SecondPage(self):
                  global image2,secondtop,secondbottom
                  
                  self.frame0.grid_forget()
                  self.frame1.grid(row=0,column=0)
                  
                  ##Second Page


                  secondtop=ImageTk.PhotoImage(file='secondtop.png')
                  secondbottom=ImageTk.PhotoImage(file='secondbottom.png')

                  topbtn=Button(self.frame1,borderwidth=0,image=secondtop,highlightthickness=0,command=self.ThirdPage)
                  topbtn.grid()

                  downbtn=Button(self.frame1,borderwidth=0,image=secondbottom,highlightthickness=0,command=self.FourthPage)
                  downbtn.grid()


                  ##
                  
         def FrontPage(self):
                  global image1
                  self.frame0.grid()
                  image1=PhotoImage(file='first.png')
                  BtnStart=Button(self.frame0,borderwidth=0,image=image1,highlightthickness=0,command=self.SecondPage)
                  BtnStart.grid()
                  ##

         def GUIStuffs(self):
                  self.root=Tk()
                  self.root.title('Foody')
                  self.root.geometry('640x480')
                  self.root.configure(background='#008080')
                  self.frame0=Frame(self.root)
                  self.frame1=Frame(self.root)
                  self.frame2=Frame(self.root)
                  self.frame3=Frame(self.root)
                  self.frame4=Frame(self.root)
                  self.frame5=Frame(self.root)
                  self.FrontPage()
                  self.root.mainloop()

b=Brain()
