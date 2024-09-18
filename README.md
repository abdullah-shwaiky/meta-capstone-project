# Capstone Project: Meta Backend Developer
Learner: Mohammad Abdallah Shweiki

## Setup:
1. Clone this repository using [this link](https://github.com/abdullah-shwaiky/meta-capstone-project.git).
2. Use commands like cd to navigate to project folder: `littlelemon/`
3. Run python commands to initialize project environment: 
```bash 
pipenv shell 
pipenv install
```
4. Run migraitons if necessary: `python manage.py makemigrations` and then `python manage.py migrate`.
5. Run the server using `python manage.py runserver`.
6. Run your preferred API testing software: `Insomnia`, `Postman`, or simply the web browser.
7. Create your tester user. See Below for more details.

## Create Tester User:
1. Using your API testing software, navigate to http://127.0.0.1:8000/auth/users/
2. Enter tester credentials. Example: `username: tester1`, `password: This_tester.1`.
In case of using `Postman` or `Insomnia`, include these parameters in the request body as such:
```json
{
  "username": "tester1",
  "password": "This_tester.1"
}
```
4. Get your authentication token after navigating to http://127.0.0.1:8000/auth/users/api-token-auth/ in your API testing software.
Keep your username and password in the request body.
5. Copy your authentication token and place it in the Auth header of the tester. Use `Bearer Token` with prefix `Token`.
6. You are now ready to test endpoint functionality. See below for details.

## Restaurant API Endpoints
There are two main endpoint branches to test: `Menu` and `Booking` endpoints.

### Menu Endpoint:
Navigate to http://127.0.0.1:8000/restaurant/menu/

`GET` operation:
1. Set the request method to `GET` in the API testing software.
2. Press `Send` to see all available menu items.

`POST` operation:
1. Set the request method to `POST` in the API testing software.
2. Fill the request body with the following parameters: `title`, `price`, and `inventory`.
Use the following structure as an example:
```json
{
  "title": "Burger",
  "price": 12.5,
  "inventory": 30
}
```
3. Press `Send` to add this item to the menu. Notice the `201 CREATED` response.

`PUT` operation:
`PUT` Method is not allowed.

`DELETE` operation:
1. Set the request method to `DELETE` in the API testing software.
2. Navigate to http://127.0.0.1:8000/restaurant/menu/{pk:int}/
3. Press `Send` to delete menu item with `id: pk`.
4. The resource is now deleted.

### Booking Endpoint:
Navigate to http://127.0.0.1:8000/restaurant/booking/tables/

`GET` operation:
1. Set the request method to `GET` in the API testing software.
2. Press `Send` to see all available bookings.

`POST` operation:
1. Set the request method to `POST` in the API testing software.
2. Fill the request body with the following parameters: `name`, `no_of_guests`, and `booking_date`.
Use the following structure as an example (replace placeholders):
```json
{
	"name": "Name",
	"no_of_guests": 1,
	"booking_date": "YYYY-MM-DDTHH:MM"
}
```
3. Press `Send` to confirm booking. Notice the `201 CREATED` response.

`PUT` operation:
1. Set the request method to `PUT` in the API testing software.
2. Change the request body data as needed.
Use the following structure as an example (replace placeholders):
```json
{
	"name": "Name",
	"no_of_guests": 1,
	"booking_date": "YYYY-MM-DDTHH:MM"
}
```
3. Press `Send` to confirm booking. Notice the `201 CREATED` response.


`DELETE` operation:
1. Set the request method to `DELETE` in the API testing software.
2. Navigate to http://127.0.0.1:8000/restaurant/booking/tables/{pk:int}/
3. Press `Send` to delete menu item with `id: pk`.
4. The resource is now deleted.

Thank you for reviewing.
