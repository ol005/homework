import pandas as pd
import argparse
import os
from sqlalchemy import create_engine, text



def main(params):

    user = params.user 
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    tbl_1 = params.tbl_1
    tbl_2 = params.tbl_2
    url_1 = params.url_1
    url_2 = params.url_2

    csv_1 = 'output-1.csv'
    csv_2 = 'output-2.csv'

    os.system(f"wget -O - {url_1} | gunzip > {csv_1}")
    os.system(f"wget {url_2} -O {csv_2}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    green_df_iter = pd.read_csv(csv_1,
                        iterator=True,
                        chunksize=100000,
                        parse_dates=['lpep_pickup_datetime', 'lpep_dropoff_datetime'],
                        dtype={
                                    'VendorID': 'Int64',
                                    'store_and_fwd_flag':'string',
                                    'RatecodeID': 'Int64',
                                    'PULocationID': 'Int64',
                                    'DOLocationID': 'Int64',
                                    'passenger_count': 'Int64',
                                    'trip_distance': 'float64',
                                    'fare_amount': 'float64',
                                    'extra':'float64',
                                    'mta_tax': 'float64',
                                    'tip_amount': 'float64',
                                    'tolls_amount': 'float64',
                                    'ehail_fee': 'float64',
                                    'improvement_surcharge': 'float64',
                                    'total_amount': 'float64',
                                    'payment_type': 'Int64',
                                    'trip_type': 'Int64',
                                    'congestion_surcharge': 'float64'
                                } )
    zones_df = pd.read_csv(csv_2)
  
    with engine.connect() as conn:

        conn.execute(text(f"DROP TABLE IF EXISTS {tbl_1}"))
        conn.commit()

        for df in green_df_iter:
            df.to_sql(name=f'{tbl_1}',con=conn, if_exists='append')
        zones_df.to_sql(name=f'{tbl_2}', con=conn, if_exists='replace', index=False)



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='ingest csv files into postgres db')

    parser.add_argument('--user', help='user for postgres_ingest')
    parser.add_argument('--password', help='password for postgres_ingest')
    parser.add_argument('--host', help='host for postgres_ingest')
    parser.add_argument('--port', help='port for postgres_ingest')
    parser.add_argument('--db', help='db for postgres_ingest')
    parser.add_argument('--tbl_1', help='tbl-1 for postgres_ingest')
    parser.add_argument('--tbl_2', help='tbl-2 for postgres_ingest')
    parser.add_argument('--url_1', help='url of csv-1 for postgres_ingest')
    parser.add_argument('--url_2', help='url of csv-2 for postgres_ingest')

    args = parser.parse_args()
    main(args)