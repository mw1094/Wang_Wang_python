# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 07:37:23 2016

@author: Meng Wang
"""

#question 1
'''
Search for the IRIS dataset on the internet. You should quickly find the UCI Machine Learning
repository. Instead of downloading the files, figure out how to directly load the files from the
internet into Python and add the column names using Python code instead of an editor.
'''
import pandas as pd #import pandas
a=pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
              names=['sepal length','sepal width','petal length','petal width','class'])#columns names="" creat a dataframe using data from website 

#question 2
'''
Using Pandas, display the first ten and the last ten rows of the data.
'''
a.head(10) #display first 10 rows of data
a.tail(10) #display last 10 rows of data

#question 3
'''
Using Pandas, print simple location statistics (Count, Mean, STD, Min, 25%, 50%, 75%, MAX).
There is a single method call that will accomplish this.
'''
a.describe() #use this function can display Count, Mean, STD, Min, 25%, 50%, 75%, MAX.

#question 4
'''
Write a function that accepts a list of numbers that represent numbers of bins and, using
Pandas, plots a histogram for each of the numeric columns at each bin size. For example, if I call
your function with [10, 50, 100] as bin sizes, the function should plot 12 histograms (3 for each
numeric variable). Group the histograms by the column name.
'''
columnname = ['sepal length', 'sepal width', 'petal length',
          'petal width', 'class']
def plothist(list1):
    for col in columnname[0:4]: # grouping by column names
        for i in list1: # then for each bin size
            a.hist(column = col, bins = i) # print a histogram
        
##Prof G - Poor choices for testing. Try 10, 50, 100        
plothist([1,2,3])
        
#question 5
'''
Plot a box plot for each of the numeric column.
'''
##Prof G - Nicer to have them all on the same graph
import matplotlib.pyplot as plot
plot.figure('sepal length box')#creat a new figure
a['sepal length'].plot.box()#box plot
plot.figure('sepal width box')
a['sepal width'].plot.box()
plot.figure('petal length box')
a['petal length'].plot.box()
plot.figure('petal width box')
a['petal width'].plot.box()

#qeustion 6
'''
Plot a bar chart for the nominal column.
'''
a['class'].value_counts().plot.bar() #count names frequency and plot a bar chart