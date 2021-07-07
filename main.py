import plotly.express as px
import csv
import numpy as np 

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x='Days Present',y='Marks In Percentage')
        fig.show()

#get the data source

def getDataSource(data_path):
    days=[]
    marks=[]

    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            days.append(float(row['Days Present']))
            marks.append(float(row['Marks In Percentage']))

    return {'x':days,'y':marks}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource['x'],datasource['y'])
    print('correlation',correlation[0,1])

def setup():
    data_path='F:\python\project\P106\Student Marks vs Days Present.csv'
    datasource=getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()