#!/usr/bin/env python
# coding: utf-8

# # Databases searched for the Oxford Catalogue of Opioids  

# #### This notebook visualises the extracted data for one of my DPhil chapters, more details about this is available on my OSF project page [here](https://osf.io/2ph6c/). 

# In[1]:


# import libraries required for analysis 
import numpy as np
import pandas as pd
from pylab import savefig
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Whole Ox Cat of Opioids import 
df1 = pd.read_csv("oxcat.csv",thousands=',')
df1.head()


# ## Bar graph of the 7 databases used to identify the opioids

# In[2]:


# import data 
df2 = pd.read_csv("chp5.csv",thousands=',')
df2.head()


# In[3]:


df2.describe()


# In[4]:


df2.dtypes


# In[5]:


df2.columns


# In[6]:


# plot data as a bar graph using seaborn
plt.figure(figsize=(12,8))
ax = sns.barplot(data=df2, x="databases", y="opioids", color="navy")
plt.xlabel(' ')
plt.ylabel('No. of opioids in data source')

plt.savefig("databases.png", dpi=600)


# In[ ]:


df2.columns = ['databases', 'opioids', 'percent']


# In[ ]:




