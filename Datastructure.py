#!/usr/bin/env python
# coding: utf-8

# # Linear search

# In[6]:


def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            return True
        i=i+1
    return False
list=[5,8,4,6,9,2]
n=9
if search(list,n):
    print("Number Found")
else:
    print("Not Found")


# # Binary search

# In[7]:


list=[4,8,9,12,15]
low=0
high=4
search=12
def binarySearch(low,high):
    if(low < high):
        middle = (low+high)//2
        if search == list[middle]:
            print("Element Found")
            return middle
        elif search < list[middle]:
            high = middle - 1
            binarySearch(low,high)
        elif search > list[middle]:
            low = middle + 1
            binarySearch(low,high)
    else:
        print("Element Not Found")
binarySearch(low,high)
           


# # Bubble sort

# In[8]:


n = int(input("Enter number of elements"))
lst=[]
for i in range(n):
    ele =int(input("Enter the number"))
    lst.append(ele)
print(lst)

def BubbleSort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i+1,n):
            if lst[i]>lst[j]:
                t=lst[i]
                lst[i]=lst[j]
                lst[j]=t
    return lst
BubbleSort(lst)


# # selection sort

# In[9]:


def SelectionSort(lst):
    for i in range(n):
        min1=i
        for j in range(i+1,n):
            if lst[j]<lst[min1]:
                min1=j
    
        lst[min1],lst[i]=lst[i],lst[min1]
    return lst
SelectionSort(lst)


# # Insertion sort

# In[10]:


def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        # Place key at after the element just smaller than it.
        array[j + 1] = key
data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)


# 
