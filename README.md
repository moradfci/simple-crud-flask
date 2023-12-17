# Simple CRUD With Flask

Description or introduction to your project.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Tests](#tests)


## Overview

This is simple CRUD operation using flask and dict as in-memory data structure.



## Installation

### Prerequisites

- no prerequisites are needed

### Steps

1. Clone the repository: `git clone https://github.com/moradfci/simple-crud-flask.git`
2. Install dependencies: `pip install -r requirements.txt`


## Usage

cd project\directory

flask run

open Postman

to create product use http method POST
http://127.0.0.1:5000/products
add this to body (you can change values as you want)
{
   
    "name":"product 1",
    "description":"text",
    "price":125.6

}

to read all product use http method GET
http://127.0.0.1:5000/products

to read specific product use http method GET
http://127.0.0.1:5000/products/<product_id>

to update specific product use http method PUT or PATCH
http://127.0.0.1:5000/products/<product_id>
the body should looks like 

{ 
    "name":"product updated",
    "description":"text",
    "price":10

}
it could only one value or multiple 

to delete specific product use http method DELETE
http://127.0.0.1:5000/products/<product_id>

## Tests

Instructions on how to run tests:

```bash
cd project\directory
pytest test/test_api.py