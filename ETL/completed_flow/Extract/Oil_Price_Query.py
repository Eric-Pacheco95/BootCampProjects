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


import pull


# In[74]:


brent_daily = pd.read_csv('completed_flow/Extract/oil_prices/brent_daily.csv')  
wti_daily = pd.read_csv('completed_flow/Extract/oil_prices/wti_daily.csv') 


# In[75]:


#brent_daily['Date_index'] = brent_daily['Date']

brent_daily = brent_daily.rename(columns={'Price':'Brent_Price_USD'})
brent_daily


# In[76]:




wti_daily = wti_daily.rename(columns={'Price':'WTI_Price_USD'})
wti_daily


# In[72]:





# In[78]:



oil_daily = pd.merge(brent_daily, wti_daily, on='Date')


# In[79]:


oil_daily.to_csv('completed_flow/data/daily_oil_prices_87_20.csv')


# In[ ]:




