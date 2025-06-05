#!/usr/bin/env python
# coding: utf-8

# # Website Analysis Project 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df= pd.read_csv('data-export (1).csv')


# In[3]:


df.columns =df.iloc[0]
df.head()  # show 5 data 


# In[4]:


df = df.drop(index = 0).reset_index(drop = True)
df.columns =["channel group", "DateHour" ,"user","Sessions","Engaged Sessions","Average engagement time per session","Engaged sessions per user","Events per session","Engagement rate","Event count"]


# In[5]:


df.head()


# In[6]:


# check the formate 
df.info()


# In[7]:


# covert the data type form object to int 
# use Date formate (Y/M/H)
df["DateHour"] =pd.to_datetime(df["DateHour"],format ="%Y%m%d%H", errors ='coerce')


# In[8]:


#for information 
df.info()
df.head()


# In[9]:


numeric_cols =df.columns.drop(["channel group","DateHour"]) # ye do column chod ke 
df[numeric_cols] =df[numeric_cols].apply(pd.to_numeric, errors ='coerce')
df["hour"] =df["DateHour"].dt.hour  # new Hour Column banaya 


# In[10]:


df.info()
df.head(3)


# In[11]:


df.describe()


# # Sessions and user over time

# In[12]:


# use DateHour , users , Sessions
sns.set(style ="whitegrid")


# In[13]:


plt.figure(figsize =(10,5))
df.groupby("DateHour")[["Sessions","user"]].sum().plot(ax=plt.gca())
plt.title("Sessions and users over time")
plt.xlabel("DateHour")
plt.ylabel("count")
plt.show()


# # Total users by channel

# In[14]:


# channel group and user 
plt.figure(figsize =(8,5))
plt.figure(figsize =(8,5))
sns.barplot(data=df,x="channel group", y ="user",estimator =np.sum,palette="viridis")
plt.title("Total users by channel")
plt.xticks(rotation =45)
plt.show()


# # Average engagement time by channel

# In[15]:


plt.figure(figsize =(8,5))
sns.barplot(data =df,x="channel group", y="Average engagement time per session",estimator =np.mean,palette="magma")
plt.title("Avg Engagement Time by Channel")
plt.xticks(rotation =45)
plt.show()


# # Engagement Rate Distribution

# In[16]:


plt.figure(figsize =(8,5))
sns.boxplot(data =df ,x ="channel group",y ="Engagement rate",palette ="coolwarm")
plt.title("Engagement Rate Distribution by Channel")
plt.xticks(rotation =45)
plt.show()


# # Engaged vs non engaged sessions

# In[17]:


session_df =df.groupby("channel group")[["Sessions","Engaged Sessions"]].sum().reset_index()
session_df["Non-Engaged"]=session_df["Sessions"] - session_df["Engaged Sessions"]
session_df_melted = session_df.melt(id_vars="channel group",value_vars =["Engaged Sessions","Non-Engaged"])

plt.figure(figsize=(8,5))
sns.barplot(data=session_df_melted, x="channel group", y ="value",hue ="variable")
plt.title("Engaged vs Non-Engaged Sessions")
plt.xticks(rotation =45)
plt.show()


# # Traffic by hour and channel

# In[19]:


heatmap_data = df.groupby(["hour", "channel group"])["Sessions"].sum().unstack().fillna(0)

plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap="YlGnBu", linewidths=0.8, annot=True, fmt='.0f')
plt.title("Traffic By Hour and Channel")
plt.xlabel("Channel Group")
plt.ylabel("Hour of Day")
plt.show()


# In[ ]:





# In[ ]:




