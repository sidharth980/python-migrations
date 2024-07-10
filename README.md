
# Docker setup for postgres

docker run --name postgres -e POSTGRES_USER=sampleuser -e POSTGRES_PASSWORD=sampledb -e POSTGRES_DB=sampledb -p 5432:5432 -d postgres

# setup 
create .env and add the following 

- DB_USER = "sampleuser" 
- DB_PASSWORD = "samplepass"
- DB_NAME = "mydatabase"


create a folder called versions
add sql commands in order eg
v1.sql
v2.sql 
etc


