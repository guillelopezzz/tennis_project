import numpy as np
import pandas as pd
def puntos_ranking(dataset, dataset_r, year):
    # Convertir la columna 'ranking_date' a formato de fecha
    dataset_r.loc[:, 'ranking_date'] = pd.to_datetime(dataset_r['ranking_date'], format='%Y%m%d')

    # Extraer solo el año y el mes
    dataset_r.loc[:, 'year_month'] = dataset_r['ranking_date'].dt.to_period('M')

    # Filtrar las filas para el año 2023
    dataset_year = dataset_r[dataset_r['ranking_date'].dt.year == year]

    # Convertir la columna 'tourney_date' a formato de fecha
    dataset['tourney_date'] = pd.to_datetime(dataset['tourney_date'], format='%Y%m%d')

    # Extraer solo el año y el mes
    dataset['year_month'] = dataset['tourney_date'].dt.to_period('M')

    # Convertir X en un DataFrame de pandas
    X_df = dataset[['winner_id', 'loser_id', 'surface']].copy()

    # Añadir dos nuevas columnas inicializadas en 0
    X_df['winner_points'] = 0
    X_df['loser_points'] = 0

    # Iterar sobre las filas de X_df
    for i in range(X_df.shape[0]):
        # Obtener los códigos de los jugadores
        winner_id, loser_id = X_df.loc[i, 'winner_id'], X_df.loc[i, 'loser_id']

        # Obtener el año y el mes del partido
        year_month = dataset.loc[i, 'year_month']
        # Buscar los puntos de los jugadores en dataset_year
        # Ahora deberías poder hacer la comparación sin problemas
        winner_points = dataset_year.loc[(dataset_year['player'] == winner_id) & (dataset_year['year_month'] == year_month), 'points']
        loser_points = dataset_year.loc[(dataset_year['player'] == loser_id) & (dataset_year['year_month'] == year_month), 'points']

        # Si se encontraron los puntos, actualizar los valores en X_df
        if not winner_points.empty:
            X_df.loc[i, 'winner_points'] = winner_points.values[0]
        if not loser_points.empty:
            X_df.loc[i, 'loser_points'] = loser_points.values[0]
    return X_df[['winner_points', 'loser_points']]