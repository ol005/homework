# Question 1
Uncompressed file size

```yaml
id: purge_files
type: io.kestra.plugin.core.storage.PurgeCurrentExecutionFiles
description: If you'd like to explore Kestra outputs, disable it.
disabled: true
```

Set disabled to true in the purge task to be able to inspect 
128.3 MiB = 134.5 MB

# Question 2

Checking the logs of flow execution we can see the rendered value for file var is green_tripdata_2020-04.csv

# Question 3

```sql
select count(*)
from (
SELECT 1 FROM `ny_taxis.yellow_tripdata_2020_01_ext`
union all
SELECT 1 FROM `ny_taxis.yellow_tripdata_2020_02_ext`
union all
SELECT 1 FROM `ny_taxis.yellow_tripdata_2020_03_ext`
union all
SELECT 1 FROM `ny_taxis.yellow_tripdata_2020_04_ext`
union all
SELECT 1 FROM `ny_taxis.yellow_tripdata_2020_05_ext`
union all
SELECT 1 FROM `ny_taxis.yellow_tripdata_2020_06_ext`
union all
SELECT 1 FROM `ny_taxis.yellow_tripdata_2020_07_ext`
union all
SELECT 1 FROM `ny_taxis.yellow_tripdata_2020_08_ext`
union all
SELECT 1 FROM `ny_taxis.yellow_tripdata_2020_09_ext`
union all
SELECT 1 FROM `ny_taxis.yellow_tripdata_2020_10_ext`
union all
SELECT 1 FROM `ny_taxis.yellow_tripdata_2020_11_ext`
union all
SELECT 1 FROM `ny_taxis.yellow_tripdata_2020_12_ext`
)
```

# Question 4

```sql
select count(*)
from (
SELECT 1 FROM `ny_taxis.green_tripdata_2020_01_ext`
union all
SELECT 1 FROM `ny_taxis.green_tripdata_2020_02_ext`
union all
SELECT 1 FROM `ny_taxis.green_tripdata_2020_03_ext`
union all
SELECT 1 FROM `ny_taxis.green_tripdata_2020_04_ext`
union all
SELECT 1 FROM `ny_taxis.green_tripdata_2020_05_ext`
union all
SELECT 1 FROM `ny_taxis.green_tripdata_2020_06_ext`
union all
SELECT 1 FROM `ny_taxis.green_tripdata_2020_07_ext`
union all
SELECT 1 FROM `ny_taxis.green_tripdata_2020_08_ext`
union all
SELECT 1 FROM `ny_taxis.green_tripdata_2020_09_ext`
union all
SELECT 1 FROM `ny_taxis.green_tripdata_2020_10_ext`
union all
SELECT 1 FROM `ny_taxis.green_tripdata_2020_11_ext`
union all
SELECT 1 FROM `ny_taxis.green_tripdata_2020_12_ext`
)
```

# Question 5

```sql
select count(*) from `ny_taxis.yellow_tripdata_2021_03_ext`
```

# Question 6

```yaml
triggers:
  - id: green_schedule
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "0 9 1 * *"
    timezone: America/New_York
    inputs:
      taxi: green
```