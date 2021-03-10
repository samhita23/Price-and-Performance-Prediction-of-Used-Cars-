#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


data=pd.read_excel(r'C:\Users\chama\Downloads\dat\cars_datafinal.xlsx')
data


# ## Cleaning the Price column
# 

# In[5]:


data['Price']=data['Price'].str.replace(r'₹','').str.replace(r',','') # removing '₹' and ',' from price column
data['Price']=pd.to_numeric(data['Price'])# converting price from str to numeric 


# In[6]:


## Cleaning the Rating column


# In[7]:


data['Rating']=data['Rating'].str.replace(r'out of 5','') # removing 'out of 5 ' from rating
data['Rating']=data['Rating'].str.replace(r'^4$','4.').str.replace(r'^3$','3.') # there some values containing '4$' and '3$' ,replacing them


# In[8]:


data['Rating']=data['Rating'].replace(r'',5.,regex=True)
data['Rating'].value_counts()


# ## Cleaning City Column

# In[10]:


city_dict={3686:'hyderabad',5732:'chennai',4709:'bengalore',777:'kolkata',2423:'pune',2378:'mumbai',290:'lucknow',1692:'ahmedabad',2130:'jaipur',769:'chandigarh'}


# In[12]:


data['city']=data['city'].replace( city_dict)


# In[14]:


import plotly.express as px


# ### Kilometers column

# In[15]:


data['Kilometers']=data['Kilometers'].str.lstrip('Kilometers') # splitting kilometers column and removing kilometers from it
data['Kilometers']=data['Kilometers'].str.replace(r',','') # removing ','
data['Kilometers']=data['Kilometers'].str.rstrip(' km')# removing 'km'
data['Kilometers']=pd.to_numeric(data['Kilometers']) # converting them to numeric
data['Kilometers']


# ## Year of purchase column

# In[16]:


data['Year_of_Purchase']=data['Year_of_Purchase'].str.lstrip('Year of Purchase')# splitting  years column and removing 'year of purchase'
data['Year_of_Purchase']


# ## Owner column

# In[17]:


data['Owner']=data['Owner'].str.strip('Owner')# splitting owner and removing owner from it
data['Owner']


# ## Fuel type colomn

# In[18]:


data['Fuel_Type']=data['Fuel_Type'].str.replace(r'Fuel','')# removing 'fuel' from it
data['Fuel_Type']


# ## Transmission colomn

# In[19]:


data['Transmission']=data['Transmission'].str.replace(r'Transmission','') # 'transmission' from it
data['Transmission']


# ## Insurance column

# In[20]:


data['Insurance']=data['Insurance'].str.lstrip('Insurance') # splitting insurance and removing 'Insurance' from it
data['Insurance'] 


# ## Insurancetype column

# In[21]:


data['Insurance_Type']=data['Insurance_Type'].str.replace('Insurance Type','')  # removing 'Insurance type' from it
data['Insurance_Type']


# In[22]:


# converting insurance_type to standard notation categories
data['Insurance_Type']=data['Insurance_Type'].str.replace(r'_Dep','Depreciation') 
data['Insurance_Type']=data['Insurance_Type'].str.replace(r'Zero ','Zero')
data['Insurance_Type']=data['Insurance_Type'].str.replace(r'Comp$','Comprehensive')
data['Insurance_Type']=data['Insurance_Type'].str.replace(r'3rd P','Third_p')
data['Insurance_Type']=data['Insurance_Type'].str.lstrip('Insurance ')


# In[23]:


data['Insurance_Type'].value_counts()


# In[24]:


data['Insurance_Type']=data['Insurance_Type'].str.replace('ll','').str.replace('NA','') # replacing 'l1' with nan
data['Insurance_Type'].value_counts()


# In[25]:


data['Insurance_Type']=data['Insurance_Type'].replace(r'^\s*$',np.NaN,regex=True) # trying to look for any whitespaces from start to end


# In[26]:


data['Insurance_Type'].isnull().sum()


# ## Creating New Columns

# In[27]:


data[['Month_of_Purchase','Year_of_Purchase']]=data.Year_of_Purchase.str.split(expand=True) # splitting year of purchase into two columns


# In[28]:


#data=data[['Name','Price','Rating','Kilometers','Month_of_Purchase','Year_of_Purchase','Owner','Fuel_Type','Transmission','RTO','Insurance','Insurance_Type']]


# In[29]:


data


# In[ ]:




