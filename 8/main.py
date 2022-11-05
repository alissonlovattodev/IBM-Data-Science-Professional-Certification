# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:29:34 2022

@author: Alisson Lovatto
"""

import numpy as np  
import pandas as pd
import json
df_dataScience=pd.read_csv('Topic_Survey_Assignment.csv', index_col=0)
print(df_dataScience.head(6))

print('-------------------')

df_dataScience = pd.read_csv("Topic_Survey_Assignment.csv")

df_dataScience.rename(columns={'Unnamed: 0':'Topic'}, inplace=True )
df_dataScience.set_index('Topic', inplace = True)

#Sort the dataframe in descending order of Very interested
df_dataScience.sort_values(['Very interested'], ascending = False, axis = 0, inplace = True)

#converting the dataframe into percentages 
df_dataScience = df_dataScience.divide(2233)
df_dataScience = df_dataScience.multiply(100)
df_dataScience = df_dataScience.round(2)
print(df_dataScience.head())

print('-------------------')


%matplotlib inline

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use('ggplot')

color_list = ['#5cb85c', '#5bc0de', '#d9534f']

ax = df_dataScience.plot.bar(figsize = (20, 8), alpha = 0.8, width = 0.8, color = color_list)
ax.set_title("Percentage of Respondents' Interest in Data Science Areas", fontsize = 16)

legend = ax.legend(fontsize='14')
ax.tick_params(axis='x', labelsize=14)
ax.set_xlabel('')

#Putting the percentage values on top of each bar
for p in ax.patches:
    ax.annotate(str(p.get_height()) + '%', (p.get_x() * 1.005, p.get_height() * 1.005), fontsize = 14)
    
ax.set_facecolor('xkcd:white')
plt.tick_params(top=False, bottom=False, left=False, right=False, labelleft=False, labelbottom=True)

print('---------')


df_initial = pd.read_csv("Police_Department_Incidents_-_Previous_Year__2016_.csv")

#print(df_initial.head(10))
df_PdDistrict = df_initial[['PdDistrict', 'X']]
df_sfcrime = df_PdDistrict.groupby(['PdDistrict']).count()
df_sfcrime = df_sfcrime.reset_index()
df_sfcrime.columns = ['Neighborhood', 'Count']
df_sfcrime.head(10)


#!conda install -c conda-forge folium
#!pip install folium
import folium
from IPython.display import display

sf_geo = pd.read_json('D:\Github\-IBM-Data-Science-Professional-Certification\8\san-francisco.geojson')
sf_map = folium.Map(location = [37.76, -122.45], zoom_start = 12)
sf_map.choropleth(
    geo_data = sf_geo, 
    data = df_sfcrime, 
    columns = ['Neighborhood', 'Count'], 
    key_on='feature.properties.DISTRICT', 
    fill_color = 'YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2, 
    legend_name='Crime Rate in San Francisco'
)

sf_map

