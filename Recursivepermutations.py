
# coding: utf-8

# In[49]:


def perm(number,couple=0):
   if(couple==len(number)):
      print (number)
   else:
      for i in range(couple,len(number)):
         number[couple],number[i] = number[i],number[couple]
         perm(number, couple+1)
         number[couple],number[i] = number[i],number[couple]

print(perm([1,2]))


# In[ ]:





# In[ ]:




