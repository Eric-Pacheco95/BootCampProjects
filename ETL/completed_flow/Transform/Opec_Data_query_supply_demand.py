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



Opec_supply_demand = pd.read_csv('completed_flow/Extract/opec/Opec_supply_demand.csv')  
Opec_supply_demand.rename(columns={'Country':'Country/Region'},inplace=True)
Opec_supply_demand.set_index('Country/Region',drop=True,inplace=True)
Opec_supply_demand = Opec_supply_demand.drop(Opec_supply_demand.columns[0], axis=1)
Opec_supply_demand


# In[4]:


Opec_supply_demand
world_demand = Opec_supply_demand.iloc[2:11]
world_demand.to_csv('completed_flow/data/world_demand.csv')
world_demand


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




