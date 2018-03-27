
# coding: utf-8

# In[ ]:


text = input("Please type anything:\n")

counter = dict() #创造一个字典 or counter = {}

for bababa in text :
    #两个条件，看是否出现过，用if
   
    if bababa in counter :
        counter[bababa] += 1
    
    else :
        counter[bababa] = 1
        
for bababa, count in counter.items():
    print("'" , bababa , "'" , " : " , count)

