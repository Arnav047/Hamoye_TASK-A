#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[155]:


x=pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv',encoding='ISO-8859-1')
x.head(1313)


# In[156]:


x.groupby('Element')['Y2014'].sum()


# In[157]:


x.groupby('Item')['Y2014'].sum()


# In[150]:


x['Y2018'].head(1313).sum()


# In[173]:


print(x.groupby('Item')['Y2014'].sum())
print(x.groupby('Item')['Y2017'].sum())


# In[162]:


print(x['Y2015'].mean())
print(x['Y2015'].std())


# In[163]:


print((x['Y2016'].isnull().sum()*100)/len(x))
print(x['Y2016'].isnull().sum())


# In[174]:


print(x['Y2014'].corr(x['Element Code']))
print(x['Y2015'].corr(x['Element Code']))
print(x['Y2016'].corr(x['Element Code']))
print(x['Y2017'].corr(x['Element Code']))
print(x['Y2018'].corr(x['Element Code']))


# In[171]:


print(x.groupby('Element')['Y2015'].sum())
print(x.groupby('Element')['Y2016'].sum())
print(x.groupby('Element')['Y2017'].sum())
print(x.groupby('Element')['Y2018'].sum())


# In[169]:


x.groupby('Element')['Y2014'].sum()


# In[172]:


x.groupby('Element')['Y2018'].sum()


# In[177]:


x.groupby('Area')['Y2018'].sum()


# In[176]:


x['Area'].unique()


# In[ ]:





# In[ ]:




