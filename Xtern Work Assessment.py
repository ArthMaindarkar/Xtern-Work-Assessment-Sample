#!/usr/bin/env python
# coding: utf-8

# In[133]:


import numpy as np
import pandas as pd

options = pd.read_csv('Downloads/XternData.csv')

import googlemaps
import requests

gmaps = googlemaps.Client(key='API_KEY') #I have not disclosed mine for security reasons

name = []
address = []
rating = []
classifier = []

for i in range(50): #Looks up different places to eat in Indianapolis 50 times and stores results
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="+ str(i) +"%20places%20to%20eat%20in%20Indianapolis&inputtype=textquery&fields=formatted_address%2Cname%2Crating&key=API_KEY"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    
    name.append(response.json()["candidates"][0]["name"])
    address.append(response.json()["candidates"][0]["formatted_address"])
    rating.append(response.json()["candidates"][0]["rating"])
    classifier.append("Food")

d = {'Name': name, 
     'Category': classifier,
     'Address': address,
     'Rating': rating}
df1 = pd.DataFrame(data=d) #Creates pandas dataframe with data

name = []
address = []
rating = []
category = []
for i in range(10): #Looks up 10 different fields and arenas and stores result
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + str(i) + "%20Fields%20Arenas%20stadiums%20Indianapolis&inputtype=textquery&fields=formatted_address%2Cname%2Crating&key=API_KEY"
    
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    
    names.append(response.json()["candidates"][0]["name"])
    address.append(response.json()["candidates"][0]["formatted_address"])
    rating.append(response.json()["candidates"][0]["rating"])
    category.append("Sport")

d = {'Name': names, 
     'Category': category,
     'Address': address,
     'Rating': rating}
df2 = pd.DataFrame(data=d)
df2 = df2.drop_duplicates(subset=None, keep='first', inplace=False) #removes duplicate entries
df1 = df1.append(df2)  #Gets added to existing data frame

names = []
address = []
rating = []
category = []
for i in range(1,5):  #Looks up 5 different Music places and stores result
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + str(i) + "%20Music%20Indianapolis&inputtype=textquery&fields=formatted_address%2Cname%2Crating&key=API_KEY"
    
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    
    names.append(response.json()["candidates"][0]["name"])
    address.append(response.json()["candidates"][0]["formatted_address"])
    rating.append(response.json()["candidates"][0]["rating"])
    category.append("Music")

d = {'Name': names, 
     'Category': category,
     'Address': address,
     'Rating': rating}
df2 = pd.DataFrame(data=d)
df2 = df2.drop_duplicates(subset=None, keep='first', inplace=False)
df1 = df1.append(df2)  #Gets added to existing data frame

names = []
address = []
rating = []
category = []
for i in range(5):  #Looks up 5 different game locations and stores result
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + str(i) + "%20Game%20Indianapolis&inputtype=textquery&fields=formatted_address%2Cname%2Crating&key=API_KEY"
    
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    
    names.append(response.json()["candidates"][0]["name"])
    address.append(response.json()["candidates"][0]["formatted_address"])
    rating.append(response.json()["candidates"][0]["rating"])
    category.append("Gaming")

d = {'Name': names, 
     'Category': category,
     'Address': address,
     'Rating': rating}
df2 = pd.DataFrame(data=d)
df2 = df2.drop_duplicates(subset=None, keep='first', inplace=False)
df1 = df1.append(df2)  #Gets added to existing data frame

df2 = df1.reset_index()
df2


# In[165]:


milesIUPUI = []
minIUPUI = []
for i in range(len(df2)):
    one = options.loc[0,'Address'].replace(" ", "%20").replace("#", "") #Formats each address for URL
    two = df2.loc[i,'Address'].replace(" ", "%20").replace("#", "")

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + one + "%2C%20DC&destinations=" + two + "%2C%20NY&units=imperial&key=API_KEY"

    payload= {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    a = float(response.json()['rows'][0]['elements'][0]['distance']['text'].split()[0]) #Gets distance in miles
    b = float(response.json()['rows'][0]['elements'][0]['duration']['text'].split()[0]) #Gets distance in minutes
    milesIUPUI.append(a)
    minIUPUI.append(b)
    


miles1 = []
min1 = []
for i in range(len(df2)):
    one = options.loc[1,'Address'].replace(" ", "%20").replace("#", "")
    two = df2.loc[i,'Address'].replace(" ", "%20").replace("#", "")

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + one + "%2C%20DC&destinations=" + two + "%2C%20NY&units=imperial&key=API_KEY"

    payload= {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    a = float(response.json()['rows'][0]['elements'][0]['distance']['text'].split()[0])
    b = float(response.json()['rows'][0]['elements'][0]['duration']['text'].split()[0])
    miles1.append(a)
    min1.append(b)
    


miles2 = []
min2 = []
for i in range(len(df2)):
    one = options.loc[2,'Address'].replace(" ", "%20").replace("#", "")
    two = df2.loc[i,'Address'].replace(" ", "%20").replace("#", "")

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + one + "%2C%20DC&destinations=" + two + "%2C%20NY&units=imperial&key=API_KEY"

    payload= {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    a = float(response.json()['rows'][0]['elements'][0]['distance']['text'].split()[0])
    b = float(response.json()['rows'][0]['elements'][0]['duration']['text'].split()[0])
    miles2.append(a)
    min2.append(b)


miles3 = []
min3 = []
for i in range(len(df2)):
    one = options.loc[3,'Address'].replace(" ", "%20").replace("#", "")
    two = df2.loc[i,'Address'].replace(" ", "%20").replace("#", "")

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + one + "%2C%20DC&destinations=" + two + "%2C%20NY&units=imperial&key=API_KEY"

    payload= {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    a = float(response.json()['rows'][0]['elements'][0]['distance']['text'].split()[0])
    b = float(response.json()['rows'][0]['elements'][0]['duration']['text'].split()[0])
    miles3.append(a)
    min3.append(b)


miles4 = []
min4 = []
for i in range(len(df2)):
    one = options.loc[4,'Address'].replace(" ", "%20").replace("#", "")
    two = df2.loc[i,'Address'].replace(" ", "%20").replace("#", "")

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + one + "%2C%20DC&destinations=" + two + "%2C%20NY&units=imperial&key=API_KEY"

    payload= {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    a = float(response.json()['rows'][0]['elements'][0]['distance']['text'].split()[0])
    b = float(response.json()['rows'][0]['elements'][0]['duration']['text'].split()[0])
    miles4.append(a)
    min4.append(b)


miles5 = []
min5 = []
for i in range(len(df2)):
    one = options.loc[5,'Address'].replace(" ", "%20").replace("#", "")
    two = df2.loc[i,'Address'].replace(" ", "%20").replace("#", "")

    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + one + "%2C%20DC&destinations=" + two + "%2C%20NY&units=imperial&key=API_KEY"

    payload= {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    a = float(response.json()['rows'][0]['elements'][0]['distance']['text'].split()[0])
    b = float(response.json()['rows'][0]['elements'][0]['duration']['text'].split()[0])
    miles5.append(a)
    min5.append(b)

            
d = {'Distance(Miles) from IUPUI': milesIUPUI,
     'Distance(Minutes) from IUPUI': minIUPUI,
     'Distance(Miles) from Speak Easy': miles1,
     'Distance(Minutes) from Speak Easy': min1,
     'Distance(Miles) from zWorks': miles2,
     'Distance(Minutes) from zWorks': min2,
     'Distance(Miles) from Launch Fishers': miles3,
     'Distance(Minutes) from Launch Fisher': min3,
     'Distance(Miles) from IMA': miles4,
     'Distance(Minutes) from IMA': min4,
     'Distance(Miles) from Launch Indy': miles5,
     'Distance(Minutes) from Launch Indy': min5}
df3 = pd.DataFrame(data=d) #Creates datafarme of all the distaces

df5 = pd.concat([df2, df3], axis=1) #Adds new data to existing location dataframe
df5.to_csv('Locations of Interest and Distance from Housing and Coworking Spaces', sep='\t')


# In[36]:


import matplotlib.pyplot as plt

df4 = df3.drop(labels=[22], axis=0) #Drops outlier (spurious google result)

plt.barh(df4.columns.values.tolist(), df4.mean(), color = ['black', 'black', 'yellow', 'yellow', 'blue', 'blue', 'green', 'green', 'pink', 'pink', 'red', 'red'],
        alpha = 0.6, edgecolor = ['white', 'black']) #Creates bar graph of means for each coworking location

plt.show()

plt.savefig('Distances Visualized.png')


# In[144]:





# In[63]:





# In[75]:





# In[90]:





# In[92]:





# In[180]:





# In[183]:





# In[185]:





# In[184]:





# In[188]:





# In[231]:





# In[ ]:




