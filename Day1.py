#!/usr/bin/env python
# coding: utf-8

# In[2]:


#sum of 2 numbers taking input from the user,if any one of the input is zero then break

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
if(num1 ==0 or num2==0):
    print("Input should not be empty")
else:
    sum = num1 + num2
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# In[3]:


import pandas as pd

names=pd.read_csv("names.csv")
print(names)


# In[5]:


def greatest_num(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
 
 
num = int(input('How many numbers to check: '))
 
lst = []
 
for n in range(num):
    numbers = int(input('Enter the number '))
    lst.append(numbers)
     
print("Greatest element in the list is :", greatest_num(lst))


# In[ ]:




