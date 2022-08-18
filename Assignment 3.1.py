#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
h=pd.read_csv("df3.csv")
h


# In[2]:


h.info()


# In[3]:


h.head()


# In[4]:


h.plot.scatter(x='a',y='b',c='red',s=50,figsize=(10,5))


# In[5]:


h['a'].plot.hist()


# In[8]:


h['a'].plot.hist(alpha=0.3,bins=30)


# In[9]:


h[['a','b']].plot.box()


# In[10]:


h['d'].plot.kde()


# In[11]:


h['d'].plot.kde(lw=3,ls='--')


# In[12]:


h.loc[0:30].plot.area(alpha=0.4)


# In[13]:


h.loc[0:30].plot.area(alpha=0.4)
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))


# In[ ]:




