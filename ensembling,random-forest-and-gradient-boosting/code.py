# --------------
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
df=pd.read_csv(path)
df.head()
df = pd.read_csv(filepath_or_buffer=path,compression='zip')

# Code starts here

y = df['attr1089']
X = df.drop(columns=['attr1089'])
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=4)
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
print(X_test[45,5])




# Code ends here


# --------------
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
lr=LogisticRegression()
lr.fit(X_train,y_train)
y_pred=lr.predict(X_test)
roc_score=roc_auc_score(y_test,y_pred)


# --------------
from sklearn.tree import DecisionTreeClassifier

dt=DecisionTreeClassifier(random_state=4)
dt.fit(X_train,y_train)
y_pred=dt.predict(X_test)
roc_score=roc_auc_score(y_test,y_pred)


# --------------
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(random_state=4)
rfc.fit(X_train,y_train)
y_pred=rfc.predict(X_test)


# Code strats here



# Code ends here
roc_score=roc_auc_score(y_test,y_pred)
print(roc_score)


# --------------
# Import Bagging Classifier
from sklearn.ensemble import BaggingClassifier

bagging_clf=BaggingClassifier(base_estimator= DecisionTreeClassifier(), n_estimators=100 , max_samples=100, random_state=0)
bagging_clf.fit(X_train,y_train)
score_bagging=bagging_clf.score(X_test,y_test)
# Code starts here


# Code ends here


# --------------
# Import libraries
from sklearn.ensemble import VotingClassifier

# Various models
clf_1 = LogisticRegression()
clf_2 = DecisionTreeClassifier(random_state=4)
clf_3 = RandomForestClassifier(random_state=4)

model_list = [('lr',clf_1),('DT',clf_2),('RF',clf_3)]
voting_clf_hard=VotingClassifier(estimators=model_list,voting='hard')
voting_clf_hard.fit(X_train,y_train)
hard_voting_score=voting_clf_hard.score(X_test,y_test)
# Code starts here



# Code ends here


