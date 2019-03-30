
# coding: utf-8

# From the raw data below create a data frame'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 'age': [42, 52, 36, 24, 73], 'preTestScore': [4, 24, 31, ".", "."],'postTestScore': ["25,000", "94,000", 57, 62, 70]

# In[4]:


import pandas as pd
import numpy as np

example ={
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
    'last_name': ['Miller', 'Jacobson', "", 'Milner', 'Cooze'], 
    'age': [42, 52, 36, 24, 73], 'preTestScore': [4, 24, 31, "", ""],
    'postTestScore': ["25,000", "94,000", 57, 62, 70]
}

df = pd.DataFrame(example)


# Save the dataframe into a csv file as example.csv

# In[5]:


df.to_csv('example.csv')


# Read the example.csv and print the data frame

# In[6]:


df = pd.read_csv('example.csv')
df


# Read the dataframe by skipping first 3 rows and print the data frame

# In[7]:


df[3:]


# From the raw data below create a Pandas Series'Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'

# In[8]:


sr = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])


# Print all elements in lower case

# In[16]:


sr.str.lower()


# Print all the elements in upper case

# In[17]:


sr.str.upper()


# Print the length of all the elements

# In[18]:


sr.str.len()


# 6.7: Create pandas series and print true if value is alphanumeric in series or false if value is not alpha numeric in series.'1', '2', '1a', '2b', '2003c'

# In[23]:


sr = pd.Series(['1', '2', '1a', '2b', '2003c'])
sr.str.isnumeric()


# 6.8: Create pandas series and print true if value is containing ‘A’'1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c

# In[25]:


sr = pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])
sr.str.contains('A')


# 6.10: Create pandas dataframe having keys and ltable and rtable as below -'key': ['One', 'Two'], 'ltable': [1, 2]'key': ['One', 'Two'], 'rtable': [4, 5]

# In[26]:


dict1 = {'key': ['One', 'Two'], 'ltable': [1, 2]}
dict2 = {'key': ['One', 'Two'], 'rtable': [4, 5]}
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
pd.merge(df1,df2, on='key')

