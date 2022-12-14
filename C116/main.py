import pandas as pd
import plotly.express as px
import plotly.graph_objects as pgo
df=pd.read_csv("data.csv")
salary=df["EstimatedSalary"].tolist()
age=df["Age"].tolist()
purchased=df["Purchased"].tolist()
colors=[]
for i in purchased:
  if i==1:
    colors.append("green")
  else:
    colors.append("red")
graph=pgo.Figure(data=pgo.Scatter(x=salary,y=age,mode='markers',marker=dict(color=colors)))
graph.show()

factors=df[["EstimatedSalary","Age"]]
purchase=df["Purchased"]

from sklearn.model_selection import train_test_split 

salary_train, salary_test, purchase_train, purchase_test = train_test_split(factors, purchase, test_size = 0.25)

print(salary_train[0:3])


from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
salary_train=sc.fit_transform(salary_train)
salary_test=sc.fit_transform(salary_test)

print(salary_train[0:3])

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(random_state=0)
lr.fit(salary_train,purchase_train)

pr=lr.predict(salary_test)

from sklearn.metrics import accuracy_score
print("Accuracy: ", accuracy_score(purchase_test,pr))

uage=int (input("Age: "))
usal=int (input("Salary: "))
utest=sc.transform([[usal,uage]])
upr=lr.predict(utest)
if upr[0]==1:
  print("Might purchase")
else:
  print("Might not purchase")