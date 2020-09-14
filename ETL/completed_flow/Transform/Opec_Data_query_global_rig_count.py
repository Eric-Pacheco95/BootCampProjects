#!/usr/bin/env python
# coding: utf-8

# In[1]:


# some_file.py
#import sys
# insert at 1, 0 is the script path (or '' in REPL)
#sys.path.insert(1, 'oil_api')
import os
import pandas as pd


# In[ ]:





# In[3]:


glb_rig_count = pd.read_csv('completed_flow/Extract/opec/glb_rig_count.csv')  

 

 


# In[4]:


glb_rig_count = glb_rig_count.drop(glb_rig_count.columns[0], axis=1)
glb_rig_count = glb_rig_count.dropna(how='all')
glb_rig_count = glb_rig_count.drop([0])
glb_rig_count = glb_rig_count.iloc[0:30]
glb_rig_count = glb_rig_count.drop([9,14,15,29])
glb_rig_count.at[31,'Country']= 'Global'


# In[5]:



glb_rig_count = glb_rig_count.round()
glb_rig_count.set_index('Country',drop=True,inplace=True)
glb_rig_count


# In[7]:


glb_rig_count.to_csv('completed_flow/data/glb_rig_count.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




