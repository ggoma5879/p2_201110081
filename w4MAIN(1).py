
# coding: utf-8

# In[176]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


# In[177]:

size= 0
angle= 0
i=0
sides=0
bigger=10


# In[184]:

def bangbangbang(size,angle,bigger,sides):
        for i in range(0,sides):
            if i%2:
                size
            else : 
                size=size+bigger
            t1.fd(size)
            t1.right(angle)


# In[185]:

bangbangbang(100,72,10,20)


# In[ ]:

wn.exitonclick()


# In[183]:

t1.home()
t1.clear()


# In[ ]:



