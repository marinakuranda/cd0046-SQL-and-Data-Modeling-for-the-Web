# Fyyur

This is the project made as a part of [Full Stack Web Developer](https://learn.udacity.com/nanodegrees/nd0044) on Udacity.

## Prerequisites

Python 3
PosstgressDB

## Running locally

´´´bash
# Istall dependencies
pip install -r requirements.txt

# Activate the environment
source ./myenv/bin/activate

# Run the app
python3 app.py
´´´

## Database Migration

# create migration when anythin changed in the model
flask db migrate

# apply the latest migration to the Database
flask db upgrade

## Inspiration

- https://github.com/reemkhd/Fyyur/blob/master/app.py