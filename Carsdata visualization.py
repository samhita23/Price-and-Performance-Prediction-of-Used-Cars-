#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[3]:


import pandas as pd
import numpy as np


# In[23]:


data=pd.read_csv(r'C:\Users\chama\Downloads\dat\Cars24_data.csv')
data


# In[5]:


# ?print('Number of data points in dataset:',data.shape[0])


# In[6]:


# creating new column for car's brand.

data['car_model']=data['Name'].str.split()
for i in range(len(data)):
    data['car_model'][i]= data['car_model'][i][0]


# In[7]:


print('column         type of column')
data.dtypes


# ## Univariate Plots

# ## Count plot on 'city'

# In[8]:


plt.figure(figsize=(10,6)) # setting desired size of plot
data['city'].value_counts().plot(kind='bar')# using bar plot for city
plt.grid()                        # adding grids to the plot 
plt.title('city vs count')


# #### Observation - 
# 1.From above plot we can conclude that hyderabad city has most number resale cars uploaded in cars24 and followed by banglore.

# ## Count plot on 'car model'

# In[9]:


plt.figure(figsize=(18,9))
data['car_model'].value_counts().plot(kind='bar')
plt.grid()
plt.title('car_model vs count')


# #### Observation
# 
# 1.From above plot we can infer that people buy maruti cars and since they  buy maruti cars ,generally the resale number count of is brand is also more.
#  
# 2.We can say maruti has high demand in india

# ## Count plot on type of owner

# In[11]:


plt.figure(figsize=(10,6))
data['Owner'].value_counts().plot(kind='bar')
plt.grid()
plt.title('type_of_owner vs count')


# ###Observation
# 1.From above plot we can obviously say that first owner of the cars are maximum which justifies our answer.

# ### Count plot on 'Rating of Car'

# In[28]:


plt.figure(figsize=(15,8))
data['Rating'].value_counts().plot(kind='bar')
plt.grid()
plt.title('ratings of cars vs count')


# #### observation:
# 
# 1.People usually give higher rating which can be observed from plot above.

# ## Count plot of 'Purchases based on Month'

# In[29]:


plt.figure(figsize=(10,6))
data['Month_of_Purchase'].value_counts().plot.bar()
plt.grid()
plt.title('purchases based on month vs count')


# #### Observation
# 
# 1.January has highest purchase because its common sense that its new year and people wait until every january to buy vehicles because it will get high value for example ,A car bought in Jan 2021 will fetch more value than a car bought in December 2020. 
# 

# ## Count plot on 'Fuel type'

# In[30]:


plt.figure(figsize=(8,6))
data['Fuel_Type'].value_counts().plot.bar()
plt.grid()
plt.title('fuel_type vs count')


# #### Observation
# 
# 1.Diesel and petrol cars are still in bought more and sold more.

# ## Count plot on 'year of purchase'

# In[31]:


plt.figure(figsize=(18,8))
data['Year_of_Purchase'].value_counts().plot.bar()
plt.grid()
plt.title('Year_of_Purchase vs count')


# #### Observation:
# 
# 1.From above plot infer that people generally resale their cars after 5,6,7,8 years since we can see the years 2012 ,2015,2016,2013 has similar count.

# ## Distribution plot of 'Kilometers'

# In[33]:


plt.figure(figsize=(10,8))
sns.distplot(data['Kilometers'])
plt.title('Kilometers')


# #### Observation
# 
# 1.Most of cars are being re-selled after using 200000 KM.
# 
# 2.Distribution is positively skewed.

# ## Piechart for transmission

# In[34]:


plt.figure(figsize=(8,7))
plt.pie(data['Transmission'].value_counts(),startangle=90,autopct='%.3f',labels=['MANUAL','AUTOMATIC'],explode=[0.2,0],shadow=True)
plt.legend()


# #### Observation
# 
# 1.Its obvious that maunal transmission cars have domination since automatic transmission costs lot higher.

# ## Ploting Insurance type

# In[35]:


data['Insurance_Type'].value_counts()


# In[36]:


plt.figure(figsize=(10,5))
data['Insurance_Type'].value_counts().plot.bar()
plt.title('Freequency of Insurance types')


# #### Observation
# 
# 1.People generally prefer comprehensive insurance type and many people dont consider renewing the expired insurance of their cars.

# ## Distribution of target vaiable

# In[38]:


plt.figure(figsize=(10,8))
sns.distplot(data['Price'])
plt.title('Price')


# #### Observation
# 
# Except some high end cars most car has low price.

# # Multivariate Analysis
# 
# Multivariate analysis is a set of statistical techniques used for analysis of data that contain more than one variable

# In[39]:


## Bivariate plots


# ### Scatterplot between Year_of_Purchase and price

# In[40]:


fig = px.scatter(data, x="Year_of_Purchase", y="Price")
fig.show()


# #### Observation
# 
# 1.Since we scatter plot between categorical(year_of_purchase) and numerical variable(price) ,here we should not look for any correlation

# ### Scatterplot between kilometer and price

# In[41]:


fig = px.scatter(data, x="Kilometers", y="Price")
fig.show()


# #### Observation 
# 
# In the above scatter plot there is no linear relationship between price and kilometers

# ### Barplot between (city vs Price),(city vs kilometer)

# In[44]:


plt.figure(figsize=(10,5))
sns.barplot(x="city", y="Price", data=data)

plt.figure(figsize=(10,5))
sns.barplot(x="city", y="Kilometers", data=data)


# #### Observation
# 
# 1.From first plot here we can infer that mean price of cars does not vary that much and similar results can be seen in second plot that kilometers driven is also moreover similar excluding kolkata.

# ### Barplot between (owner vs Price),(owner vs kilometer)

# In[45]:


plt.figure(figsize=(10,5))
sns.barplot(x="Owner", y="Price", data=data)
plt.figure(figsize=(10,5))
sns.barplot(x="Owner", y="Kilometers", data=data)


# #### Observation
# 
# 1.Owner vs price graph shows that first owner car will obviously have high price followed by rest ,but here in our dataset we have owner upto 10 .
# 
# 2.Owner vs kilometer graph shows inverse relation with owner vs price graph and that is judgemental since first owner would drive less Kilometers than rest of owner types.

# ### Barplot between (Fuel_type vs kilometer),(Fuel_type vs Price)

# In[46]:


plt.figure(figsize=(10,5))
sns.barplot(x="Fuel_Type", y="Kilometers", data=data)


plt.figure(figsize=(10,5))
sns.barplot(x="Fuel_Type", y="Price", data=data)


# ### Observation
# 1.From first plot we can infer that petrol cars are usually sold eariler than diesel,Petrol+lpg and petrol+cng cars.
# 
# 2.From second plot we can take that hybrid cars is highly priced.

# ### Barplot between (Year_of_Purchase vs price),(Year_of_Purchase vs kilometers)

# In[47]:


plt.figure(figsize=(19,5))
sns.barplot(x="Year_of_Purchase", y="Price", data=data)
plt.figure(figsize=(19,5))
sns.barplot(x="Year_of_Purchase", y="Kilometers", data=data)


# #### Observation
# 1.If someone sells his car in 1 year then the resale of the car will be close to new car price.
# 
# 2.Both graphs should idealy have inverse relation which is true for most extent .

# ### Barplot between (Transmission vs  kilometers),(Transmission vs price)

# In[48]:


group=data.groupby('Transmission')['Kilometers'].mean().plot(kind='bar')
plt.ylabel('Kilometers')
plt.show()

group=data.groupby('Transmission')['Price'].mean().plot(kind='bar')
plt.ylabel('Price')
plt.show()


# #### Observation
# 
# 1.Mostly automatic transmission cars are expensive which can be reflected from 2nd plot.

#  ### Barplot between rating vs price

# In[49]:


plt.figure(figsize=(18,8))

sns.barplot(x="Rating", y="Price", data=data)
plt.title('price based on rating')
plt.show()


# ####  Observation
# 1.Rating of car becomes one of the important variable which predict resale price of car. 
# 
# 2.Relation between rating and price of car is directly proportional

# ## More than 2 variable plots

# In[50]:


plt.figure(figsize=(16,12))
sns.pairplot(data)


# ### Numerical column's correlation

# In[51]:


data.corr()


# In[52]:


corrMatrix=data.corr()
sns.heatmap(corrMatrix,annot=True,cmap="YlGnBu", linewidths=2,center=2)
plt.show()


# #### Observation
# 1.Numerical variables like price and kilometers driven is not highly correlated ,but rating and year of purchase shows positive correlation.
# 
# 2.Year purchase is a categorical variable and can be used to predict price of car .
# 

# #### pandas Crosstabs

# In[53]:


stack_bar=pd.crosstab(data['Owner'],data.Insurance_Type,margins=True)
stack_bar


# In[54]:


stack_bar.plot(kind='bar',stacked=True,grid=True,figsize=(10,7))


# In[55]:


stack_bar_1 = pd.crosstab([data.Transmission,data.Fuel_Type],data.Owner,margins=False)


# In[56]:


stack_bar_1


# In[57]:


stack_bar_1.plot(kind='bar',stacked=True,grid=True,figsize=(8,6))


# In[58]:


stacked=pd.crosstab([data.Transmission,data.Fuel_Type],data.Month_of_Purchase,margins=True)
stacked


# In[59]:


stacked.plot(kind='bar',stacked=True,grid=True,figsize=(17,8))


# In[60]:


stacked_bar2=pd.crosstab([data.Transmission,data.Fuel_Type,data.Owner],data.Insurance_Type,margins=False)
stacked_bar2


# In[61]:


stacked_bar2.plot(kind='bar',stacked=True,grid=False,figsize=(17,8))


# #### Observation
# 
# 
# 1.Stacked bar plots are used to show relation between multiple categorical variables vs count of that variables.But we can get much information only if we have less number of categories in each categorical column.

# In[ ]:




