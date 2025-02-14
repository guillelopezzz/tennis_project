import pandas as pd

def calculate_head_to_head(dataset):
    dataset['tourney_date'] = pd.to_datetime(dataset['tourney_date'], format='%Y%m%d')
    dataset = dataset.sort_values('tourney_date')
    dataset['head_to_head'] = -1.0
    for index, row in dataset.iterrows():
        previous_matches = dataset[((dataset['winner_id'] == row['winner_id']) & (dataset['loser_id'] == row['loser_id']) | (dataset['winner_id'] == row['loser_id']) & (dataset['loser_id'] == row['winner_id'])) & (dataset['tourney_date'] < row['tourney_date'])]
        if not previous_matches.empty:
            wins = len(previous_matches[previous_matches['winner_id'] == row['winner_id']])
            total = len(previous_matches)
            dataset.at[index, 'head_to_head'] = wins / total
    return dataset

'''Función para calcular el head_to_head de cada pareja de jugadores. La función tiene en cuenta para cada partido todos los partidos anteriores
y calcula el porcentaje (sobre 1) de veces que ha ganado el jugador 1 (winner_id), obviamente no tiene en cuenta el partido actual.
Para tener en cuenta: Se inicializa en -1, es decir, si los jugadores aún no han jugado la columna head_to_head valdrá -1.'''