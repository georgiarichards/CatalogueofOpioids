#!/usr/bin/env python
# coding: utf-8

# # The Oxford Catalogue of Opioids  

# #### This notebook visualises the extracted data for the searches and pharmacology data of opioid drugs, more details about this research is available on our OSF project page [here](https://osf.io/2ph6c/). 

# In[2]:


# import libraries required for analysis 
import numpy as np
import pandas as pd
from pylab import savefig
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Phase 1: The list of opioid drugs and their nomenclature 

# In[3]:


# importing data for phase 1 - the list of opioid drugs 
df1 = pd.read_csv("phase1_oxcatop.csv",thousands=',')


# In[4]:


df1.head()


# In[5]:


df1.sum()


# In[6]:


# total number of opioids from searches
57+31+65+120+110+68+170


# In[21]:


# removing duplicates 
621-432


# In[22]:


# new drugs found from the literature & wikipedia 
189+42+2


# In[9]:


# percentage of drugs in each drug source
(df1['INN'].value_counts()/df1['INN'].count())*100


# In[10]:


(df1['INCB'].value_counts()/df1['INCB'].count())*100


# In[11]:


(df1['Merck_index'].value_counts()/df1['Merck_index'].count())*100


# In[13]:


(df1['Martindale'].value_counts()/df1['Martindale'].count())*100


# In[14]:


(df1['guide_to_pharmacol'].value_counts()/df1['guide_to_pharmacol'].count())*100


# In[15]:


(df1['ATC'].value_counts()/df1['ATC'].count())*100


# In[16]:


(df1['BNF'].value_counts()/df1['BNF'].count())*100


# In[17]:


# creating a new variable to sum the 7 data sources 
df1['sources'] = df1['ATC'] + df1['BNF'] + df1['guide_to_pharmacol'] + df1['INCB'] + df1['Merck_index'] + df1['Martindale'] + df1['INN']


# In[18]:


df1.describe()


# In[23]:


# visualising the spread of data to check the median is the best measure
ax = sns.countplot(data=df1, x="sources", color="navy")


# In[24]:


# importing new dataframe for figure of seven data sources 
df2 = pd.read_csv("oxcat_databases.csv",thousands=',')
df2.head()


# In[25]:


df2.describe()


# In[28]:


# ploting data as a bar graph using seaborn
plt.figure(figsize=(12,8))
ax = sns.barplot(data=df2, x="databases", y="opioids", color="navy")
plt.xlabel(' ')
plt.ylabel('No. of opioids in sources searched', fontsize=16)

plt.savefig("databases.png", dpi=600)


# In[29]:


# determining the number of unique stems
df1['who_stem'].nunique()


# In[30]:


# the breakdown of the number of drugs in each stems subgroup 
df1['who_stem'].value_counts()


# In[31]:


# the percentage of drugs in each stem subgroup 
(df1['who_stem'].value_counts()/df1['who_stem'].count())*100


# In[32]:


# number of drugs with no stem 
len(df1) - df1['who_stem'].count()


# In[33]:


(50/233)*100


# In[35]:


# plotting the number of stems using seaborn
plt.figure(figsize=(15,10))
ax = sns.countplot(data=df1, 
                   x="who_stem", 
                   color="navy",
                   order=df1['who_stem'].value_counts().index)
plt.xlabel(' ')
plt.ylabel('Number of drugs', fontsize=16)

plt.savefig("fig_stem.png", dpi=600)


# ### Phase 2: Cataloging of opioids by pharmacology properties   

# In[36]:


# importing data for phase 2 - pharmacology data 
df3 = pd.read_csv("phase2_oxcatop.csv",thousands=',')


# In[37]:


df3.head()


# In[38]:


# calculating the median for molecular weight 
df3.describe()


# In[42]:


#missing data for receptors 
(10/233)*100


# In[39]:


# determining the total for each receptor 
df3.sum()


# In[43]:


# the breakdown of the number of drugs in each suffix subgroup 
df3['effect_MOP'].value_counts()


# In[44]:


df3['effect_DOP'].value_counts()


# In[45]:


df3['effect_KOP'].value_counts()


# In[46]:


df3['effect_NOP'].value_counts()


# In[47]:


# total agonists 
103 + 40 + 45 + 3


# In[48]:


# percentage of agonists 
((191)/233) * 100


# In[49]:


# total partial agonists 
8+3+8+1


# In[50]:


# percentage of partial agonists 
(20/233)*100


# In[51]:


# total antagonists
18+16+15


# In[52]:


# percentage of antagonits 
(49/233)*100


# In[53]:


# percentage of mixed receptors 
(6/233)*100


# In[54]:


# opioid classes based on their origin of discovery or development
df3['class'].value_counts()


# In[55]:


(df3['class'].value_counts()/df3['class'].count())*100


# In[ ]:




