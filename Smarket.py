
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv("D:/Data-Analysis/Smarket.csv")
data


# In[4]:


data_01 = data[data['Year']==2001]
data_01_dn = dict(data_01[data_01['Direction']=='Down'])
del data_01_dn['Direction'],data_01_dn['Year']
print(data_01_dn)


# In[5]:


for i in range(0,len(list(data_01_dn['Lag1']))-6):
    lag_li.append([data_01_dn['Lag5'][i]])
    
lag_li.append()


# In[7]:


plt.plot(data_01_dn['Lag5'], "-b")

