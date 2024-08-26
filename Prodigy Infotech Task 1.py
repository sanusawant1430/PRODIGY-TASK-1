#!/usr/bin/env python
# coding: utf-8

# # Task 1
# 
# <i>Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population.

# ## Importing necessary libraries

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ## Reading the dataset

# In[3]:


df = pd.read_csv(r"worldpopulationdata.csv")


# ## Checking the first 10 rows

# In[4]:


df.head(10)


# ## Checking the last 10 rows

# In[5]:


df.tail(10)


# ## Checking the shape of the dataset

# In[6]:


df.shape


# ## Checking the columns of the dataset

# In[7]:


df.columns


# ## Some information about the dataset

# In[8]:


df.info()


# In[9]:


df.describe()


# ## Checking for duplicate rows 

# In[15]:


df.duplicated().sum()


# `Observation:`
# - There are no duplicate rows in the dataset

# ## Checking for missing values

# In[16]:


df.isna().sum()


# `Observation:`
# - no missing values present

# ## Checking unique values for columns

# In[17]:


print(df['Country Name'].unique())
print("\nTotal no of unique countries:",df['Country Name'].nunique())


# In[18]:


print(df['Country Code'].unique())
print("\nTotal no of unique country code:",df['Country Code'].nunique())


# In[19]:


df['Series Name'].unique()


# In[123]:


df['Series Code'].unique()


# ## Dropping unnecessary columns

# In[20]:


df.drop(['Series Name','Country Code'],axis=1,inplace=True)


# In[21]:


df.columns


# ## Extraction of top-05 countries with respect to total population

# In[101]:


# Filter data for total population
total_population_data = df[df['Series Code'] == 'SP.POP.TOTL']

# Sort data based on the total population for 2022
total_population_sorted = total_population_data.sort_values(by="2022", ascending=True)

# Get the top ten countries with the highest total population for 2022
total_top_five_countries = total_population_sorted.head(5)
print("Top five countries of total population\n")
print(total_top_five_countries[['Country Name']] )


# # Bar Plot
# 
# ## Top ten countries of total population in year 2022 and 2016

# In[85]:


# Create the bar plot
plt.figure(figsize=(15, 6))
plt.subplot(2,2,1)
sns.barplot(x="2022", y="Country Name", data=total_top_ten_countries, palette="bright")
plt.title("Top Ten Countries of Total Population (2022)",fontsize=10)
plt.xlabel("Total Population",fontsize=10)
plt.ylabel("Country",fontsize=10)
plt.show()

plt.figure(figsize=(15, 6))
plt.subplot(2,2,2)
sns.barplot(x="2016", y="Country Name", data=total_top_ten_countries, palette="coolwarm")
plt.title("Top Ten Countries with Total Population (2016)",fontsize=10)
plt.xlabel("Total Population",fontsize=10)
plt.ylabel("Country",fontsize=10)
plt.show()



# ## Top ten countries of total population in year 2010 and 2001

# In[113]:


# Create the bar plot
plt.figure(figsize=(15, 6))
plt.subplot(2,2,1)
sns.barplot(x="2010", y="Country Name", data=total_top_ten_countries, palette="coolwarm")
plt.title("Top Ten Countries of Total Population (2010)",fontsize=10)
plt.xlabel("Total Population",fontsize=10)
plt.ylabel("Country",fontsize=10)
plt.show()

plt.figure(figsize=(15, 6))
plt.subplot(2,2,2)
sns.barplot(x="2001", y="Country Name", data=total_top_ten_countries, palette="coolwarm")
plt.title("Top Ten Countries with Total Population (2001)",fontsize=10)
plt.xlabel("Total Population",fontsize=10)
plt.ylabel("Country",fontsize=10)
plt.show()


# ## Extraction of bottom-10 countries with respect to total population

# In[108]:


# Sort data based on the total population for 2022
total_population_sorted1 = total_population_data.sort_values(by="2022", ascending=True)

# Get the bottom ten countries with the highest total population for 2022
total_bottom_ten_countries = total_population_sorted1.head(10)
print("Bottom ten countries of total population\n")
print(total_bottom_ten_countries[['Country Name']] )


# ## Bottom ten countries of total population in year 2022 and 2016

# In[80]:


# Create the bar plot
plt.figure(figsize=(15, 6))
plt.subplot(2,2,1)
sns.barplot(x="2022", y="Country Name", data=total_bottom_ten_countries, palette="pastel")
plt.title("Top Ten Countries of Total Population (2022)",fontsize=10)
plt.xlabel("Total Population",fontsize=10)
plt.ylabel("Country",fontsize=10)
plt.show()

plt.figure(figsize=(15, 6))
plt.subplot(2,2,2)
sns.barplot(x="2016", y="Country Name", data=total_bottom_ten_countries, palette="coolwarm")
plt.title("Top Ten Countries with Total Population (2016)",fontsize=10)
plt.xlabel("Total Population",fontsize=10)
plt.ylabel("Country",fontsize=10)
plt.show()



# ## Bottom ten countries of total population in year 2010 and 2001

# In[78]:


# Create the bar plot
plt.figure(figsize=(15, 6))
plt.subplot(2,2,1)
sns.barplot(x="2010", y="Country Name", data=total_bottom_ten_countries, palette="deep")
plt.title("Top Ten Countries of Total Population (2010)",fontsize=10)
plt.xlabel("Total Population",fontsize=10)
plt.ylabel("Country",fontsize=10)
plt.show()

plt.figure(figsize=(15, 6))
plt.subplot(2,2,2)
sns.barplot(x="2001", y="Country Name", data=total_bottom_ten_countries, palette="pastel")
plt.title("Top Ten Countries with Total Population (2001)",fontsize=10)
plt.xlabel("Total Population",fontsize=10)
plt.ylabel("Country",fontsize=10)
plt.show()


#  ## Extraction of top ten countries with highest male population

# In[30]:


# Filter data for male population
male_population_data = df[df["Series Code"] == "SP.POP.TOTL.MA.IN"]

# Sort data based on the male population for 2022
male_population_sorted = male_population_data.sort_values(by="2022", ascending=False)

# Get the top ten countries with the highest male population for 2022
male_top_ten_countries = male_population_sorted.head(10)
print("Top ten countries of male population")
print(male_top_ten_countries[['Country Name']] )


# ## Extraction of top ten countries with highest female population

# In[31]:


# Filter data for female population
female_population_data = df[df["Series Code"] == "SP.POP.TOTL.FE.IN"]

# Sort data based on the female population for 2022
female_population_sorted = female_population_data.sort_values(by="2022", ascending=False)

# Get the top ten countries with the highest female population for 2022
female_top_ten_countries = female_population_sorted.head(10)
print("Top ten countries of female population")
print(female_top_ten_countries[['Country Name']] )


# ## Top ten countries with highest male and female population in 2022

# In[76]:


# Create the bar plot
plt.figure(figsize=(15, 6))
plt.subplot(2,2,1)
sns.barplot(x="2022", y="Country Name", data=male_top_ten_countries, palette="colorblind")
plt.title("Top Ten Countries with Highest Male Population (2022)",size=10)
plt.xlabel("Male Population",size=10)
plt.ylabel("Country",size=10)
plt.show()

plt.figure(figsize=(15, 6))
plt.subplot(2,2,2)
sns.barplot(x="2022", y="Country Name", data=female_top_ten_countries, palette="bright")
plt.title("Top Ten Countries with Highest Female Population (2022)",size=10)
plt.xlabel("Female Population",size=10)
plt.ylabel("Country",size=10)
plt.show()


# ## Extraction of top ten countries with lowest male population

# In[33]:


male_lowest_ten_countries = male_population_sorted.tail(10)
print("Top ten countries of lowest male population")
print(male_lowest_ten_countries[['Country Name']] )


# ## Extraction of top ten countries with lowest female population

# In[34]:


female_lowest_ten_countries = female_population_sorted.tail(10)
print("Top ten countries of lowest female population")
print(female_lowest_ten_countries[['Country Name']] )


# ## Top ten countries with lowest male and female population in 2022

# In[72]:


# Create the bar plot
plt.figure(figsize=(15, 6))
plt.subplot(2,2,1)
sns.barplot(x="2022", y="Country Name", data=male_lowest_ten_countries, palette="colorblind")
plt.title("Top Ten Countries with Lowest Male Population (2022)",size=10)
plt.xlabel("Male Population",size=10)
plt.ylabel("Country",size=10)
plt.show()

plt.figure(figsize=(15, 6))
plt.subplot(2,2,2)
sns.barplot(x="2022", y="Country Name", data=female_lowest_ten_countries, palette="dark")
plt.title("Top Ten Countries with Lowest Female Population (2022)",size=10)
plt.xlabel("Female Population",size=10)
plt.ylabel("Country",size=10)
plt.show()


# # Stacked Bar Plot
# 
# ## Top 10 Countries with Male and Female Populations (2022)

# In[36]:


# Merge male and female population data on 'Country Name'
merged_data = pd.merge(male_population_data, female_population_data, on="Country Name", suffixes=("_male", "_female"))


# In[172]:


merged_data


# In[37]:


# Calculate the total population for each country (male + female)
merged_data["Total Population"] = merged_data["2022_male"] + merged_data["2022_female"]


# In[174]:


merged_data.head()


# In[38]:


# Sort data based on total population in descending order
sorted_data = merged_data.sort_values(by="Total Population", ascending=False)

# Select the top 10 countries with the highest total population
top_10_countries = sorted_data.head(10)


# In[125]:


# Create the stacked bar plot
plt.figure(figsize=(15, 5))

sns.barplot(x="Country Name", y="2022_female", data=top_10_countries, color="lightblue", label="Female Population")
sns.barplot(x="Country Name", y="2022_male", data=top_10_countries, bottom=top_10_countries["2022_female"], color="darkblue", label="Male Population")
plt.title("Top 10 Countries with Male and Female Populations (2022)")
plt.xlabel("Country")
plt.ylabel("Population")
plt.legend()
plt.xticks(rotation=45, ha="right")
plt.show()


# ## Bottom 10 Countries with Male and Female Populations (2022)

# In[40]:


# Select the top 10 countries with the highest total population
bottom_10_countries = sorted_data.tail(10)


# In[124]:


# Create the stacked bar plot
plt.figure(figsize=(15, 5))

sns.barplot(x="Country Name", y="2022_female", data=bottom_10_countries, color="lightblue", label="Female Population")
sns.barplot(x="Country Name", y="2022_male", data=bottom_10_countries, bottom=bottom_10_countries["2022_female"], color="darkblue", label="Male Population")
plt.title("Bottom 10 Countries with Male and Female Populations (2022)")
plt.xlabel("Country")
plt.ylabel("Population")
plt.legend()
plt.xticks(rotation=50, ha="right")
plt.show()


# In[ ]:




