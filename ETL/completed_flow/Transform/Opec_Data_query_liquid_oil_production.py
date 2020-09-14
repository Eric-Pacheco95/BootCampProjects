#!/usr/bin/env python
# coding: utf-8

# In[2]:


# some_file.py
#import sys
# insert at 1, 0 is the script path (or '' in REPL)
#sys.path.insert(1, 'oil_api')
import os
import pandas as pd


# In[3]:



oil_liquid_production = pd.read_csv('completed_flow/Extract/opec/oil_liquid_production.csv')  




# In[4]:


oil_liquid_production = oil_liquid_production.drop(oil_liquid_production.columns[0], axis=1)
oil_liquid_production = oil_liquid_production.dropna()
oil_liquid_production = oil_liquid_production.drop([4,9,12,13,21,27,33,41,42])
oil_liquid_production = oil_liquid_production.iloc[0:39]
oil_liquid_production.set_index('Country',drop=True,inplace=True)
oil_liquid_production


# In[6]:


oil_liquid_production.to_csv('completed_flow/data/oil_liquid_production.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




