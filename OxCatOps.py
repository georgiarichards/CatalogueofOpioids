#!/usr/bin/env python
# coding: utf-8

# # The Oxford Catalogue of Opioids  

# #### This notebook visualises the extracted data for the searches and pharmacology data of 228 opioid drugs, more details about this research is available on our OSF project page [here](https://osf.io/2ph6c/). 

# In[1]:


# import libraries required for analysis 
import numpy as np
import pandas as pd
from pylab import savefig
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Phase 1: The list of opioid drugs and their nomenclature 

# In[2]:


# importing data for phase 1 - the list of 228 opioid drugs 
df1 = pd.read_csv("phase1_oxcatop.csv",thousands=',')


# In[3]:


df1.head()


# In[4]:


df1.sum()


# In[5]:


# percentage of drugs in each drug source
(df1['INN'].value_counts()/df1['INN'].count())*100


# In[6]:


(df1['INCB'].value_counts()/df1['INCB'].count())*100


# In[7]:


(df1['Merck_index'].value_counts()/df1['Merck_index'].count())*100


# In[8]:


(df1['Martindale'].value_counts()/df1['Martindale'].count())*100


# In[9]:


(df1['guide_to_pharmacol'].value_counts()/df1['guide_to_pharmacol'].count())*100


# In[10]:


(df1['ATC'].value_counts()/df1['ATC'].count())*100


# In[11]:


(df1['BNF'].value_counts()/df1['BNF'].count())*100


# In[12]:


# creating a new variable to sum the 7 data sources 
df1['sources'] = df1['ATC'] + df1['BNF'] + df1['guide_to_pharmacol'] + df1['INCB'] + df1['Merck_index'] + df1['Martindale'] + df1['INN']


# In[13]:


df1.describe()


# In[14]:


# visualising the spread of data to check the median is the best measure
ax = sns.countplot(data=df1, x="sources", color="navy")


# In[15]:


# importing new dataframe for figure of seven data sources 
df2 = pd.read_csv("oxcat_databases.csv",thousands=',')
df2.head()


# In[16]:


df2.describe()


# In[17]:


# ploting data as a bar graph using seaborn
plt.figure(figsize=(12,8))
ax = sns.barplot(data=df2, x="databases", y="opioids", color="navy")
plt.xlabel(' ')
plt.ylabel('No. of opioids in data source')

plt.savefig("databases.png", dpi=600)


# In[18]:


# determining the number of unique suffixes 
df1['suffix'].nunique()


# In[19]:


# the breakdown of the number of drugs in each suffix subgroup 
df1['suffix'].value_counts()


# In[20]:


# the percentage of drugs in each suffix subgroup 
(df1['suffix'].value_counts()/df1['suffix'].count())*100


# In[21]:


# plotting the number of suffixes using seaborn
plt.figure(figsize=(18,13))
ax = sns.countplot(data=df1, 
                   x="suffix", 
                   color="navy",
                   order=df1['suffix'].value_counts().index)
plt.xlabel(' ')
plt.ylabel('Number of drugs', fontsize=16)

plt.savefig("fig_suffix.png", dpi=600)


# ### Phase 2: Cataloging of opioids by pharmacology properties   

# In[22]:


# importing data for phase 2 - pharmacology data 
df3 = pd.read_csv("phase2_oxcatop.csv",thousands=',')


# In[23]:


df3.head()


# In[24]:


# calculating the median for molecular weight 
df3.describe()


# In[25]:


# percentage of missing data - MOP receptor
(137/228)*100


# In[26]:


# percentage of missing data - DOP receptor
(80/228)*100


# In[27]:


# percentage of missing data - KOP receptor
(82/228)*100


# In[28]:


# percentage of missing data - NOP receptor
(10/228)*100


# In[29]:


# determining the total for each receptor 
df3.sum()


# In[30]:


# the breakdown of the number of drugs in each suffix subgroup 
df3['effect_MOP'].value_counts()


# In[31]:


df3['effect_DOP'].value_counts()


# In[32]:


df3['effect_KOP'].value_counts()


# In[33]:


df3['effect_NOP'].value_counts()


# In[34]:


# total agonists 
104 + 41 + 46 + 3


# In[35]:


# percentage of agonists 
((104 + 41 + 46 + 3)/228) * 100


# In[36]:


# total partial agonists 
8+3+8+1


# In[37]:


# percentage of partial agonists 
((8+3+8+1)/228)*100


# In[38]:


# total antagonists
14+11+12


# In[39]:


# percentage of antagonits 
((14+11+12)/228)*100


# In[40]:


# percentage of mixed receptors 
(6/228)*100


# In[41]:


# opioid classes based on their origin of discovery or development
df3['class'].value_counts()


# In[42]:


(df3['class'].value_counts()/df3['class'].count())*100


# In[ ]:




