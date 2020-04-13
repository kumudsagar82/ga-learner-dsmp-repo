# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv(path)

data=data[data['Rating']<=5]

plt.hist(data['Rating'],bins=20)
#Code starts here


#Code ends here


# --------------
# code starts here
total_null=data.isnull().sum()
print(total_null)
percent_null=(total_null/data.isnull().count())
print(percent_null)
missing_data=pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'])
print(missing_data)
# code ends here
data.dropna(inplace = True)
total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().count())
missing_data_1 = pd.concat([total_null_1, percent_null_1], axis=1, keys=['Total', 'Percent'])
print(missing_data_1)



# --------------

#Code starts here
ax=sns.catplot(x="Category", y="Rating",kind="box", height=10,data=data)

ax.set_xticklabels(rotation=90)
plt.title('Rating vs Category')

#Code ends here

#ax = sns.boxplot(x='categories', y='oxygen', hue='target', data=df)
#ax.set_xticklabels(ax.get_xticklabels(),rotation=30)


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here



#data['Installs'].map(lambda v: v.replace("+"," "))#data['Installs'].map(lambda v: v.replace(","," "))

data['Installs']=data['Installs'].str.replace(',','')
data['Installs']=data['Installs'].str.replace('+','')


#Code ends here
data['Installs']= data['Installs'].astype(int)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['Installs']=le.fit_transform(data['Installs'])
plt.figure(figsize = (10,10))

sns.regplot(x="Installs", y="Rating" , data=data)


# --------------
#Code starts here
data['Price'] = data['Price'].str.replace('$','') 
b=data['Price'].value_counts()
print(b)
#Code ends here
data['Price']=data['Price'].astype(float)
sns.regplot(x="Price", y="Rating" , data=data)


# --------------

#Code starts here

print(len(data['Genres'].unique()),"genres")

data['Genres'] = data['Genres'].str.split(';').str[0]

gr_mean=data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()

print(gr_mean.describe())
gr_mean=gr_mean.sort_values('Rating')


#Code ends here


# --------------

#Code starts here

data['Last Updated'] = pd.to_datetime(data['Last Updated']) 

data['Last Updated Days'] = (data['Last Updated'].max()-data['Last Updated'] ).dt.days 


plt.figure(figsize = (10,10))
sns.regplot(x="Last Updated Days", y="Rating", color = 'lightpink',data=data )

#Code ends here


