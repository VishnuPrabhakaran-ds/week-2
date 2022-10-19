#!/usr/bin/env python
# coding: utf-8

# ## DIY 3

# 1) Download the csv data file from WHO on Tuberculosis

# In[83]:


import pandas as pd


# In[3]:


tb = pd.read_csv('TB_burden_countries_2014-09-29.csv')
tb.head(10)


# In[6]:


tb.describe()


# 2) Replacing missing values.

# In[4]:


tb.isna().sum()


# In[69]:


print(tb['iso2'].mode())  


# In[5]:


tb ['iso2'] = tb ['iso2'].fillna(tb ['iso2'].mode()[0]) #replacing char variable with mode


# In[6]:


tb.isna().sum()


# In[7]:


tb = tb.fillna(tb.mean())


# In[8]:


tb.isna().sum()


# 3) Choose a number of columns with different shapes, for instance, "e_prev_100k_hi" is right skewed and visualise on an histogram

# In[9]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
  


# In[11]:


data_log = np.log(tb.e_prev_100k_hi)


# In[95]:


tb.hist(figsize=(20,20), edgecolor='black', density=True)


# 4) Apply a log transformation on the data. Numpy has a log function. and visualise. Observe the changes

# In[27]:


numeric_data = tb.select_dtypes(include=[np.number])
categorical_data = tb.select_dtypes(exclude=[np.number])

#numeric_data.shape[1]
#categorical_data.shape[1]


# In[41]:


dflog = np.log(numeric_data)


# In[96]:


dflog.hist(figsize=(30,30), edgecolor='black', range = (0,1), density = True)


# 5) Choose the numerical columns and map all the columns to [0,1] interval

# In[58]:


fig, axs = plt.subplots(nrows=1, ncols=2)
axs[0].hist(tb.e_prev_100k_lo, edgecolor='black', range =(0,1))
axs[1].hist(dflog.e_prev_100k_lo, edgecolor='black', range =(0,1))
axs[0].set_title('Original Data')
axs[1].set_title('Log-Transformed Data')


# In[57]:


fig, axs = plt.subplots(nrows=1, ncols=2)
axs[0].hist(tb.e_prev_100k_hi, edgecolor='black', range =(0,1))
axs[1].hist(dflog.e_prev_100k_hi, edgecolor='black', range =(0,1))
axs[0].set_title('Original Data')
axs[1].set_title('Log-Transformed Data')


# In[60]:


fig, axs = plt.subplots(nrows=1, ncols=2)
axs[0].hist(tb.e_inc_tbhiv_100k_lo, edgecolor='black', range =(0,1))
axs[1].hist(dflog.e_inc_tbhiv_100k_lo, edgecolor='black', range =(0,1))
axs[0].set_title('Original Data')
axs[1].set_title('Log-Transformed Data')


# In[93]:


tb.mean(), range(0,1)


# In[98]:


dataframe_num_mappedv= tb


# In[101]:



for cl in tb.columns:
    mx = tb[cl].max()
    mn = tb[cl].min()
    dataframe_num_mapped[cl] = (tb[cl] - mn) / (mx - mn)

