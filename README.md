# GraphQL Hello World

A simple Hello World project for learning about GraphQL.

Based on the Very Academy "[GraphQL](https://www.youtube.com/watch?v=kP7wQoFXUSc&list=PLOLrQ9Pn6caxz00JcLeOR-Rtq0Yi01oBH)" tourorial.

# Setup

## Prerequisites

Python must be installed to complete setup.

## Virtual Environment

Using a virutal environment is recommended.

`python -m venv venv`

`venv\Scripts\activate`

## Installation

The required packages are in the [requirements.txt](requirements.txt) file.

`pip install -r requirements.txt`

# Running the Program

1. Navigate to the directory with [manage.py](manage.py).
2. Activate the virtual environment (if applicable).
3. Migrate and run the sever.

    `python manage.py migrate`

    `python manage.py runserver`

4. From a web browser, open [localhost:8000/books](http://localhost:8000/books), [localhost:8000/quiz](http://localhost:8000/quiz), or [localhost:8000/users](http://localhost:8000/users).
