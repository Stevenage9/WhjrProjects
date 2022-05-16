import pandas as pd
import plotly.figure_factory as ff
import csv
df=pd.read_csv("data.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg Ratings of Mobile Brands"],show_hist=False)
fig.show()