from functools import lru_cache


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    return []

# A função deve receber um path (uma string com o caminho para um arquivo).
# A função deve abrir o arquivo e ler seus conteúdos.
# A função deve tratar o arquivo como CSV.
# A função deve retornar uma lista de dicionários, onde as chaves são os cabeçalhos de cada coluna e os valores correspondem a cada linha.