# Smart Chef
Web server for the Smart Chef app. This app can help to select some recipes based on the ingredients user already has.

## Technolages
Our app uses Python powered by django for our backend, html/css with some js for the frontend, and postgreSQL as the database. More information about database configuration you can find in the database folder.
## API
GET `/` - root endpoint that sends main page

GET `/api/recipy` - requires a body with json, that contains array of products,
sends back json with recipies (yeah, GET should not have a body, but I don't care :) )