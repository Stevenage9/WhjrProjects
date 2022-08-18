import pandas as pd
import plotly.express as px
import numpy as np
df=pd.read_csv("main.csv")
toefl=df["TOEFL Score"].tolist()
coa=df["Chance of Admit "].tolist()
fig=px.scatter(x=toefl,y=coa)
fig.show()
toefl=np.array(toefl)
coa=np.array(coa)
m,c=np.polyfit(toefl,coa,1)
y=[]
for x in toefl:
  y_value=(m*x)+c
  y.append(y_value)
fig=px.scatter(x=toefl,y=coa)
fig.update_layout(shapes=[dict(type="line",y0=min(y),y1=max(y),x0=min(toefl),x1=max(toefl))])
fig.show()
x=250
y=(m*x)+c
print("coa of someone with toefl",x,"is",y)
input("enter to close")