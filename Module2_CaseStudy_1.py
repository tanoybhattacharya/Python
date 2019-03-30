
# coding: utf-8

# 1.Write a program which will find factors of given number and find whether the factor is even or odd

# In[4]:


n= num = int(input('Enter a number:'))
fact =1
while n>1:
    fact*=n
    n-=1
if fact%2==0:
    print('The factorial of %d is %d which is even number.'%(num,fact))
else:
    print('The factorial of %d is %d which is odd number.'%(num,fact))


# 2. Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically

# In[7]:


print(','.join(sorted(list(set([word for word in input("Enter a series of words with comma seperator:").split(',')])))))


# 3.Write a program, whichwill find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line

# In[14]:


print([x for x in range(10,30) if x%2==0]) 


# 4.Write a program that accepts a sentence and calculate the number of letters and digits

# In[9]:


import re

str = list(input("Enter a String:"))
l = d = 0
for i in str:
    if re.search('[A-Z]',i) or re.search('[a-z]',i):
        l+=1 
    elif re.search('[0-9]',i):
        d+=1
print('LETTER:',l)
print('DIGIT:',d)


# 5.Design a code which will find the given number is Palindrome number or not

# In[18]:


str=input('Enter a String:')
if str == str[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')

