import pandas as pd
import plotly.express as px

df = pd.read_csv("covid_data.csv")

fig = px.scatter(df, x="Date", y="Cases", color="Country",title='Covid Data')
fig.show()