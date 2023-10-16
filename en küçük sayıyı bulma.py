        # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#en küçük sayıyı arıyorum.
liste = [50,90,40,45,1,70,1000,0]
x= 0
y= x +1
bos='\n*******'
for i in liste:

    
        print(liste[x])
        if liste[x]<liste[y]:
            print(bos)
            print(x,y)
            print(liste[x],liste[y])
           
            y+=1
            if x == y:
                print(y)
                y+=1
            else:
                print(x,y)
                print(liste)
        
        else: 
            if x == y:
                print(y)
                y+=1
            else:
                print(bos)
                print(x,y)
                print(liste[x],liste[y])
            x+=1
            print(x,y)
            print(liste)
