
# coding: utf-8

# In[ ]:


GoodsKart—largest ecommerce company of Indonesia with revenue of $2B+ acquired another ecommerce company FairDeal.  FairDeal has its own IT system to maintain records of customer, sales etc.For ease of maintenance and cost savings GoodsKart is integrating customer databases of both the organizations hence customer data of FairDeal has to be converted in GoodsKartCustomer Format.


# In[1]:


import pandas as pd


# In[65]:


df = pd.read_csv('FairDealCustomerData.csv',header=None)
df[1] = df[1]+df[0]
del df[0]
#str.strip() is similar to trim
fairCustList = list(df[df[2]==0][1].str.strip())
blockcustlist= list(df[df[2]==1][1].str.strip())
fairCustList

class customer:
    customers = []
    def __init__(self,custlst):
        self.customers = custlst
    def __del__(self):
        self.customers =[]
    def IsFair(self,name):
        if name in self.customers:
            print('{0} is a fair customer'.format(name))
        else:
            raise Exception


try:
    fr = customer(fairCustList)
    fr.IsFair(input('Enter Customer Name for an Order:'))
#     print(fr.customers)

except:
    print('Sorry!!Input Customer is a blacklisted.')


# In[ ]:


Miss. Laina  Heikkinen

