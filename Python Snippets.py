#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Creating to two empty lists
list1=[]
list2=[]
#Creating a variable to store range of list1
n1=int(input("Enter the range of list 1 :"))
#Creating a loop for storing user input data for list1
for i in range(0,n1):
    num1=int(input())
    list1.append(num1)
#Creating a variable to store range of list2
n2=int(input("Enter the range of list 2 :"))
#Creating a loop for storing user input data for list2
for j in range(0,n2):
    num2=int(input())
    list2.append(num2)
#Printing both the lists
print(list1)
print(list2)

    
    
    


# In[26]:


#Creating a tuple
students=("Sumesh","Ramesh","Sathish","Rahul","Mrinal")
print(students)
for pos in students:
#Entering postion to be displayed in the tuple
    pos=int(input("Enter the position you want to access :"))
#Printing the name in the entered position
    print(students[pos])
    break
    
    
    
    
    
    
    
    
    


# In[2]:


students={"A":"Excellent","B":"Good","C":"Average","D":"Poor"}
print(students)
for ele in students:
    ele=input("Enter the element you would like to delete :")
    break
#Deleting the dictionary element from the dictionary
students.pop(ele)
print(students)









# In[ ]:




