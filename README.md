# emmanuel_jr
Project Innovate - Emmanuel Jr.

## Description
A navigation robot controlled through a website on Django framework

## Getting started

1. Clone the repository

```
git clone https://github.com/Geniools/emmanuel_jr
```

 2. Inside the website directory (website/website), add the following file: 

*db_credentials.py*

And then add the following code to the file:

 ```
DB_PASS = ""
DB_USER = "root"
DB_HOST = "localhost"
DB_NAME = "emmanuel_jr_database"
DB_PORT = 3306
```
(Note: change the credentials to your own)

3. Run the website using the following command (inside the website directory):

```
python manage.py runserver PORT
```
(Note: PORT is optional)

