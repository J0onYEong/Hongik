import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class Movie_recommendation:
    def __init__(self, train_x, train_y):
        self.ts = train_x
        self.ty = train_y
        self.nameToIndex = pd.Series(range(len(train_y)), index=train_y).drop_duplicates()
        # 모든 영화들을 바탕으로 TF-IDF를 계산
        tfidf = TfidfVectorizer()
        # 영화들 간의 유사도를 분석, 각셀은 영화1x영화2의 코사인 유사도를 나타낸다.
        # row는 각영화를 의미함
        matrix = tfidf.fit_transform(train_x)
        self.cosine_sim = linear_kernel(matrix, matrix)

    def extract_similar_movies(self, count, movie_name):
        index = self.nameToIndex[movie_name]

        # 해당 영화와 다른 영화들의 코사인 유사도 추출
        # enumurate는 0 - 인덱스, 1 - 값을 저장함
        cs = list(enumerate(self.cosine_sim[index]))
        cs = sorted(cs, key=lambda x:x[1], reverse=True)
        # 영화의 인덱스 추출
        movie_indices = [i[0] for i in cs[1:1+count]]
        # 추출한 인덱스를 사용하여 영화이름 추출
        titles = [self.ty[index] for index in movie_indices]
        return titles