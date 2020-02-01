#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qrtools
qr = qrtools.QR()
qr.decode("code.png")
print(qr.data)

