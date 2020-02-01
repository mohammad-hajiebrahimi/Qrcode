#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyqrcode
file = "www.geeksforgeeks.org"
main = pyqrcode.create( file )
main.svg("geeks.svg" ,scale=8)
main.eps("geeks.eps" ,scale=8)
print(main.terminal(quiet_zone = 1))


# In[2]:


#create pyqrcode full
main1 = pyqrcode.create( file , error="L" ,version=30 ,mode="binary")


# In[3]:


import tkinter
code = pyqrcode.create('Knights who say ni!')
code_xbm = code.xbm(scale=5)
top = tkinter.Tk()
code_bmp = tkinter.BitmapImage(data=code_xbm)
code_bmp.config(foreground="black")
code_bmp.config(background="white")
label = tkinter.Label(image=code_bmp)
label.pack()


# In[4]:


import png
big_code = pyqrcode.create('0987654321') 
big_code.png('code.png', scale=8)
big_code.show()


# In[ ]:




