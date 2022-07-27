## CONTENTS OF THIS FILE

-   Introduction
-   Requirements
-   Recommended modules
-   Installation
-   Configuration
-   Troubleshooting
-   FAQ
-   Maintainers

## INTRODUCTION

This repository provides a Python script to update a Postgres table with the information retrieved from
the dataset described in this website:
https://analisi.transparenciacatalunya.cat/es/Salut/Vacunaci-per-al-COVID-19-dosis-administrades-per-m/irki-p3c7

The postgres table contains a row for each unique combination of comarca, number of first vaccine doses that
were delivered and the date of the delivery.

In the main.py script, a request is made to the provided endpoint to get all available results for the ongoing week (dataset is updated weekly). Each request made to the given endpoint is prefiltered to restrict the fields provided by the endpoint and to limit available results. Once the queryset is obtained, duplicates values coming from the request are removed, values are formatted and each item is validated against the database to avoid duplicate entries before final insert.

settings.py provides all config variables and basic settings.

models.py and database.py contain model definition and base class to work with the database.

api.py contains all helper functions related to the API Client

create_db is a script to create model related tables in the database. An optional parameter (--reset) can be provided as command line argument to reset all tables.

To test this repo an example file is provided. These example.py contains an EXAMPLE_DATE variable to recreate all steps contained in the main.py file for a given date in the past, since this database is updated weekly.

Both main.py and example.py accept an optional --limit command line argument to limit results coming from the api call

## REQUIREMENTS

This Project main requirements are:

-   Python 3.9.13
-   [Database ORM] SQLAlchemy (https://www.sqlalchemy.org/)
-   [API Client] Soda Library (https://dev.socrata.com/)

To work with the dataset an APP Token must be created for authentication according to the following docs:
https://dev.socrata.com/foundry/analisi.transparenciacatalunya.cat/irki-p3c7

---

## CONFIGURATION

-   Create APP password to use proper authentication

-   Setup Postgresql database.

    -   Docker compose file is provided with optional values, these values should match those contained in the environment file

    -   Pgadmin is also configured in the docker compose as a tool to visualize changes in postgres.

-   Create .env file. Fields expected by the settings file are

    -   HOST
    -   POSTGRES_USER
    -   POSTGRES_PASSWORD
    -   POSTGRES_DB
    -   APP_TOKEN
    -   APP_USERNAME
    -   APP_PASSWORD

-   Create database tables by running: python create_db.py

-   Run python main.py or python example.py

## ADDITIONAL INFORMATION

A record.log file is created in the working directory to store results coming from all events as well as exceptions
