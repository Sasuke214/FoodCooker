import time

fp=open('Data.txt')

all_data=fp.read().split('DONE')

itemNames=[]

counter=0
for x in all_data:
         if len(x)>0 :
                  y=x.split('\n')
                  y=y[:len(y)-1]
                  if counter>0:
                           y=y[1:len(y)-1]
                     
                  itemNames.append(y[0])
                  all_data[counter]=y
                  counter+=1
         

file2=open('items.txt','w')
for d in itemNames:
         d=d[4:]
         file2.write(d+'\n')

file2.close()
fp.close()

ingredients=open('Ingredients.txt').read().split('DONE')



def RetrieveMenu():
         temp=[]
         file=open('items.txt','r').read().split('\n')
         for s in file:
                  if len(s)>0:
                           temp.append(s)
         return temp

def RetrieveIngredients(item_name):
         for i in range(0,len(ingredients)-1):
                  itemlst=ingredients[i].split('\n')
                  if i==0:
                           itemlst=itemlst[:len(itemlst)-1]
                  else:
                           itemlst=itemlst[1:len(itemlst)-1]
                  itemname=itemlst[0]

                  if item_name==itemname:
                           return itemlst[1:]
         return []
                  
def RetrieveRecepie(item_name):
        for a in all_data:
                 if len(a)>0:

                          if a[0][4:]==item_name:
                                   return a[1:]
        return []



