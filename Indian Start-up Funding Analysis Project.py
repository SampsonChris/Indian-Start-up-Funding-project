#!/usr/bin/env python
# coding: utf-8

# # INDIAN START UP FUNDING PROJECT LP1
# 
# ### The goal of this project is to analyze the funding received by startups in India from 2018 to 2021. The data for each year of funding is found in separate csv files. These files are what I’m going to use in asking my questions, stating my hypothesis, cleaning my data and analyzing my data.
# 
# 
# ### QUESTIONS
# ### 1. Who are the top funded start-ups in India?
# ### 2. Which cities are most favoured by investors?
# ### 3. How does the funding change in time?
# ### 4. Which year records the most start-ups funded?
# ### 5. Which sectors do investors prefer?
# 
# 
# ### HYPOTHESIS
# ### 1. Investors prefer to invest in Tech start-ups more than the other start ups
# ### 2. The location of a start-up is a major factor in receiving funds from Investors.
# 

# # Importing Libraries

# In[1]:


# Importing and installing libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
get_ipython().system('pip install seaborn ')
import seaborn as sns
get_ipython().system('pip install plotly==4.14.3')
import plotly.graph_objects as go
import warnings


# In[2]:


# Importing Datasets 
Data_2018 = pd.read_excel("/Users/Admin/Desktop/India Startup Funding/startup_funding2018.xls")
Data_2019 = pd.read_csv("/Users/Admin/Desktop/India Startup Funding/startup_funding2019.csv")
Data_2020 = pd.read_csv("/Users/Admin/Desktop/India Startup Funding/startup_funding2020.csv")
Data_2021 = pd.read_csv("/Users/Admin/Desktop/India Startup Funding/startup_funding2021.csv")


# ### Since I will be merging datasets at the end of the cleaning process, I have decided to add a new column called "Funding Year" to all datasets, to distinguish data after merging.

# In[3]:


# Adding a new column called Funding Year to all datasets
Data_2018["Funding Year"] = 2018
Data_2019["Funding Year"] = 2019
Data_2020["Funding Year"] = 2020
Data_2021["Funding Year"] = 2021


# # Loading and Cleaning Datasets individually before merging

# In[4]:


# Previewing 2018 dataset 
Data_2018.head()


# In[5]:


# Printing a concise summary of the 2018 dataset
Data_2018.info()


# ### Upon observation, the 2018 dataset has different column names from the rest of the datasets. Since I will be merging the data in the end, there must be uniformity in column names. Hence I am going to rename the column names in the 2018 dataset to suit that of the others.
# 

# In[6]:


# Renaming columns in 2018 data set 
Data_2018.rename(columns = {"Company Name": "Company/Brand", "Industry": "Sector", "Round/Series": "Stage", "Amount": "Amount($)", "Location": "HeadQuarter", "About Company": "What it does"}, inplace = True)
Data_2018.head()


# In[7]:


#Next step is to drop columns that are irrelevant to answering my research questions.
# Dropping columns
Data_2018.drop(columns = ["Calculation", "Amount.1", "What it does", "Stage"], inplace = True)
Data_2018.head()


# In[8]:


#Renaming Column name Amount($) to Amount in USD 
Data_2018.rename(columns = {"Amount($)": "Amount in USD"}, inplace = True)


# ### Looking at the 2018 dataset above, the amount column has a datatype in the form of a string. The amount column is supposed to be in an Int or Float datatype, so I went ahead to change the datatype from object to int.

# In[9]:


# Changing amount datatype to int/float 
Data_2018["Amount in USD"] = pd.to_numeric(Data_2018["Amount in USD"], errors = "coerce").fillna(0, downcast = "infer")
Data_2018.info()


# In[10]:


# Checking for any other errors in the 2018 data set 
Data_2018.isnull().sum()


# ### The Sector and Headquarter columns in the 2018 dataset has multiple sector names. I am going to strip off the commas and select just the first names of Sectors and Headquarters, to make my analysis and visualization clean and concise.

# In[11]:


# Stripping data to separate the values in the column by commas and select the first value only
Data_2018['Sector'] = Data_2018['Sector'].str.split(',').str[0] 
Data_2018['HeadQuarter'] = Data_2018['HeadQuarter'].str.split(',').str[0]
Data_2018


# In[12]:


# Replacing '-' values in the sector and headquarter columns with 'unknown'
Data_2018["HeadQuarter"].replace('-', value = "unknown", inplace = True)
Data_2018["Sector"].replace('-', value = "unknown", inplace = True)
Data_2018


# # Cleaned 2018 Dataset

# In[14]:


Data_2018


# # Loading and Cleaning 2019 Dataset

# In[15]:


# Previewing 2019 dataset to view 
Data_2019.head()


# In[16]:


# Printing a summary of the dataset to find errors and missing values. 
Data_2019.info()


# In[17]:


# Dropping Founders, Stage and What it does columns.
Data_2019.drop(columns = ["Founders", "Stage", "What it does"], inplace = True)
Data_2019.head()


# In[18]:


#Renaming Column name Amount($) to Amount in USD 
Data_2019.rename(columns = {"Amount($)": "Amount in USD"}, inplace = True)


# In[19]:


# Removing dollar sign from the Amount in USD column 
Data_2019["Amount in USD"] = Data_2019["Amount in USD"].replace({"\$": "", ",": ""}, regex = True)


# In[20]:


# Changing amount datatype to int/float 
Data_2019["Amount in USD"] = pd.to_numeric(Data_2019["Amount in USD"], errors = "coerce").fillna(0, downcast = "infer")


# In[21]:


# Changing undisclosed values in 'Amount in USD' to 0
Updated = Data_2019["Amount in USD"] == "Undisclosed"
Data_2019.loc[Updated, "Amount in USD"] = 0
Data_2019


# In[22]:


# Replacing null values in columns with unknown
Data_2019["Founded"].replace(np.NaN, value = "unknown", inplace = True)
Data_2019["HeadQuarter"].replace(np.NaN, value = "unknown", inplace = True)
Data_2019["Sector"].replace(np.NaN, value = "unknown", inplace = True)


# In[23]:


#Changing datatype for Founded Column from object to int
Data_2019['Founded']= Data_2019['Founded'].astype('str')


# In[24]:


# Checking for null values in 2019 Dataset.
Data_2019.isnull().sum()


# # Cleaned 2019 Dataset

# In[25]:


Data_2019


# # Loading and Cleaning 2020 Dataset
# 

# In[26]:


# Previewing 2020 dataset
Data_2020.head()


# In[27]:


# Printing a concise summary of 2020 Dataset. 
Data_2020.info()


# In[28]:


# Dropping Columns Founders, Stage, What it does and Unnamed: 9
Data_2020.drop(columns = ["Founders", "Stage", "What it does", "Unnamed: 9"], inplace = True)


# In[29]:


# Viewing the columns and rows of the 2020 dataset. 
Data_2020.head()


# In[30]:


#Renaming Column name Amount($) to Amount in USD 
Data_2020.rename(columns = {"Amount($)": "Amount in USD"}, inplace = True)


# In[31]:


# Removing dollar and comma signs from the Amount in USD column 
Data_2020["Amount in USD"] = Data_2020["Amount in USD"].replace({"\$": "", ",": ""}, regex = True)


# In[32]:


# Changing Amount in USD datatype to int/float 
Data_2020["Amount in USD"] = pd.to_numeric(Data_2020["Amount in USD"], errors = "coerce").fillna(0, downcast = "infer")


# In[33]:


# Changing undisclosed values in 'Amount in USD' column to 0
Updated = Data_2020["Amount in USD"] == "Undisclosed"
Data_2020.loc[Updated, "Amount in USD"] = 0
Data_2020


# In[34]:


# Viewing missing data in 2020 Data set
Data_2020.isnull().sum()


# ### I am going to replace all null values in the Founded, Sector and Investor columns with unknown. I did not go the extra mile to look for missing values because its a bit irrelevant to my questions.

# In[35]:


Data_2020["Founded"].replace(np.NaN, value = "unknown", inplace = True)
Data_2020["HeadQuarter"].replace(np.NaN, value = "unknown", inplace = True)
Data_2020["Sector"].replace(np.NaN, value = "unknown", inplace = True)
Data_2020["Investor"].replace(np.NaN, value = "unknown", inplace = True)


# In[36]:


# Checking for null values in dataset. 
Data_2020.isnull().sum()


# # Cleaned 2020 Dataset

# In[37]:


Data_2020


# # Loading and Cleaning 2021 dataset
# 

# In[38]:


# Loading and cleaning 2021 Data set 
Data_2021.head()


# In[39]:


Data_2021.info()


# In[40]:


# Dropping the Stage, Founders and What it does column
Data_2021.drop(columns = ["Founders", "Stage", "What it does"], inplace = True)


# In[41]:


#Renaming Column name Amount($) to Amount in USD 
Data_2021.rename(columns = {"Amount($)": "Amount in USD"}, inplace = True)


# In[42]:


# Removing dollar sign from the Amount column 
Data_2021["Amount in USD"] = Data_2021["Amount in USD"].replace({"\$": "", ",": ""}, regex = True)


# In[43]:


# Changing amount datatype to int/float 
Data_2021["Amount in USD"] = pd.to_numeric(Data_2021["Amount in USD"], errors = "coerce").fillna(0, downcast = "infer")


# In[44]:


# Replacing columns within null values with Unknown.
Data_2021["Founded"].replace(np.NaN, value = "unknown", inplace = True)
Data_2021["HeadQuarter"].replace(np.NaN, value = "unknown", inplace = True)
Data_2021["Investor"].replace(np.NaN, value = "unknown", inplace = True)


# In[45]:


#Changing datatype for Founded Column from object to int
Data_2021['Founded']= Data_2021['Founded'].astype('str')


# In[46]:


Data_2021.head()


# In[47]:


# Checking for null values in dataset. 
Data_2021.isnull().sum()


# # CLEANED 2021 DATA

# In[48]:


Data_2021


# # Merging 2018,2019,2020 and 2021 datasets for Analysis and Visualization

# In[49]:


Columns = [Data_2018, Data_2019, Data_2020, Data_2021]
Merged_Data = pd.concat(Columns)
Merged_Data


# ### I am going to drop the Investor and Founded columns in this merged dataset because they are irrelevant to the questions I want to answer. Also, I am dropping these columns because the 2018 dataset does not have the mentioned columns which is going to affect my analysis negatively. Dropping these columns will give the merged datasets uniformity and precise analysis.
# 

# In[50]:


# Dropping the Founded and Investor columns 
Merged_Data.drop(columns = ["Founded", "Investor"], inplace = True)
Merged_Data


# In[51]:


# dropping duplicates in the merged data set. 
Merged_Data.drop_duplicates(inplace = True)
Merged_Data


# In[52]:


Merged_Data["Funding Year"] = pd.to_numeric(Merged_Data["Funding Year"], errors = "coerce").fillna(0, downcast = "infer")
Merged_Data


# In[53]:


# Grouping values in the sector column after duplicates were dropped. 
group_by_sector = Merged_Data["Sector"].value_counts()
group_by_sector.head(60)


# In[54]:


group_by_sector


# In[55]:


# Replacing duplicate sector names in Sector column with a single name
Merged_Data.replace({'Sector':{'EdTech':'Edtech','FinTech':'Fintech','HealthCare':'Healthcare','SaaS startup':'SaaS','HealthTech': 'Healthtech', 'Ecommerce': 'E-commerce','Food':'Foodtech','AI startup':'AI','AgriTech':'Agritech','Logistics & Supply Chain':'Logistics','IT':'Information Technology','Automobile':'Automotive','Tech':'Tech Startup'}}, inplace = True)
Merged_Data


# In[56]:


group_by_sector = Merged_Data["Sector"].value_counts()
group_by_sector


# # DATA ANALYSIS AND VISUALIZATION

# ### The libraries I am going to use for my analysis and visualization have already been imported at the start of my data cleaning. They are matplotlib, seaborn, and plotly.

# # Q1. WHO ARE THE TOP FUNDED STARTUPS IN INDIA?

# In[58]:


x = Merged_Data['Company/Brand'].value_counts()[:10].index
y = Merged_Data['Company/Brand'].value_counts()[:10].values
plt.bar(x,y)
plt.rcParams['figure.figsize'] = (20,10)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.title('TOP FUNDED START-UPS IN INDIA', fontsize = 19, fontweight = 'bold')
plt.xlabel('Start-ups', fontsize = 19, fontweight = 'bold')
plt.ylabel('Amount received', fontsize = 19, fontweight = 'bold')


# ### From the chart, we can see that BharatPe is the top funded startup in the Indian Ecosystem. Bharat is a fintech start up founded in 2018 and has it's HeadQuarter located in Delhi, India. Zomato falls next in place as the next top funded start-up in India.

# # Q2. Which cities are the most favoured by Investors?
# 

# ### For this analysis, I am going to use a pie chart to demonstrate the cities that are most favored by investors.

# In[59]:


fig1 = go.Figure(
    data=go.Pie(values=Merged_Data['HeadQuarter'].value_counts()[:8].values,labels=Merged_Data['HeadQuarter'].value_counts()[:8].index,title='Percentage of cities in every sector'))
fig1.show()


# ### From the illustration above, it is evident that investors prefer start-ups that come up from Bangalore city in India with a percentage of 38.9%. The graph clearly tells us why Bangalore is called the Silicon Valley State of India. The second most favored city is Mumbai, which has a percentage of 21.2%.
# 

# # Q3 . How does the funding change in time?

# In[61]:


c = list(Merged_Data.groupby(Merged_Data['Funding Year']).sum()['Amount in USD'])
d = list(Merged_Data['Funding Year'].value_counts().index.sort_values())
sns.scatterplot(d,c)
plt.plot(d,c)
plt.xlabel('Year', fontsize = 22, fontweight = 'bold')
plt.ylabel('Amount(USD) in billions', fontsize = 22, fontweight = 'bold')
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.title('Amount Funded over the Years', fontsize = 22, fontweight = 'bold')
plt.rcParams['figure.figsize'] = (20,10)
warnings.filterwarnings('ignore')


# ### From the plot above, we can tell that, funding has increased positively over time. Amount funded was stable from year 2018 to 2019 and increases from year 2019 to 2020, and further increases from year 2020 to 2021. This proves that investors invest in the Indian start up more and more as the years go by.
# 

# # Q4. Which year records the most start-ups funded?

# In[62]:


sns.countplot(Merged_Data['Funding Year'])
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.xlabel('Year', fontsize = 22, fontweight = 'bold')
plt.ylabel('No. of Startups Funded', fontsize = 22, fontweight = 'bold')
plt.title('No of Startups Funded Over the Years', fontsize = 22, fontweight = 'bold')
plt.rcParams['figure.figsize'] = (18,8)
warnings.filterwarnings('ignore')


# ### From the graph above, it is clear that 2021 received the most start up funding. 2019 recorded the least funding.

# # Q5. Which Sectors do Investors prefer?

# In[63]:


plt.figure(figsize = (25,18))
sns.barplot(y = group_by_sector[:10].index, x = group_by_sector[:10].values)
plt.xticks(fontsize = 17)
plt.yticks(fontsize = 17)
plt.xlabel("Number of Investors", fontsize = 24, fontweight = 'bold')
plt.ylabel("Sector", fontsize = 24, fontweight = 'bold')
plt.title("SECTORS PREFERRED BY INVESTORS", fontsize = 24, fontweight = 'bold')


# # Summary 

# ### 1. The top funded start ups in the Indian Start-up ecosystem are BharatePe, Zomato and Zetwerk
# 
# ### 2. Bangalore, known as the Silicon Valley State of India, is the most preferred city by Investors. Followed by Mumbai.
# 
# ### 3. 2021 records the year with the most start ups funded
# 
# ### 4. Investors prefer to invest more in Tech start-up companies.
# 
# 
# 
# # Conclusion
# 
# ### To satisfy my hypothesis, 
# 
# 
# ### 1. Investors prefer to invest in Tech start-ups more than the other start ups.
# 
# ### This is clearly stated in Fig 5. Investors prefer to invest in Tech start-ups. Looking at the chart, more than 3 start ups are from the tech sector, with Fintech being at the top, followed by Edtech. 
# 
# 
# ### 2. The Location of a start-up plays a major role in receiving funds from Investors
# 
# ### Yes they do. According to this survey start-ups in Bangalore alone have got more funding than the next 6 cities in line put together. This could also be owing to the fact that Bangalore has the most number of start-ups in the country. 

# In[ ]:




