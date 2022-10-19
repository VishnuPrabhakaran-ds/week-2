#!/usr/bin/env python
# coding: utf-8

# ## DIY 2

# 1) Load the slightly modified Titanic survival data  into a pandas data frame

# In[2]:


#titanicSurvival_m.csv
import pandas as pd
titanic = pd.read_csv('titanicSurvival_m.csv')
titanic.head(10)


# 2) Find the counts of missing values in each column

# In[3]:


titanic.isna().sum()


# In[4]:


titanic.describe()


# 3) Compute the mean and other descriptive statistics and note these down, you can use this function

# In[5]:


Age_Mean = titanic['Age'].mean()
print("Average age of passengers is", Age_Mean)
Age_Median = titanic['Age'].median()
print("Median age of passengers is", Age_Median)
Age_Mode = titanic['Age'].mode()
print("Majority of Passenger's are", Age_Mode, "years old")
Age_Max = titanic['Age'].max()
print("Oldest Passenger", Age_Max, "years old")
Age_Min = titanic['Age'].min()
print("Youngest Passenger is", Age_Min, "years old")


# 4) Replace the missing values in "Age" and "Fare" columns with 0 values, and visualise in a scatterplot

# In[6]:


titanic2 = titanic.fillna({'Age': 0, 'Fare': 0})
print(titanic["Age"], titanic["Fare"])


# In[7]:


titanic2.isna().sum()


# In[8]:


#titanic.plot.scatter(x = 'Age', y = 'Fare')
import matplotlib.pyplot as plt
import numpy as np
plt.scatter(titanic2['Age'], titanic2['Fare'])
plt.show()


# 5) Replace the missing values in "Age" and "Fare" columns with the mean of each column, and visualise in a scatterplot

# In[9]:


titanic3 = titanic.fillna({'Age': titanic['Age'].mean(), 'Fare': titanic['Fare'].mean()})

titanic3.head()


# In[10]:


titanic3.plot.scatter(x = 'Age', y = 'Fare')


# 6) Reflect on the differences you see in these plots.

# In[11]:


plt.scatter(titanic2['Age'], titanic2['Fare'], c='red', label="titanic2")
plt.scatter(titanic3['Age'], titanic3['Fare'], c='green', label="titanic3")
plt.legend()

