#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df=pd.read_csv('mnist_test.csv')
df.head()


# In[5]:


dir(df)


# In[7]:


a=df.iloc[3,1:].values


# In[9]:


plt.plot(df.iloc[3,1:].values)b


# In[10]:


a=a.reshape(28,28).astype('uint8')
plt.imshow(a)


# In[13]:


inputs=df.drop('label',axis='columns')
inputs


# In[14]:


outputs=df.label
outputs


# In[15]:


x_train,x_test,y_train,y_test=train_test_split(inputs,outputs,test_size=0.2)


# In[20]:


rf=RandomForestClassifier(n_estimators=100)


# In[21]:


rf.fit(x_train,y_train)


# In[22]:


rf.score(x_test,y_test)


# In[23]:


rf.predict(x_test)


# In[24]:


y_test


# In[ ]:




