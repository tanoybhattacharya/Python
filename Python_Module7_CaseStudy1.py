
# coding: utf-8

# Create a pandas dataframe

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'float_col':[0.1,0.2,0.2,10.1,np.NAN],
    'in_col':[1,2,6,8,-1],
    'str_col':['a','b','None','c','a']
})

print(df)


# filter  the  columns  'float_col',  'int_col'  from  the  dataframe  in  one  query.  Hint-use  ix method of dataframes. Also print without using ix method

# In[14]:


df.iloc[:,0:2]


# filter the records from float_col having value greater than 0.15 and in separate query filter float_col valueequal to 0.1

# In[21]:


print(df[df['float_col']==0.1])
print(df[df['float_col']>0.15])


# filter  the  records  from data  frame which  satisfies  both  the  conditions  float_col greater than 0.1 and int_col greater than 2

# In[28]:


df[(df['float_col'] > 0.1) & (df['in_col'] >2)]


# filter  the  records  from  data  frame  which  satisfies  both  the  conditions  float_col greater than 0.1 or int_col greater than 2

# In[29]:


df[(df['float_col']>0.1)|(df['in_col']>2)]


# filter the records from data frame which satisfies the conditions float_col not greater than 0.1

# In[30]:


df[df['float_col']<=0.1]


# Create a new data frame in which column int_col is renamed to new_name

# In[2]:


df_new =df.copy()
df_new.rename(columns={'in_col':'new_name'},inplace = True)
df_new


# Modify the existing dataframe and rename the column int_col to new_name

# In[36]:


df.rename(columns={'in_col':'new_name'},inplace=True)
df


# Drop the rows where any value is missing from the dataframe

# In[3]:


df.dropna(inplace=True)
df


# Change the missing value in column float_col as mean value of the float_col

# In[4]:


mval = df_new['float_col'].mean()
df_new['float_col'].replace(np.NAN,mval, inplace=True)
df_new


# change  all  the  values  of  str_col  with  new  valueand  drop  the  missing  values.  New value should have prefixmap_ and original value. Eg map_a, map_b

# In[6]:


df_wrang = df_new.copy()
df_wrang.drop(2,inplace =True)
df_wrang['str_col'] = 'map_' +df_wrang['str_col'].astype(str)
df_wrang


# Group  all  the  values  of  str_col  and  find  the  mean  of  float_col  in  all  the  groups respectively

# In[7]:


df_wrang.groupby(['str_col'])['float_col'].mean()


# find the covariance of float_col and int_col

# In[11]:


df[['float_col','in_col']].cov()

find the correlation of float_col and int_col
    r value	Strength
0.0 – 0.2	Weak correlation
0.3 – 0.6	Moderate correlation
0.7 – 1.0	Strong correlation
# In[15]:


df[['float_col','in_col']].corr()


# Create a data frame ‘other’ having columns some_val and str_col having values given belowsome_val str_col0         1       a1         2       b

# In[19]:


df_other = pd.DataFrame({
    'some_val':[1,2],
    'str_col':['a','b']    
})
df_other


# In[21]:


df


# Perform inner join, outer join, left join and right join with data frame df

# In[20]:


#inner join
df_other.merge(df,on='str_col',how='inner')


# In[22]:


#outer join
df_other.merge(df,on='str_col',how='outer')


# In[23]:


#left join
df_other.merge(df,on='str_col',how='left')


# In[26]:


#right join
df_other.merge(df,on='str_col',how='right')


# When we want to send the same invitations to many people, the body of the mail does not change. Only the name (and maybe address) needs to be changed.Mail  merge  is  a  process  of  doing  this.  Instead  of  writing  each  mail  separately, we              have  a  template  for  body  of  the  mail  and a  list  of  names  that  we  merge together to form all the mails.

# In[68]:


df_name = pd.read_csv('names.txt',sep='\n',header=-1)
df_body = pd.read_csv('body.txt',sep='\n',header=-1)
body = ''
for b in list(df_body[0]):
    body = body+b+'\n'
for x in list(df_name[0]):
    mail = 'Hello ' + str(x)+'\n'+body
    filename = x +'.txt'
    txt_file = open(filename,"w")
    txt_file.write(mail)
    txt_file.close()
         
        

