def codificacion(dataset, num_bits):
    for col in ['winner_id', 'loser_id']:
        dataset[col] = dataset[col].apply(lambda x: format(x, f'0{num_bits}b'))
    return dataset

'''Esta función codifica a los jugadores transformando la clave de los jugadores (decimal) a binario.
Lo hace recibiendo un número predeterminado de bits que tiene que usar, si para un número se usan menos bits se rellenará con 0s a la izquierda.
De esta forma se optimiza el número de columnas utilizadas en el modelo'''