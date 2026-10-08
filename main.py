from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():
    print("Pipeline Started")

    features_df, sales_df, store_df = extract_data()
    dim_date, dim_feature, dim_store, fact_sales = transform_data(features_df, sales_df, store_df)
    
    load_data(dim_date, dim_feature, dim_store, fact_sales)

    print('Pipeline completed, Data loaded to MySQL Succesfully')

if __name__ == "__main__":
    run_pipeline()
    