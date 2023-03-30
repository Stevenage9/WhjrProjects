import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

df=pd.read_csv("escape_velocity.csv")

velocity_list=df["Velocity"].tolist()
escaped_list=df["Escaped"].tolist()

fig=px.scatter(x=velocity_list,y=escaped_list)

fig.show()

velocity_array=np.array(velocity_list)
escaped_array=np.array(escaped_list)

m,c=np.polyfit(velocity_array,escaped_array,1)
y=[]

for x in velocity_array:
        y_value=m*x + c
        y.append(y_value)

fig=px.scatter(x=velocity_array,y=escaped_array)
fig.update_layout(shapes=[
        dict(
            type='line',
            y0=min(y),y1=max(y),
            x0=min(velocity_array),x1=max(velocity_array)
        )

])
fig.show()

X=np.reshape(velocity_list,(len(velocity_list),1))
Y=np.reshape(escaped_list,(len(escaped_list),1))

lr=LogisticRegression()
lr.fit(X,Y)

plt.figure()
plt.scatter(X.ravel(),Y,color='black')