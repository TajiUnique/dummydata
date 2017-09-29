
 ![travis build pass](https://travis-ci.org/joewachira/Shoppinglist.svg?branch=deploy2) 
[![Test Coverage](https://codeclimate.com/github/codeclimate/codeclimate/badges/coverage.svg)](https://codeclimate.com/github/codeclimate/codeclimate/coverage)

## Shoppinglist
Simple shopping list for personal use. Create a virtual enviroment `virtualenv --python=python3 env` then activate it `source env/bin/activate`

The innovative shopping list app is a web based application that allows users  to record and share things they want to spend money on  meeting the needs of keeping track of their shopping lists.

## Getting Started
- Python 3.6.2 installation
- Git installation

## Usage
> 1. Clone this repo :https://github.com/joewachira/Shoppinglist/tree/deploy2
> 2. Create a virtual enviroment `virtualenv --python=python3 env` then activate it `source env/bin/activate`
> 3. Install requirements `pip3 install -r requirements.txt`

## Running the Tests

 To run unittests locally, install nose then point it to the tests folder located at tests folder of the project

 nosetests tests
 
 
## Flask Application

The file app.py is used to run the flask application. To run it use

    python run.py  
    
it will run a local webserver on http://127.0.0.1:5000 and user will be provided with a home page

## Deployment

Running the app requires you to just visit the url  https://shoplapp.herokuapp.com/register

## Build With
- Flask- The web framework used
- Flask-WTF- extension that wraps the project.

## Acknowledgement
The following people have contributed to the concept/code:

- Mbithe Nzomo
- Jee Gikera
- Linnnette Wanjiru
- Ann Mukundi

