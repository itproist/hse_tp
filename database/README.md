# Database
Our project uses PostgreSQL as its database. This folder contains some files to initialize database and add some records to it.
# Structure
In order to deploy database on your device you need to insert into PostgreSQL shell commands from following files:

1) `Database_create.txt` (creates tables and some custom enums)
2) `Products.txt` (inserts values into products table)
3) `Dishes.txt` (inserts values into dishes and ingredients tables)

After this your database is ready to be used by server.