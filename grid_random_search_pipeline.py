import pandas as pd 
import numpy as np

from sklearn import ensemble
from sklearn import metrics
from sklearn import model_selection
from sklearn import preprocessing
from sklearn import decomposition
from sklearn import pipeline

if __name__=='__main__':
    df = pd.read_csv('train.csv')
    X  = df.drop('price_range',axis=1).values
    y = df.price_range.values

    scl = preprocessing.StandardScaler()
    pca = decomposition.PCA()
    rf = ensemble.RandomForestClassifier(n_jobs=-1)
    classifier = pipeline.Pipeline([('scaling',scl),('pca',pca),('rf',rf),])

    param_grid = {
        'pca__n_components':[5,6,7,8,9,10],
        'rf__n_estimators': [100,200,300],
        'rf__max_depth': [1,3,5],
        'rf__criterion': ['gini','entropy'],
    }

    model = model_selection.RandomizedSearchCV(
        estimator=classifier, 
        param_distributions=param_grid,
        scoring='accuracy',
        n_iter=10,
        n_jobs=1,
        verbose=10,
        cv = 5,
    )
    model.fit(X,y)
    print(model.best_score_)
    print(model.best_estimator_.get_params())



