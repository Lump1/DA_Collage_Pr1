import datetime
import pandas as pd

def get_col_row_size(df: pd.DataFrame):
    return df.shape

def get_column_names(df: pd.DataFrame):
    return df.columns.tolist()

def get_column_types(df: pd.DataFrame):
    return df.dtypes

def sort_by_full_name(df: pd.DataFrame):
    return df.sort_values(by='Full Name')

def count_by_gender(df: pd.DataFrame):
    return df['Sex'].value_counts()

def most_nobel_winning_country(df: pd.DataFrame):
    return df['Birth Country'].value_counts().idxmax()

def first_female_nobel_laureate(df: pd.DataFrame):
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df_female = df[df['Sex'] == 'Female']
    first_female = df_female.loc[df_female['Year'].idxmin()]
    return first_female['Full Name']

def posthumous_nobel_winners(df: pd.DataFrame):
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df['Death Date'] = pd.to_datetime(df['Death Date'], errors='coerce')
    df['Death Year'] = df['Death Date'].dt.year

    return df[(df['Death Year'].notna()) & (df['Year'] > df['Death Year'])][['Full Name', 'Year', 'Death Year']]

def multiple_nobel_winners(df: pd.DataFrame):
    return df[df.duplicated(subset=['Full Name'], keep=False)][['Full Name', 'Organization Name']].drop_duplicates()

def add_age_column(df: pd.DataFrame):
    df['Birth Date'] = pd.to_datetime(df['Birth Date'], errors='coerce')
    birth_year_df = df['Birth Date'].dt.year

    df['Age'] = df['Year'] - birth_year_df
    return df

def age_statistics_by_gender(df: pd.DataFrame):
    return df.groupby('Sex')['Age'].agg(['min', 'max'])

def average_age_by_category_and_gender(df: pd.DataFrame):
    return df.groupby(['Category', 'Sex'])['Age'].mean()

def gender_percentage_by_category(df: pd.DataFrame):
    category_sex_counts = df.groupby(['Category', 'Sex']).size().unstack()
    return category_sex_counts.div(category_sex_counts.sum(axis=1), axis=0) * 100