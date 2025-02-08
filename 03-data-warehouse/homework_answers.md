## Setup

Run load_yellow_taxi_data.py to download and upload to GCS Bucket

Create the External and Materialized tables:

```sql
CREATE OR REPLACE EXTERNAL TABLE `dataeng-course-project.ny_taxi.yellow_tripdata_2024_ext`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://data-zoomcamp-taxi-43920493/yellow_tripdata_2024-*.parquet']
);
```

```sql
CREATE OR REPLACE TABLE `dataeng-course-project.ny_taxi.yellow_tripdata_2024` AS
SELECT * FROM `dataeng-course-project.ny_taxi.yellow_tripdata_2024_ext`;
```

## Question 1

```sql
SELECT COUNT(*) FROM `ny_taxi.yellow_tripdata_2024`;
```
## Question 2

```sql
SELECT COUNT(PULocationID) FROM `ny_taxi.yellow_tripdata_2024_ext`;
SELECT COUNT(PULocationID) FROM `ny_taxi.yellow_tripdata_2024`;
```

## Question 3

```sql
SELECT PULocationID FROM `ny_taxi.yellow_tripdata_2024`;
SELECT PULocationID, DOLocationID FROM `ny_taxi.yellow_tripdata_2024`;
```

# Question 4

```sql
SELECT COUNT(*) FROM `ny_taxi.yellow_tripdata_2024`
WHERE fare_amount = 0;
```

# Question 5

```sql
CREATE OR REPLACE TABLE `ny_taxi.yellow_tripdata_2024_partition` 
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS SELECT * FROM `ny_taxi.yellow_tripdata_2024_ext`;
```

# Question 6

```sql
SELECT DISTINCT VENDORID FROM `ny_taxi.yellow_tripdata_2024`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';

SELECT DISTINCT VendorID FROM `ny_taxi.yellow_tripdata_2024_partition`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';
```
