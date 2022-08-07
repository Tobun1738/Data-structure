#!/usr/bin/env python
# coding: utf-8

# In[9]:


def last(n):
    return n[-1] 
  
def sort(tuples):
    return sorted(tuples, key=last)
  
a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort(a))



#question2


# In[42]:


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)


#question3


# In[12]:


n=int(input("enter a number: "))
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)


#question 4


# In[36]:


list= [('item1','12.20'), ('item2','15.10'), ('item3','24.5')]
print(list[2],list[1],list[0])



#Question 5


# In[41]:


p= [2*3*6]
print(p)


#question1


# In[ ]:




