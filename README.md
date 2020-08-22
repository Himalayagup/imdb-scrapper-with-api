# imdb-scrapper-with-api
Scrappimg IMDB and storing the data in Database also with APIs


-> This projects scrappes the IMDb Website's movie listing and store them in local database(SQLite3).
-> It accepts any url of IMDb such as (https://www.imdb.com/chart/top/)
-> It is necessary to provide ```http://``` or ```https://``` in the url


(To view APIs token authentication is required)

API VIEWS

-> To scrap any URL go to: ```localhost/movie/addmovies/```
-> To check the existing movie list go to: ```localhost/movie/api/```
-> To check the existing movie details/or to update go to: ```localhost/movie/api/detail/<id>```
-> To check the wishlisted movies go to: ```localhost/movie/wishlist/api/```
-> To check the update the wishlisted movie go to: ```localhost/movie/wishlist/api/detail/<id>```

User View

This website is user friendly;
User can create accounts and login
-> homepage: ```localhost/```
-> movie list: ```localhost/movie/list```
-> wish list: ```localhost/movie/wishlist``` (login required)
-> Signup: ```localhost/accounts/signup```
-> Login: ```localhost/accounts/login```
Firstly Create the Virtual enviornment

```
1.virtualenv -p python3 env
2.source env/bin/activate
3.cd movie
4.pip install -r requirement.txt
5.python manage.py runserver
```

Then makemigrations are required:

 --> $ python manage.py makemigrations
 --> $ python manage.py migrate

 Now run server by

 --> $ python manage.py runserver

if the local IP address shows refused to connect --> $ python manage.py runserver 127.0.0.1:8000
