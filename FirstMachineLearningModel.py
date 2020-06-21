#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[14]:


from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


# In[15]:


from sklearn.datasets import load_iris


# In[16]:


iris= load_iris()


# In[17]:


dir(iris)


# In[23]:


df=pd.DataFrame(iris.data,columns=iris.feature_names)
df.head()


# In[27]:


df['flower']=iris.target
df['flower']=df['flower'].apply(lambda x:iris.target_names[x])


# In[28]:


df


# In[29]:


df.describe()


# In[40]:


x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.2)


# In[41]:


folds=StratifiedKFold(n_splits=3)


# In[43]:


score_l=[]
score_svm=[]
score_rf=[]

for train_index,test_index in folds.split(iris.data,iris.target):
    x_train,x_test,y_train,y_test=iris.data[train_index],iris.data[test_index],iris.target[train_index],iris.target[test_index]


# In[45]:


def get_score(model,x_train,x_test,y_train,y_test):
    model.fit(x_train,y_train)
    return model.score(x_test,y_test)


# In[46]:


score_l.append(get_score(LogisticRegression(),x_train,x_test,y_train,y_test))
score_svm.append(get_score(SVC(),x_train,x_test,y_train,y_test))
score_rf.append(get_score(RandomForestClassifier(),x_train,x_test,y_train,y_test))


# In[47]:


score_l


# In[48]:


score_svm


# In[49]:


score_rf


# In[50]:


lr=LogisticRegression()
lr.fit(x_train,y_train)


# In[51]:


lr.predict(x_test)


# In[52]:


y_test

