#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from math import log
n=100
y=np.random.randint(low=0,high=2, size=100)
uy=np.random.rand(0,n)
o=-np.sum(y*np.log2(uy) + (1-y)*np.log2(1-uy))/n
print(o)


# In[24]:


def answer(A,t):
    ans={}
    b=1
    for i in range(0,len(A)):
        for j in range(0,len(A)):
            if A[i]+A[j]==t:
                ans[b]=[i,j]
                b+=1
    return ans            
#for example    
a=answer([10,20,10,40,50,60,70],50)
print(a)

