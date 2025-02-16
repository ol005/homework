## Question 1
```bash
pip install dlt[duckdb]
dlt --version
```
1.6.1

## Question 2

```python
@dlt.resource(name="rides")
def ny_taxi():
    client= RESTClient(
        base_url="https://us-central1-dlthub-analytics.cloudfunctions.net",
        paginator=PageNumberPaginator(
            base_page=1,
            total_path=None
        )
    )
    for page in client.paginate("data_engineering_zoomcamp_api"):
        yield page
    
pipeline = dlt.pipeline(
    pipeline_name="ny_taxi_pipeline",
    destination="duckdb",
    dataset_name="ny_taxi_data"
)

load_info = pipeline.run(ny_taxi, write_disposition="replace")
conn = duckdb.connect(f"{pipeline.pipeline_name}.duckdb")
# Set search path to the dataset
conn.sql(f"SET search_path = '{pipeline.dataset_name}'")

# Describe the dataset
print(conn.sql("DESCRIBE").df())
```
4 Tables created

## Question 3
```python
df = pipeline.dataset(dataset_type="default").rides.df()
print(df)
```
10000 rows

## Question 4
```python
with pipeline.sql_client() as client:
    res = client.execute_sql(
            """
            SELECT
            AVG(date_diff('minute', trip_pickup_date_time, trip_dropoff_date_time))
            FROM rides;
            """
        )
    # Prints column values of the first row
    print(res)
```
12.3049