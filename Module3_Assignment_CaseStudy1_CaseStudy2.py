
# coding: utf-8

# A Robot moves in a Plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT, RIGHT.

# In[3]:


import math
stpoint = {"x":0,"y":0}

while True:
    line = input(">")
    if not line:
        break

    direction, step = line.split()
    if direction == "UP":
        stpoint["y"]+=int(step)
    if direction == "DOWN":
        stpoint["y"]-=int(step)
    if direction == "LEFT":
        stpoint["x"]-=int(step)
    if direction == "RIGHT":
        stpoint["x"]+=int(step)

print (int(round((stpoint["x"]**2+stpoint["y"]**2))**0.5))


# Weather forecasting organization wants to show is it day or night. So, write a program for such organization to findwhether is it dark outside or not.

# In[9]:


from datetime import datetime
def daynight(hour):
    s=""
    if hour >=5 and hour<=11:
        s= "morning and outside is day"
    elif hour >=12 and hour<=17:
        s = "afternoon and outside is day"
    elif hour >=18 and hour<=22:
        s = "evening and outside is night"
    else:
        s="night and outside is night"
    return s


h = datetime.now().hour
print('Have a good {0}!\n'.format(daynight(h)))


# Write a program to find distancebetween two locations when their latitude and longitudes are given.

# In[10]:


from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

lat1 = radians(56.2296756)
lon1 = radians(45.0122287)
lat2 = radians(52.406374)
lon2 = radians(16.9251681)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", round(distance) ,"KM")


# Design a software for bank system. There should be options like cash withdraw, cash credit and change password. According to user input, the software should provide required output.

# In[3]:


class BankAccount:
    def __init__(self,amt,name,pwd):
        self.amount = amt
        self.name = name
        self.pwd = pwd
        print("Account Opening Successfully!! Please Start the transaction!!")
    def Cash(self,x):
        if x < self.amount:
            self.amount-=x
            print("Account Balance :", self.amount)
        else:
            print("Insufficient Amount, Please deposite some money")
    def deposit(self,y):
        self.amount+=y
        print ("Account Balance:",self.amount)
    def changepwd(self,nwpwd):
        self.pwd= nwpwd
        print("Password Change Successfully\nNew password is:",self.pwd)
    def checkbalance(self):
        print("Mr. {0}, your account balance is:{1}".format(self.name,self.amount))
    def __del__(self):
        self.amount = 0
        self.name = ""
        self.pwd = ""
        print("Account Closed!!\n")

print("Open Your Bank Account!!\n")
nm = input("Enter your full name:")
pw = input("Please provide accout password:")
ob = input("Please enter opening balance:")

bk = BankAccount(int(ob),nm,pw)

while True:
    print("1. Check Balance\n2. Deposit\n3.Cash Withdraw\n4. Change Password\n5. Close Account\n6.Exist")
    p = input("Please Select an option as number:")
    n = int(p)
    if n==1:
        bk.checkbalance()
    elif n==2:
        x = input("Amount:")
        bk.deposit(int(x))
    elif n==3:
        x= input("Amount:")
        bk.Cash(int(x))
    elif n==4:
        x = input("New Password:")
        bk.changepwd(x)
    elif n==5:
        del bk
        break
    elif n==6:
        print ("Thanks For Using ATM!! Bye")
        break
    


# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[5]:


lst = [x for x in range(2000,3200) if x%7 == 0 and x%5!=0]
print(lst)


# Write a program which can compute the factorial of a given numbers. Use recursion to find it.

# In[6]:


def fact(n,res=1):
    while True:
        res = res*n
        n-=1
        if(n!=1):
            fact(n)
        else:
            return res
num =input("Enter a Number:")
print("Factorial {0} is {1}".format(num,fact(n=int(num))))


# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

# In[7]:


row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
print(multi_list)


# ccepts a comma separated sequence of words as input and  sorting them alphabetically

# In[8]:


line = input('Enter Words:')
print(sorted(line.split(',')))


# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized

# In[9]:


line = input('Enter string')
print(line.upper())


# Write  a  program  that  accepts  a  sentence  and  calculate  the  number  of  upper  case letters and lower case letters

# In[10]:


def Letter_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

Letter_test(input("Enter String:"))


# Banking Marketing - Loan Approval Process

# In[2]:


import pandas as pd
import numpy as np


df = pd.read_csv('bank-data.csv')
profs = list(df['job'].unique())

prof = input("Enter a profession:")
if prof in profs:
    print("{0} is entitle profession".format(prof))
else:
    print("{0} is not entitle profession".format(prof))

