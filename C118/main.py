import pandas as pd
import plotly.express as px
df=pd.read_csv("stars.csv")
print(df.head())

graph=px.scatter(df,x="Size",y="Light")
graph.show()

from sklearn.cluster import KMeans
x=df.iloc[:,[0,1]].values
Wcss=[]
for i in range(1,11):
  kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
  kmeans.fit(x)
  Wcss.append(kmeans.inertia_)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,5))
sns.lineplot(range(1,11),Wcss,marker='o',color='green')
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Wcss')
plt.show()

kmeans=KMeans(n_clusters=3,init='k-means++',random_state=42)
ykmeans=kmeans.fit_predict(x)

plt.figure(figsize=(15,7))
sns.scatterplot(x[ykmeans==0,0],x[ykmeans==0,1],color='red',label='cluster 1')
sns.scatterplot(x[ykmeans==1,0],x[ykmeans==1,1],color='green',label='cluster 2')
sns.scatterplot(x[ykmeans==2,0],x[ykmeans==2,1],color='blue',label='cluster 3')
sns.scatterplot(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],color='orange',label='centroid',s=250)
plt.grid(False)
plt.title('Clusters')
plt.xlabel('Star size')
plt.ylabel('Star luminosity')
plt.show()