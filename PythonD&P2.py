#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing libraries

import pandas as pd
import seaborn as sbn
import numpy as np


# In[3]:


from matplotlib import pyplot as plt


# In[5]:


# importing the variable description dataset 
# that gives information about my dataset
VariableDescription= pd.read_csv('VariableDescription.csv')


# In[6]:


VariableDescription


# In[4]:


#importing the train_data dataset.

train_data= pd.read_csv('train_data.csv')


# In[5]:


train_data


# In[12]:


# this states how my dataset is stored
type(train_data)


# In[13]:


# to know how many features i have in the dataset,int,float, 
# object, null and non-null observed no null
#the shape of my dataset

train_data.shape
train_data.info()


# In[6]:


#Removing unimportant variables from the dataset

drop_colums = ['Geo_Code', 'Building Dimension', 'NumberOfWindows']

train_data = train_data.drop(drop_colums, axis=1)


# In[7]:


#after removing unimportant variables

train_data.info()


# In[16]:


# Summary statistics of the dataset

train_data.describe()


# In[17]:


# including the object type inthe summary statistics

train_data.describe(include=object)


# In[12]:


train_data.describe() .T


# In[18]:


train_data.dtypes


# In[19]:


train_data.dtypes.value_counts()


# In[20]:


train_data.select_dtypes(object).columns


# In[21]:


#Geting individual mean to better understand the dataset

train_data.mean()


# In[22]:


# standard deviation of the dataset 

train_data.std()


# In[23]:


train_data.quantile()


# In[24]:


#Correlations of the dataset

train_data.corr()


# In[25]:


# correlation between yearofobservation and targetvariable claim

train_data[['YearOfObservation', 'Claim']].corr()      
                   


# In[26]:


#sorting out the data by target variable which is Claim

train_data_sort = train_data.sort_values(by='Claim', ascending=False)

train_data_sort


# In[27]:


#Plotting histogram for continuous numerical variable Claim

num_of_bins=10

plt.hist(train_data['Claim'],num_of_bins)


# In[28]:


#using seaborn to get the  probability density function

sbn.distplot(train_data['Claim'],bins=10)


# In[29]:


#Plotting histogram for continuous numerical variable insured period

num_of_bins=10

plt.hist(train_data['Insured_Period'],num_of_bins)


# In[30]:


#using seaborn to get the  probability density function

sbn.distplot(train_data['Insured_Period'],bins=10)


# In[31]:


#Selecting the colums that are numeric that is, float64 and int64

train_data.select_dtypes("number")


# In[32]:


#Using groupby for cross tabulation to count categorical variables 
making_distri = train_data.groupby('Customer Id').size()


# In[35]:


making_distri


# In[33]:


making_distri.plot(title='Customer identification')


# In[34]:


# selecting all numerical variables

train_data_num = train_data.select_dtypes(include=['float64', 'int64'])

train_data_num


# In[35]:


#plotting histogram of all numerical variables

train_data_num.hist(bins=20)


# In[36]:


#correlation with the target variable

train_data_corre = train_data_num.corr()['Claim'][:-1]


# In[37]:


train_data_corre


# In[ ]:


#boxplot of categorical variable

boxplt1 = sbn.boxplot(x='Customer Id', y='Claim', data=train_data)


# In[ ]:


#boxplot of categorical variable

boxplt2 = sbn.boxplot(x='Settlement', y='Claim', data=train_data)


# In[ ]:


#boxplot of categorical variable

boxplt3 = sbn.boxplot(x='Building_Fenced', y='Claim', data=train_data)


# In[ ]:


#boxplot of categorical variable

boxplt4 = sbn.boxplot(x='Garden', y='Claim', data=train_data)


# In[43]:


#boxplot of categorical variable

boxplt5 = sbn.boxplot(x='Building_Painted', y='Claim', data=train_data)


# In[8]:


#histogram of  the dataset

train_data.hist(figsize=(20,20))
#setting a large fig size because the dataset is many
plt.tight_layout()
plt.show()


# In[9]:


#creating regression plot to determine the relationship between targetvariable
# and other variable

sbn.regplot(train_data['Insured_Period'],train_data['Claim'])


# In[ ]:





# In[ ]:




