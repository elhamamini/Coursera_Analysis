#!/usr/bin/env python
# coding: utf-8

# In[230]:


import pandas as pd
import json
from pandas import json_normalize
from sklearn.preprocessing import LabelEncoder
from ua_parser import user_agent_parser
from user_agents import parse


# In[162]:


df = pd.read_csv('psy-001_clickstream_export_snippet.txt', sep="|",header=None)
df


# In[191]:


result = df.to_json(orient="split")


# In[123]:


parsed = json.loads(result)

List_of_lists=parsed["data"]


# In[139]:


list_of_dict=[]
for line in List_of_lists:
    obj={}
    for row in line:
         command, description = row.strip().split(":",1)
         
         if command=="{key":
                command="key"
      
         obj[command]=description 
        
   
    list_of_dict.append(obj)
               


# In[136]:


json.dumps(list_of_dict, indent=4) 


# In[150]:


with open("my_data.json", "w") as final:
    json.dump(list_of_dict, final)
  


 


# In[231]:


Coursera_df = pd.read_json("my_data.json")
Coursera_df


# # Most viewed videos

# In[232]:


Coursera_df.groupby(["page_url"]).size().sort_values(ascending=False).head(6)


# # Users most used language

# In[233]:


Coursera_df.groupby(["language"]).size().sort_values(ascending=False)


# # List of most active users

# In[234]:


Coursera_df.groupby(["username"]).size().sort_values(ascending=False).head(6)


# # Most Used Internet Browser

# In[235]:


Coursera_df["browser"]=Coursera_df["user_agent"].apply(lambda ua: user_agent_parser.Parse(ua))


# In[236]:


Coursera_df["browser"]=Coursera_df["browser"].apply(lambda x: x["user_agent"]["family"])


# In[237]:


Coursera_df.groupby(["browser"]).size()

