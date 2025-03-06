import api_worker as api_W
import data_manipulation as dm

url = 'https://raw.githubusercontent.com/x5or6/A-Visual-History-of-Nobel-Prize-Winners/master/archive.csv'

def main():
    nobel_df = api_W.get_data(url)
    print("Columns, rows size:", dm.get_col_row_size(nobel_df))
    print("Column names:", dm.get_column_names(nobel_df))
    print("Column data types:\n", dm.get_column_types(nobel_df))
    print("Sorted dataset by Full Name:\n", dm.sort_by_full_name(nobel_df).head())
    print("Number of male and female Nobel laureates:\n", dm.count_by_gender(nobel_df))
    print("Country with most Nobel Prize winners:", dm.most_nobel_winning_country(nobel_df))
    print("First female Nobel laureate:", dm.first_female_nobel_laureate(nobel_df))
    print("Posthumous Nobel Prize winners:\n", dm.posthumous_nobel_winners(nobel_df))
    print("Scientists with multiple Nobel Prizes:\n", dm.multiple_nobel_winners(nobel_df))

    nobel_df_with_age = dm.add_age_column(nobel_df)
    print("Age statistics by gender:\n", dm.age_statistics_by_gender(nobel_df_with_age))
    print("Average age of laureates by category and gender:\n", dm.average_age_by_category_and_gender(nobel_df_with_age))
    print("Percentage of male and female laureates by category:\n", dm.gender_percentage_by_category(nobel_df_with_age))

if __name__ == "__main__":
    main()