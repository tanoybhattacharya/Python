
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Salaries.csv')
df.shape


# Compute how much total salary cost has increased from year 2011 to 2014

# In[28]:



totalsal_2011=df['TotalPay'][df['Year']==2011].sum()
totalsal_2014=df['TotalPay'][df['Year']==2014].sum()

print('Total salary cost has increased from year 2011 to 2014 :%.2f'%(totalsal_2014-totalsal_2011))


# In[11]:


df.head(1)


# Which Job Title in Year 2014 has highest mean salary

# In[88]:


df_2014=df[['JobTitle','TotalPay']][df['Year']==2014]
df_2014=df_2014.groupby(['JobTitle']).mean()
df_2014[df_2014['TotalPay']==df_2014['TotalPay'].max()]


# How much money could have been saved in Year 2014 by stopping OverTimePay

# In[45]:


df.head(5)


# In[ ]:


df_ot= df[['Year','OvertimePay']]
pd.options.display.float_format = '{:,.2f}'.format

print('%.2f have been saved in Year 2014 by stopping OverTimePay'%(df_ot['OvertimePay'][df_ot['Year']==2014].sum()))


# Which are the top 5 common job in Year 2014 and how much do they cost SFO

# In[2]:


df_2014=df[['JobTitle','TotalPay']][df['Year']==2014]
df_job=df_2014.groupby(['JobTitle']).count()
df_job.reset_index(inplace=True)
df_job.sort_values(by='TotalPay', ascending=False,inplace=True)
df_job[['JobTitle','TotalPay']].head(5)


# Who was the top earning employee across all the years

# In[4]:


df[df['TotalPay']==df['TotalPay'].max()]

