import pandas as pd
def get_stats(dataset):
    jugadores = pd.concat([dataset['winner_id'], dataset['loser_id']], ignore_index=True)
    codigos_jugadores = set(jugadores) # Conjunto con todos los jugadores de la temporada
    players_stats = {}
    for codigo in codigos_jugadores:
        iter = 0
        filas_w = dataset[(dataset['winner_id'] == codigo)]
        filas_w = filas_w.dropna(subset=['w_svpt', 'w_df', 'w_1stIn', 'w_ace', 'w_1stWon', 'w_2ndWon', 'w_bpSaved', 'w_bpFaced'])
        filas_l = dataset[(dataset['loser_id'] == codigo)]
        filas_l = filas_l.dropna(subset=['l_svpt', 'l_df', 'l_1stIn', 'l_ace', 'l_1stWon', 'l_2ndWon', 'l_bpSaved', 'l_bpFaced'])
        total = [0 for _ in range(6)]
        for result in ['w', 'l']:
            filas = filas_w if result == 'w' else filas_l
            for _, fila in filas.iterrows():
                if fila[f'{result}_svpt'] + fila[f'{result}_df'] != 0:
                    total[0] += fila[f'{result}_1stIn'] / (fila[f'{result}_svpt'] + fila[f'{result}_df']) # Porcentaje primeros servicios
                    total[1] += fila[f'{result}_ace'] / (fila[f'{result}_svpt'] + fila[f'{result}_df']) # Porcentaje de aces
                    total[2] += 1 - (fila[f'{result}_df'] / (fila[f'{result}_svpt'] + fila[f'{result}_df'])) # INVERSA del porcentaje de dobles faltas
                if fila[f'{result}_1stIn'] != 0:                    
                    total[3] += fila[f'{result}_1stWon'] / fila[f'{result}_1stIn'] # Porcentaje de puntos ganados en el primer sv
                if fila[f'{result}_svpt'] - fila[f'{result}_1stIn'] != 0:
                    total[4] += fila[f'{result}_2ndWon'] / (fila[f'{result}_svpt'] - fila[f'{result}_1stIn']) # Porcentaje de puntos ganados de en segundo sv
                if fila[f'{result}_bpFaced'] != 0:
                    total[5] += fila[f'{result}_bpSaved'] / fila[f'{result}_bpFaced'] # Porcentaje de puntos de quiebre salvados
                iter += 1
        if iter > 0:
            players_stats[codigo] = [i/iter for i in total]
    return(players_stats)
