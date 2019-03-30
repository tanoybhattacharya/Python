
# coding: utf-8

# 1.What is the output of the following code?
# nums =set([1,1,2,3,3,3,4,4])
# print(len(nums))

# In[1]:


nums =set([1,1,2,3,3,3,4,4]) 
print(len(nums))


# 2.What will be the output? d ={"john":40, "peter":45}print(list(d.keys()))

# In[2]:


d ={"john":40, "peter":45}
print(list(d.keys()))


# 3.A website requires a user to input username and password to register. Write a program to check the validity of password given 
# by user. Following are the criteria for checking password:
#     1. At least 1 letter between [a-z]
#     2. At least 1 number between [0-9]
#     3. At least 1 letter between [A-Z]
#     4. At least 1 character from [$#@]
#     5. Minimum length of transaction password: 6
#     6. Maximum length of transaction password: 12

# In[4]:


import re
p = input("Enter Password: ")
x = True
while x:
    if (len(p)<5) or (len(p)>13):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("/s",p):
        break
    else:
        print("Valid Password")
        x= False

if x:
    print("Invalid Password")


# 4.Write a for loop that prints all elements of a list and their position in the list.a = [4,7,3,2,5,9] 

# In[5]:


a=[4,7,3,2,5,9]
for i in a:
    print ('The value is %d and correspondece index is %d.'%(i,a.index(i)))


# 5.Please   write   a   program   which accepts  a   string   from   console   and   print   the characters that have even indexes.
# Example: If the following string is given as input to the program:
# H1e2l3l4o5w6o7r8l9dThen, 
# the output of the program should be:
# Helloworld

# In[8]:


import re

str = input("Enter a String:")
ostr = ''
for i in str:
    if re.search('[A-Z]',i) or re.search('[a-z]',i):
        ostr +=i
print(ostr)


# 6.Please write a program which accepts a string from console and print it in reverse order

# In[13]:


str = input('Please Enter a String:')
print(str[::-1])


# 7. Please write a program which count and print the numbers of each character in a string input by console

# In[14]:


str = input('Enter a String:')
dict = {}
for i in str:
    keys = dict.keys()
    if i in keys:
        dict[i]+=1
    else:
        dict[i] =1
print(dict)


# 8.With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],   write   a program to make a list whose elements are intersection of the above given lists.

# In[15]:


s1 = [1,3,6,78,35,55]
s2 = [12,24,35,24,88,120,155]
print(set(s1)&set(s2))


# 9.By usinglist comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

# In[16]:


lst = [12,24,35,24,88,120,155]
print([x for x in lst if x!=24])


# 10.By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]

# In[19]:


lst = [12,24,35,70,88,120,155]
print([x for (i,x) in enumerate(lst) if i not in [0,4,5]])


# 11. By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]

# In[29]:


lst = [12,24,35,70,88,120,155]
print(sorted(list(set(lst)-set([x for x in lst if x%5==0 and x%7==0]))))


# 12. Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0)

# In[30]:


n = input("Please Enter a Numebr:")

while int(n)<3:
    n = input("Please Enter a Numebr:")

N=int(n)
sum = 0
i=2
while i<=N:
    sum= sum +((i-1)/i)
    i+=1
print (round(sum,2))

