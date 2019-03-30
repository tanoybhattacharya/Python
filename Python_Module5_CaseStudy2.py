
# coding: utf-8

# Plot Total Sales Per Month for Year 2011.  How the total sales haveincreased over months in Year 2011. Which month has lowest Sales?

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('BigMartSalesData.csv')

df_2011=df[df['Year']==2011]
rep_plot=df_2011.groupby(['Month'])['Amount'].sum().sort_values(ascending=True).plot(kind='bar')

rep_plot.set_xlabel("Month")
rep_plot.set_ylabel("Total Sales")


# Plot Total Sales Per Month for Year 2011 as Bar Chart.  Is Bar Chart Better to visualize than Simple Plot?

# In[23]:


read_plot = df_2011.groupby(['Month'])['Amount'].sum().plot()
read_plot.set_xlabel('Month')
read_plot.set_ylabel('Total Sales')


# Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest towards sales

# In[3]:


pd.options.display.float_format = '{:,.2f}'.format
dfc = df_2011.groupby(['Country'])['Amount'].sum().plot(kind='bar')


# In[6]:


plt.scatter(df.Amount,df.Amount)
plt.show()

