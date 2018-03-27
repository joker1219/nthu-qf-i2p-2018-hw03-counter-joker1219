
# coding: utf-8

# In[ ]:


text = input("Please type anything:\n")

for bababa in set(text):
    print("'" , bababa , "'" , " : " , text.count(bababa))

