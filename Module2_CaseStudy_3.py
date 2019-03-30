
# coding: utf-8

# 1.Read the input from command line –Reference ID
# 2.Check for validity –it should be 12 digits and allows on number andalphabet
# 3.Encrypt the Reference ID and print it for reference

# In[1]:


from cryptography.fernet import Fernet
import re
p = input("Enter a ReferenceID:")
cipher_text = plain_text = ""
nf = open("KeyFile.txt","wb+")
key = Fernet.generate_key()
cipher_suite = Fernet(key)

x = True
while x:
    if len(p) != 12:
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    else:
        print("Valid Reference ID")
        cipher_text = cipher_suite.encrypt(p.encode())
        nf.write(cipher_text)
        nf.close()
        print(cipher_text)
        x= False
if x:
    print("Invalid Password")
else:
    rf = open("KeyFile.txt","rb")
    print(cipher_suite.decrypt(rf.read()))
    rf.close()
    

