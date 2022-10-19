#!/usr/bin/env python
# coding: utf-8

# ## DIY 1 

# 1)  Download the two files and load them into pandas data frames.

# In[44]:


import pandas as pd


# In[2]:


df1 = pd.read_excel("ticketPrices.xlsx")


# In[3]:


pdf = pd.read_csv("passengerData (1).csv")


# In[4]:


df1.head()


# In[5]:


pdf.head()


# 2) Merge the two files based on the column they share.

# In[6]:


ndf = pd.merge(df1, pdf, on="TicketType")
print(ndf)


# 3) Display the name of the oldest passengers

# In[7]:


max(ndf.Age)


# In[8]:


dff = pd.DataFrame( ndf, columns=['Name', 'Age']) 


# In[9]:


dff.sort_values(by=["Age"], inplace=True,ascending=False)
print(dff)


# In[10]:


dff.head(20)


# 4) Plot the data on a scatter plot that shows the Age vs. Ticket Prices

# In[39]:


ndf2 = pd.merge(df1, pdf)
ndf2.head()


# In[12]:


ndf2.plot.scatter(x = 'Age', y = 'Fare')


# 5) Plot only the data that shows female passengers aged 40 to 50 and who paid more than or equal to 40.

# In[48]:


fml = ndf2[(ndf2['Age'] >= 40) & (ndf2['Age'] <= 50) & (ndf2['Sex'] == 'female') & (ndf2['Fare'] >= 40)]


# In[50]:


fml.plot.scatter('Age', 'Fare')

