import pandas as pd

def get_data(url: str) -> pd.DataFrame:
    nobel_df = pd.read_csv(url)

    return nobel_df