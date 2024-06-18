This is a DBT project which has a Postgre database as DW to run the transformations.
Every technology is open-source and you can do locally on your machine.


>> It's necessary to have a Postgres database  to run this project.
This Postgres database you can install on your local machine via docker, to achieve that you need to have Docker installed
on yout local machine as well.
Or, you can use a POstgres databse hosted somewhere wich you have access on it.

If you choose to use Docker:
sudo docker run --name DATABASE_NAME -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres

Obs: free port 5432 to have access to container

>> Create three schemas on your database(dw) called: bronze, silver and gold

>> I'm gonna use a Python script to load the CSV files(sources) to Postgres tables


# Step 2:

First, create a virtual enviroment
>> python3 -m venv .venv

Activate the environment
>> source .venv/Scripts/activate

# Step 4:
>> python import_tables.py

# Step 5:
Install package dbt-postgres
>> pip install dbt-postgres

# Step 6:
Init a DBT Project
>> dbt init owsbanco

# Step 7:
Connect DBT to databse(DW)

# Step 8:
Create profiles.yml to connect DBT to postgresql

# Step 9: run specific model called location.sql
>> dbt run --select location

# Step 10:
>> dbt docs generate

>> dbt run

>> dbt docs serve


test dbt debug

# Step 11:
If want to run the project in prd enviroment
>> dbt build --target=prod