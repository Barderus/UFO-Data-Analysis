import pandas as pd

def load_ufo_data(filepath):
    df = pd.read_csv(filepath, low_memory=False)
    return df
