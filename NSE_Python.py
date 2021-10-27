#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nsepython import *   
print(indices)
import datetime
from pynse import *
nse=Nse()


# In[25]:


from datetime import datetime
import os

today = datetime.now()

DATE = today.strftime('%d_%m_%Y')
DATE_DIR = r"C:/Users/Adhaar Sharma/Desktop/"+DATE
if not os.path.exists(DATE_DIR):
    os.mkdir(DATE_DIR)
TIME = today.strftime('%H_%M_%S')
TIME_DIR = DATE_DIR+r"/"+TIME
os.mkdir(TIME_DIR)


# In[31]:


A = nse.info('SBIN')
df1 = pd.DataFrame(A.items())
df1
DF1_DIR = TIME_DIR+r"/nse.info"
if not os.path.exists(DF1_DIR):
    os.mkdir(DF1_DIR)
df1.to_csv(DF1_DIR+'/nse_info.csv')


# In[4]:


nse.update_symbol_list()


# In[30]:


A = fnolist()
df2 = pd.DataFrame({'col':A})
df2
DF2_DIR = TIME_DIR+r"/fnolist"
if not os.path.exists(DF2_DIR):
    os.mkdir(DF2_DIR)
df2.to_csv(DF2_DIR+'/fnolist.csv')


# In[6]:


print(running_status())


# In[7]:


nse.market_status()


# In[32]:


df4 = nse.pre_open()
df4
DF4_DIR = TIME_DIR+r"/nse.pre_open"
if not os.path.exists(DF4_DIR):
    os.mkdir(DF4_DIR)
df4.to_csv(DF4_DIR+'/nse_pre_open.csv')


# In[33]:


A = nse_blockdeal()
df5 = pd.DataFrame(A.items())
df5
DF5_DIR = TIME_DIR+r"/nse.blockdeal"
if not os.path.exists(DF5_DIR):
    os.mkdir(DF5_DIR)
df5.to_csv(DF5_DIR+'/nse_blockdeal.csv')


# In[34]:


df6 = nse_fiidii()
df6
DF6_DIR = TIME_DIR+r"/nse.fiidii"
if not os.path.exists(DF6_DIR):
    os.mkdir(DF6_DIR)
df6.to_csv(DF6_DIR+'/nse_fiidii.csv')


# In[11]:


#Circular
print(nse_circular("latest"))
print(nse_circular("all"))


# In[12]:


#P-E,Sector
print(nse_eq("JUSTDIAL")['metadata']['pdSectorPe'])
print(nse_eq("JUSTDIAL")['metadata']['pdSectorInd'])


# In[35]:


df7 = nse.top_gainers(index=IndexSymbol.FnO, length=10)
df7
DF7_DIR = TIME_DIR+r"/nse.top_gainers"
if not os.path.exists(DF7_DIR):
    os.mkdir(DF7_DIR)
df7.to_csv(DF7_DIR+'/nse_top_gainers.csv')


# In[36]:


df8 = nse.top_losers(index=IndexSymbol.FnO, length=10)
df8
DF8_DIR = TIME_DIR+r"/nse.top_losers"
if not os.path.exists(DF8_DIR):
    os.mkdir(DF8_DIR)
df8.to_csv(DF8_DIR+'/nse_top_losers.csv')


# In[38]:


df9 = nse_get_top_gainers()
df9
DF9_DIR = TIME_DIR+r"/nse.get_top_gainers"
if not os.path.exists(DF9_DIR):
    os.mkdir(DF9_DIR)
df9.to_csv(DF9_DIR+'/nse_get_top_gainers.csv')


# In[39]:


df10 = nse_get_top_losers()
df10
DF10_DIR = TIME_DIR+r"/nse_get_top_losers"
if not os.path.exists(DF10_DIR):
    os.mkdir(DF10_DIR)
df10.to_csv(DF10_DIR+'/nse_get_top_losers.csv')


# In[40]:


df11 = nse_get_advances_declines()
df11
DF11_DIR = TIME_DIR+r"/nse_get_advances_declines"
if not os.path.exists(DF11_DIR):
    os.mkdir(DF11_DIR)
df11.to_csv(DF11_DIR+'/nse_get_advances_declines.csv')


# In[41]:


df12 = nse_results("equities","Quarterly")
df12
DF12_DIR = TIME_DIR+r"/nse_results"
if not os.path.exists(DF12_DIR):
    os.mkdir(DF12_DIR)
df12.to_csv(DF12_DIR+'/nse_results.csv')


# In[42]:


df13 = nse_events()
df13
DF13_DIR = TIME_DIR+r"/nse_results"
if not os.path.exists(DF13_DIR):
    os.mkdir(DF13_DIR)
df13.to_csv(DF13_DIR+'/nse_results.csv')


# In[43]:


df14 = pd.json_normalize(nse_holidays()['FO'])
df14
DF14_DIR = TIME_DIR+r"/nse_holidays"
if not os.path.exists(DF14_DIR):
    os.mkdir(DF14_DIR)
df14.to_csv(DF14_DIR+'/nse_holidays.csv')


# In[22]:


holiday_master(type='trading')


# In[23]:


holiday_master(type='clearing')


# In[24]:


nse_holidays(type='trading')


# In[ ]:




