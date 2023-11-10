import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from Model import Movie_recommendation
import re

def processing(str):
    new_str = re.sub(r"[^a-zA-z]", " ", str)
    keywords=new_str.split(" ")
    nop=['to','is','','be','for','from','the','But','but','while','as','from','while','a','an','in','after','at','and','of']
    print(keywords)
    for i in range(0,len(nop)):
        while 1:
            if nop[i] not in keywords:
                break
            keywords.remove(nop[i])
    result=""
    for i in range(0,len(keywords)):
        result+=keywords[i]+" "
    return result


df = pd.read_csv('movies_metadata.csv')

scheme = {
    'title': str,
    'overview': str,
}

df = pd.read_csv('movies_metadata.csv', usecols=['title', 'overview'], dtype=scheme)


titles = df[['title']]
overviews = df[['overview']]

trainData_x = np.array([element[0] for element in overviews.values])
trainData_y = np.array([element[0] for element in titles.values])

model1 = Movie_recommendation(trainData_x[0:1000], trainData_y[0:1000])

print("결과: {}".format(model1.extract_similar_movies(3, 'Toy Story')))





