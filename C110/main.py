import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

import statistics
import random

df=pd.read_csv("data.csv")
data=df["temp"].tolist()
def random_set_of_mean(counter):
    dataset=[]
    for o in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="mean"))
    fig.show()


def setup():
    meanlist=[]
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        meanlist.append(set_of_means)
    show_fig(meanlist)
    
    mean=statistics.mean(meanlist)
    print("Mean of sample=",mean )
setup()

population_mean=statistics.mean(data)
print("Mean of population=", population_mean)

def stdevf():
    meanlist=[]
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        meanlist.append(set_of_means)

    stdev=statistics.stdev(meanlist)
    print("Standard deviation of sample=", stdev)

stdevf()