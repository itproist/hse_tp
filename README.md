# Smart Chef
Web server for the Smart Chef app. This app can help to select some recipes based on the ingredients user already has.

## Technolages
Our app uses Python powered by django for our backend, html/css with some js for the frontend, and postgreSQL as the database. More information about database configuration you can find in the database folder.
## API
GET `/` - root endpoint that sends main page

POST `/api/recipe` - requires a body with json, that contains array of products,
sends back json with recipies

## How to run the whole system?
Foremostly, to run this system you need to have postgreSQL and python interpreter preinstalled on your PC. Then, follow these steps:
1) Clone both server and telegram bot repository.
2) Open pqsl-shell and follow the instructions from readme in database directory of server repository.
3) Set environment variables to appropriate values.
4) While being in the server's directory, run command `python -m venv directory_name`. This command will create directory directory_name where scripts directory is placed. Depend on your system run one of the existing file in oreder to enter virtual environment.
5) Install psycopg2 and Django via pip.
6) Run server by command `python manage.py runserver`
