# Django Restaurant Voting System
This is a Django web application that provides an API that helps employees to make a decision at the lunch place.

## API Functionality

Authentication

Creating a restaurant

Uploading a menu for a restaurant

Creating an employee

Getting the current day's menu

Getting the results for the current day's voting

## Installation
This application requires Docker and Docker Compose to be installed.

Clone the repository:
`git clone https://github.com/viannik/apiMenuVote.git`

Build and run the Docker container:
`docker-compose up --build`

This will start the Django server at http://localhost:8000.

## API Endpoints
/admin/: Django admin page

/api/token/: API endpoint for obtaining authentication tokens

/api/token/refresh/: API endpoint for refreshing authentication tokens

/api/restaurants/: API endpoint for creating a new restaurant

/api/restaurants/<int:restaurant_id>/results/: API endpoint for getting the results of the current day's voting for a menu

/api/menus/: API endpoint for uploading a menu for a restaurant for a specific date

/api/menus/<int:restaurant_id>/: API endpoint for getting the current day's menu for a restaurant

/api/employees/: API endpoint for creating a new employee

/api/votes/: API endpoint for employees to vote for a menu
