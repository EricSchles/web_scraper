# Web Scraper

## Doing Migrations

Doing migrations with Flask-Migrate and SQLITE are a little bit weird.

First you need to move database.db to the top level (same level as manage.py) then you can run:

`python manage.py db migrate`

Flask-Migrate will detect the changes to your app.models (which is good) without having to write a migration from scratch

However it doesn't detect the location of your database, for some reason? 

In any case, then run - `python manage db upgrade`

And then move database.db back down (otherwise your models won't know where your db went)
