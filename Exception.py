#!/usr/bin/env python
# coding: utf-8

# # # Exception

# In[5]:


amount = 10000
 

if(amount > 2999)
    print("You are eligible to purchase")


# In[6]:


#divide by zero exception
marks = 10000

a = marks / 0
print(a)


# In[7]:


#catch exception using try except

a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))
 
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
except:
    print ("An error occurred")


# In[9]:


def fun(a):
    if a < 4:
 
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
  
    # throws NameError if a >= 4
    print("Value of b = ", b)
     
try:
    #fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")


# In[11]:


#try with else clause

def call(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
 
# Driver program to test above function
call(2.0, 3.0)
call(3.0, 3.0)


# In[13]:


#using finally 
try:
    k = 5/0  # raises divide by zero exception.
    print(k)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print('This is always executed')


# In[17]:


#raise statement
try:
    raise ValueError
except ValueError:
    print('There was an exception.')

