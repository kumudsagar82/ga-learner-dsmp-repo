# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv(path)
df.head()
X=df.drop(['list_price'],axis=1)
y=df['list_price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)


# --------------
import matplotlib.pyplot as plt

# code starts here        

cols = X_train.columns
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(20,20))

for i in range(0,3):
    for j in range(0,3): 
            col = cols[i*3 + j]
            axes[i,j].set_title(col)
            axes[i,j].scatter(X_train[col],y_train)
            axes[i,j].set_xlabel(col)
            axes[i,j].set_ylabel('list_price')
plt.show()

# code ends here



# --------------
# Code starts here
# correlation(dataset, threshold):
    #col_corr = set() # Set of all the names of deleted columns
    #corr = dataset.corr()
   # for i in range(len(corr.columns)):
        #for j in range(i):
           # if (corr.iloc[i, j] > threshold) and (corr.columns[j] not in col_corr):
             #   colname = corr.columns[i] # getting the name of column
               # col_corr.add(colname)
               # if colname in dataset.columns:
                #    del dataset[colname] # deleting the column from the dataset

   # print(col_corr)

#correlation(X_train,0.75)
#print(X_train)corr = X_train.corr()
corr=X_train.corr()
print(corr)

X_train.drop(['play_star_rating','val_star_rating'], 1 ,inplace=True)
X_test.drop(['play_star_rating','val_star_rating'], 1 ,inplace=True)

# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here

regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)
mse=mean_squared_error(y_test,y_pred)
print(mse)
r2=r2_score(y_test,y_pred)
# Code ends here


# --------------
# Code starts here
residual=y_test-y_pred
plt.hist(residual,bins=20)


# Code ends here


