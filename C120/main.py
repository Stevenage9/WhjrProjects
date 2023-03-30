from sklearn import datasets
wine=datasets.load_wine()

print("Features:", wine.feature_names)
print("Labels:", wine.target_names)

from sklearn.model_selection import train_test_split
X=wine.data
y=wine.target
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=109)

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics
model=GaussianNB()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("accuracy :- ",metrics.accuracy_score(y_test,y_pred))