#!/usr/bin/env python
# coding: utf-8

# In[10]:


def prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count = count+1
    if count == 2:
        print("prime")
    else:
        print("not a prime")
prime(25)


# In[ ]:




