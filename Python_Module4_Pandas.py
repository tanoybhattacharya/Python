
# coding: utf-8

# In[28]:


import numpy as np
import pandas as pd

ds_df= pd.read_csv('DSScoreTerm1.csv')
ds_math =pd.read_csv('MathScoreTerm1.csv')
ds_phy = pd.read_csv('PhysicsScoreTerm1.csv')
ds_df = ds_df.append(ds_math)
ds_df = ds_df.append(ds_phy)
ds_df = ds_df.drop(columns=['Name','Ethinicity'])
ds_df['Sex'].replace(['M'],1,inplace=True)
ds_df['Sex'].replace(['F'],2,inplace=True)


ds_df['Score'].replace(0.0, np.nan, inplace= True)
ds_df.to_csv('ScoreFinal.csv',sep=',', encoding='utf-8')

