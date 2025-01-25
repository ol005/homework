
## Question 1

Terminal commands:

```bash
docker run -it python:3.12.8 bash
pip --version
```

## Question 2
pgAdmin connects to either postgres or db hostname on port 5432

## Prepare Postgres

Build pipeline image from Dockerfile
```bash
docker build -t import_taxi_data:v1 ./ingestion_scriptpy
```
run the docker-compose yaml file
```bash
docker compose up -d
```

run pipeline container
```bash
docker run -it \
--name taxi-pipeline \
--network 01-docker-terraform_default \
import_taxi_data:v1 \
--user=postgres \
--password=postgres \
--host=postgres \
--port=5432 \
--db=ny_taxi \
--tbl_1=green_taxi_tripdata \
--tbl_2=taxi_zones \
--url_1="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz" \
--url_2="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"
```



## Question 3
SQL Query
```sql
SELECT SUM(case when trip_distance <= 1.0 then 1 else 0 end) as miles_lt1
	  ,SUM(case when trip_distance > 1.0 AND trip_distance <= 3.0 then 1 else 0 end) as miles_1_3 
	  ,SUM(case when trip_distance > 3.0 AND trip_distance <= 7.0 then 1 else 0 end) as miles_3_7
	  ,SUM(case when trip_distance > 7.0 AND trip_distance <= 10.0 then 1 else 0 end) as miles_7_10
	  ,SUM(case when trip_distance > 10.0 then 1 else 0 end) as miles_gt10
FROM green_taxi_tripdata
WHERE cast(lpep_pickup_datetime as date) >= '2019-10-01'
AND cast(lpep_dropoff_datetime as date) < '2019-11-01';
```

## Question 4
SQL Query
```sql
select lpep_pickup_datetime from green_taxi_tripdata
where trip_distance = (SELECT MAX(trip_distance) FROM green_taxi_tripdata);
```

## Question 5
SQL Query
```sql
SELECT tz."Zone" as pickup_location, sum(gt.total_amount) as total_amount from green_taxi_tripdata gt
INNER JOIN taxi_zones tz
ON gt."PULocationID" = tz."LocationID"
WHERE cast(gt.lpep_pickup_datetime as date) = '2019-10-18'
GROUP BY tz."Zone"
HAVING sum(gt.total_amount) > 13000
ORDER BY total_amount desc;
```

## Question 6
SQL Query
```sql
SELECT dz."Zone" as drop_zone, max(td.tip_amount) as max_tip FROM green_taxi_tripdata td
INNER JOIN taxi_zones pz
ON pz."LocationID" = td."PULocationID"
INNER JOIN taxi_zones dz
ON dz."LocationID" = td."DOLocationID"
WHERE cast(td.lpep_pickup_datetime as date) BETWEEN '2019-10-01' AND '2019-10-31' 
AND pz."Zone" = 'East Harlem North'
GROUP BY dz."Zone"
ORDER BY max_tip desc;
```

## Terraform Section
Terraform
Set the env var and activate gcp service account creds
```bash
export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/dataeng.json
```

```bash
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
```

terraform order of operations:
```bash
cd terraform
terraform init
terraform apply -auto-approve
terraform destroy
```