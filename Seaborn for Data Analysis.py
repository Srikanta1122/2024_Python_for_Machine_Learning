#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#!pip install --upgrade numpy 


# In[3]:


df=sns.load_dataset('tips')


# In[4]:


df


# In[5]:


df.isnull().sum()


# In[6]:


sns.relplot(x='total_bill', y='tip', data=df, hue='day', style='time') 


# In[7]:


sns.relplot(x='total_bill', y='tip', data=df, style='day') 


# In[8]:


df['day'].value_counts()


# In[9]:


df['sex'].value_counts()


# In[10]:


import seaborn as sns


# In[11]:


df1=sns.load_dataset('dots') 


# In[12]:


df1


# In[13]:


#relplot
sns.relplot(df1['coherence'], df1['firing_rate'], data=df1, kind='line', hue='time', style='choice')


# In[14]:


sns.relplot(df1['coherence'], df1['firing_rate'], data=df1, kind='line', 
            hue='align', col='choice') 


# In[15]:


df1['choice'].value_counts()


# In[16]:


data=sns.load_dataset('tips')


# In[17]:


data.head()


# In[18]:


#catter plot
sns.catplot(x='day', y='total_bill', data=data)


# In[19]:


sns.catplot(x='day', y='total_bill', data=data, jitter=False)


# In[20]:


sns.catplot(x='day', y='total_bill', data=data, kind='swarm')


# In[21]:


#box plot
sns.catplot(x='day', y='total_bill', data=data, kind='box') # kind=box says that this is the box plot 


# In[22]:


#boxen plot
data=sns.load_dataset('diamonds')


# In[23]:


data


# In[24]:


sns.catplot(x='color', y='carat', data=data, kind='boxen')


# In[25]:


#violin plot
sns.catplot(x='carat', y='color', data=data, kind='violin', hue='cut')


# In[26]:


#bar plot
titanic=sns.load_dataset('titanic')


# In[27]:


titanic


# In[28]:


sns.catplot(x='sex', y='survived', kind='bar', data=titanic, hue='class') 


# In[29]:


#point plot
sns.catplot(x='sex', y='survived', kind='point', data=titanic, hue='class') 


# In[30]:


#joint plot
sns.jointplot(titanic['sex'], titanic['survived'])


# In[32]:


#pair plot
sns.pairplot(df) 


# In[39]:


#regression plot
sns.regplot(x='total_bill', y='tip', data=df) # use tips dataset


# In[ ]:





# In[ ]:





# In[ ]:




