from time import time
from collections import defaultdict

import numpy as np
import pandas as pd
#import seaborn as sns

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.metrics import f1_score, accuracy_score
from sklearn.model_selection import ShuffleSplit
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.linear_model import SGDClassifier, LogisticRegression, LogisticRegressionCV
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import MultinomialNB, CategoricalNB, ComplementNB, BernoulliNB
from sklearn.decomposition import FastICA, KernelPCA, TruncatedSVD, SparsePCA, NMF, FactorAnalysis, LatentDirichletAllocation

import nltk

lemmatizer = nltk.WordNetLemmatizer() # english


import nltk

nltk.download('punkt')
nltk.download('stopwords')


def lemmatize(sentence):
    v = sentence.split()
    # take lower case
    #vv = [x.lower() for x in v]
    # remove stopwords
    #vvv = [x for x in vv if x not in stopwords]
    # remove punction ...
    v = [lemmatizer.lemmatize(x) for x in v]
    return " ".join(v)
