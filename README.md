## Assignment 3

This assignment is an implementation of Cash Register using Django framework.
Users can simulate scanning products by inputting the barcode in the textbox.

### Architecture overview

In this architecture (MTV), the model contains two main classes: Product and
Cart. Product is responsible to hold all the products registered, including the
product name, code and price. Cart holds the current session when the cash
register starts scanning. Note that this class also includes the logic to
calculate the total amount, which is passed to the views, therefore meeting one
of the architecture's requirement.

## Installation

1. Clone the repository
2. Run the migrations:
`python manage.py migrate`
3. Populate the database
`python populate.py`
4. Run the django server
`python manage.py runserver`

## Screenshots & Demonstration

### Populating the database


### Scanning a product


### Removing a product


### Group members

| Name  | Student number |
| ------------- | ------------- |
| Rui David  | 100806022  |
| Jacky Chuk Han Lee  | 100787870  |
| Jason Stuckless | 100248154 |
