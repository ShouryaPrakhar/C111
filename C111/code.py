import csv
import plotly.figure_factory as ff 
import pandas as pd 
import random
import statistics
import plotly.graph_objects as go 
 
df = pd.read_csv("data.csv")
data = df["Math_score"].tolist()

#fig = ff.create_distplot([data] , ["Math Score"] , show_hist=False)
#fig.show()

#mean = statistics.mean(data)
#std = statistics.stdev(data)
#print(mean)
#print(std)
def randomM(counter):
    dataset = []
    for i in range(0,counter):
        randomI = random.randint(0,len(data)-1)
        value = data[randomI]
        dataset.append(value)
    mean = statistics.mean(dataset)

    return mean 
meanList = []
for i in range(0,1000):
    setOfMean = randomM(100)
    meanList.append(setOfMean)

std = statistics.stdev(meanList)
mean = statistics.mean(meanList)

std_1_start,std_1_end = mean-std , mean+std
std_2_start,std_2_end = mean-(2*std) , mean+(2*std)
std_3_start,std_3_end = mean-(3*std) , mean+(3*std)
print(mean)
print(std)
print("std1" , std_1_start , std_1_end)
print("std2" , std_2_start , std_2_end)
print("std3" , std_3_start , std_3_end)
fig = ff.create_distplot([meanList] , ["Math Score"] , show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean] , y = [0,0.20] , mode = "lines" , name = "Mean"))
fig.add_trace(go.Scatter(x = [std_1_start,std_1_start] , y = [0,0.17] , mode = "lines" , name = "std1 Start"))
fig.add_trace(go.Scatter(x = [std_1_end,std_1_end] , y = [0,0.17] , mode = "lines" , name = "std1 End"))
fig.add_trace(go.Scatter(x = [std_2_start,std_2_start] , y = [0,0.17] , mode = "lines" , name = "std2 Start"))
fig.add_trace(go.Scatter(x = [std_2_end,std_2_end] , y = [0,0.17] , mode = "lines" , name = "std2 End"))
fig.add_trace(go.Scatter(x = [std_3_start,std_3_start] , y = [0,0.17] , mode = "lines" , name = "std3 Start"))
fig.add_trace(go.Scatter(x = [std_3_end,std_3_end] , y = [0,0.17] , mode = "lines" , name = "std3 End"))
fig.show()
        
