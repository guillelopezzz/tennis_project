import pandas as pd

def puntos_ranking(dataset, dataset_r, year):
    dataset_r.loc[:, 'ranking_date'] = pd.to_datetime(dataset_r['ranking_date'], format='%Y%m%d')
    dataset_r.loc[:, 'year_month'] = dataset_r['ranking_date'].dt.to_period('M')
    dataset_2023 = dataset_r[dataset_r['ranking_date'].dt.year == year]
    dataset.loc['tourney_date'] = pd.to_datetime(dataset['tourney_date'], format='%Y%m%d')
    dataset.loc['year_month'] = dataset['tourney_date'].dt.to_period('M')
    X_df = dataset[['winner_id', 'loser_id', 'surface']].copy()
    X_df['winner_points'] = 0
    X_df['loser_points'] = 0
    for i in range(X_df.shape[0]):
        winner_id, loser_id = X_df.loc[i, 'winner_id'], X_df.loc[i, 'loser_id']
        year_month = dataset.loc[i, 'year_month']
        winner_points = dataset_2023.loc[(dataset_2023['player'] == winner_id) & (dataset_2023['year_month'] == year_month), 'points']
        loser_points = dataset_2023.loc[(dataset_2023['player'] == loser_id) & (dataset_2023['year_month'] == year_month), 'points']
        if not winner_points.empty:
            X_df.loc[i, 'winner_points'] = winner_points.values[0]
        if not loser_points.empty:
            X_df.loc[i, 'loser_points'] = loser_points.values[0]
    return X_df

'''La necesidad de este programa se debe a datos faltantes por parte de las bases de datos atp_matches_{year}.csv. A pesar de que para cada partido establece
los puntos en el ranking para cada jugador, hay ocasiones en las que falta esa información.
Para tener en cuenta: los jugadores que no encuentre en el ranking tomarán el valor de 0 para sus puntos de ranking.'''