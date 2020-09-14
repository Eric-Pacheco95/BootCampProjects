#!/usr/bin/env python
# coding: utf-8

# In[1]:


# some_file.py
#import sys
# insert at 1, 0 is the script path (or '' in REPL)
#sys.path.insert(1, 'oil_api')
import os
import pandas as pd


# In[2]:



opec_storage_water = pd.read_csv('completed_flow/Extract/opec/opec_storage_water.csv')  
 

 


# In[3]:


opec_storage_water = opec_storage_water.drop(opec_storage_water.columns[0], axis=1)


# In[4]:


total_oil_storage = opec_storage_water.iloc[[3,4,5,7,8,9,11],:]
Categories = ['OECD Onland Commercial','OECD Onland Commercial','OECD Onland Commercial','OECD SPR','OECD SPR','OECD SPR','Oil-on-water']
total_oil_storage['_'] = Categories
total_oil_storage.drop('-',axis=1,inplace=True)


# In[5]:


total_oil_storage.reset_index(drop=True,inplace=True)
total_oil_storage.rename(columns={'_':'Storage Type'},inplace=True)


# In[6]:


total_oil_storage['Country'][6] = 'Global'


# In[7]:


total_oil_storage.set_index('Storage Type',drop=True,inplace=True)


# In[8]:


total_oil_storage.to_csv('completed_flow/data/world_storage.csv')
total_oil_storage


# In[ ]:





# In[ ]:




