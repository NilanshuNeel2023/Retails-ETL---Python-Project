import pandas as pd 

def extract_data():
    features_df = pd.read_csv(r'F:\Google Course of Data Science\Youtube\Python Projects\Retails ETL Python Project\Data\features_dataset.csv')
    sales_df = pd.read_csv(r'F:\Google Course of Data Science\Youtube\Python Projects\Retails ETL Python Project\Data\sales_dataset.csv')
    stores_df = pd.read_csv(r'F:\Google Course of Data Science\Youtube\Python Projects\Retails ETL Python Project\Data\stores_dataset.csv')

    print("Features Dataset")
    print(features_df.head())
    print(features_df.dtypes)

    print("Sales Dataset")
    print(sales_df.head())
    print(sales_df.dtypes)

    print("Stores Dataset")
    print(stores_df.head())
    print(stores_df.dtypes)

    return(features_df, sales_df, stores_df)