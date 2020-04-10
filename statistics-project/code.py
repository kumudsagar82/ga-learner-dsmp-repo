# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv(path)

data['Gender'].replace('-','Agender',inplace=True)
print(data['Gender'])
#path of the data file- path
gender_count=data['Gender'].value_counts()
data['Gender'].value_counts().plot(kind="bar")

#Code starts here 




# --------------
#Code starts here
alignment=data['Alignment'].value_counts()

alignment.plot(kind="pie",autopct='%.2f',label='Character Alignment')



# --------------
#Code starts here
sc_df=data[['Strength','Combat']]
sc_covariance=sc_df.Strength.cov(sc_df.Combat)
sc_strength=sc_df.Strength.std()
sc_combat=sc_df.Combat.std()
sc_pearson=round(sc_covariance/(sc_strength*sc_combat),2)
ic_df=data[['Intelligence','Combat']]
ic_covariance=ic_df.Intelligence.cov(ic_df.Combat)
ic_combat=ic_df.Combat.std()
ic_intelligence=ic_df.Intelligence.std()
ic_pearson=round(ic_covariance/(ic_combat*ic_intelligence),2)



# --------------
#Code starts here

total_high=data['Total'].quantile(q=0.99)

super_best=data[data['Total']>total_high]
super_best_names=list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3)= plt.subplots(1,3,figsize=(20,8))

ax_1.boxplot(super_best['Intelligence'])
ax_1.set(title='Intelligence')

ax_2.boxplot(super_best['Speed'])
ax_2.set(title='Speed')

ax_3.boxplot(super_best['Power'])
ax_3.set(title='Power')







