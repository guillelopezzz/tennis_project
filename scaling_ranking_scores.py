import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def scaling_ranking_scores(dataset, num):
    scaler = MinMaxScaler(feature_range=(num, 1))
    dataset['winner_points'] = scaler.fit_transform(dataset[['winner_points']])
    dataset['loser_points'] = scaler.fit_transform(dataset[['loser_points']])
    return dataset
'''El dataset de entrada tiene que haber tratado el problema de los NaN's a través de ranking_scores.py.
Esta función devuelve un dataframe con puntos de ranking escalados entre 0.5 y 1.
Tiene dos objetivos: solucionar el problema de datos atípicos en las estadísticas
y hacer notoria la diferencia entre ganarle a jugadores de diferente nivel'''