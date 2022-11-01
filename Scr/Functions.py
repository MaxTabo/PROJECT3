
import pandas as pd

import json

import numpy as np
import os
#______________Cleaning______________

def clean_df():
    data= pd.read_json ('Labjson.csv')
    def dropcolumn(df,column):
        df.drop(f"{column}", axis = 1, inplace = True)
    
        return df
    columns=['permalink', 'crunchbase_url', 'homepage_url',
       'blog_url', 'blog_feed_url', 'twitter_username',
        'founded_year', 'founded_month', 'founded_day',
       'deadpooled_year', 'deadpooled_month', 'deadpooled_day',
       'deadpooled_url', 'tag_list', 'email_address', 'phone_number',
       'created_at', 'updated_at', 'image',
        'relationships', 'providerships', 'funding_rounds',
       'video_embeds', 'screenshots', 'external_links', 'partners', 'ipo','competitions','overview','_id','products']
    for i in columns:
        dropcolumn(data,i)
    data['description'] = data['description'].str.upper()
    data['description'] = data['description'].str.extract('(.*GAM.*)')
    data=data.dropna(subset=['description'])
    data=data.dropna(subset=['total_money_raised'])
    data=data.explode('offices')
    Test=data['offices'].apply(pd.Series)
    dropcolumn(Test,'description')
    Test1=pd.concat([data, Test], axis=1)
    Test1=Test1.dropna(subset=['latitude'])

    Test1=Test1.dropna(subset=['longitude'])

    Test1=Test1.dropna(subset=['number_of_employees'])

    Test1=Test1.dropna(subset=['city'])


    Test1.reset_index(drop=True, inplace=True)
    T=Test1.sort_values(by=["city"]) 
    T['city'] = T['city'].str.strip()
    T['city'] = T['city'].astype(str)
    SF=T[T["city"] =='San Francisco']
    SF.reset_index(drop=True, inplace=True)
    SF['total_money_raised'] = SF['total_money_raised'].str.extract('(.*M|B)')
    SF=SF.dropna(subset=['total_money_raised'])
    return SF



#______________Creating a dictionary______________

def get_dist_category(latitude,longitude,category):

    url = f"https://api.foursquare.com/v3/places/search?ll={latitude}%2C{longitude}&categories={category}"

    headers = {
        "accept": "application/json",
        "Authorization":token_fsq}
    response = requests.get(url, headers=headers).json()
    newlist=[]
    for lista in response["results"]:
        distance = lista["distance"]
        newlist.append(distance)

    return newlist

def get_dist_query(latitude,longitude,query):

    url = f"https://api.foursquare.com/v3/places/nearby?ll={latitude}%2C{longitude}&query={query}"

    headers = {
        "accept": "application/json",
        "Authorization": token_fsq}
    response = requests.get(url, headers=headers).json()
    newlist=[]
    for lista in response["results"]:
        distance = lista["distance"]
        newlist.append(distance)

    return newlist
#______________Scoring______________

def Score(dist_list):
    Scoring=0
    for i in dist_list:
        if i<100:
            Scoring+=50
        elif 100<i<200:
            Scoring+=30
        elif 200<i<300:
            Scoring+=20
        elif 300<i<600:
            Scoring+=10
        
    return Scoring    

#______________Creating a dictionary______________


keys = ['Exent', 'Serious Business', 'Kongregate','Curse']
values = [3250, 2980, 2190,2100]

def create_dictionary(keys, values):
    result = {} 
    for key, value in zip(keys, values):
        result[key] = value
    return result
