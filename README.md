FullstackInternTask - Auction and User Management System


Project Overview
This project consists of two microservices:

User Management and Authentication
Auction Management and Bidding
The project is built with Django and is designed to handle user authentication, CRUD operations for users and auctions, and bidding functionality.

Project Structure
auction_management/: Handles auction-related operations including CRUD and bidding.

user_management/: Manages user authentication, registration, and user data.

manage.py: Django's command-line utility for administrative tasks.

.env: Environment variables for configuration.

requirements.txt: Lists all the dependencies for the project.

Folder Structure

AuctionSystem/
├── auctionenv/
├── AuctionSystem/
│   ├── auction_management/
│   │   ├── __pycache__/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── user_management/
│   │   ├── __pycache__/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── generate_secret_key.py
│   ├── manage.py
│   ├── middleware.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── .env
├── .gitignore
├── db.sqlite3
├── requirements.txt
└── README.md


Dependencies
Dependencies are listed in requirements.txt. To install the necessary packages, use:


pip install -r requirements.txt

Setup Instructions
Follow these steps to set up the project:

Clone the Repository:


git clone https://github.com/kazi-azahar-uddin/wasserstoff/FullstackInternTask.git
cd FullstackInternTask
Set Up Virtual Environment:

Create and activate a virtual environment:


python -m venv auctionenv
source auctionenv/bin/activate  # On Windows, use `auctionenv\Scripts\activate`

Install Dependencies:
pip install -r requirements.txt

Run Migrations:
Apply the migrations to set up the database:
python manage.py migrate

Create Superuser:
Create a superuser account for admin access:
python manage.py createsuperuser

Run the Development Server:
Start the development server:
python manage.py runserver


API Endpoints
User Management
User Registration:

POST /api/user/register/
Request body: { "username": "string", "email": "string", "password": "string" }

User Login:

POST /api/user/login/
Request body: { "username": "string", "password": "string" }
Response: { "token": "string" }

Auction Management
Create Auction:

POST /api/auction/auctions/
Request body: { "item_name": "string", "start_time": "datetime", "end_time": "datetime", "start_price": "float" }
Headers: { "Authorization": "Token <admin_token>" }
View All Auctions:

GET /api/auction/auctions/
Update Auction:

PUT /api/auction/auctions/{id}/
Request body: { "item_name": "string", "start_time": "datetime", "end_time": "datetime", "start_price": "float", "highest_bid": "float", "winner": "user_id" }
Headers: { "Authorization": "Token <admin_token>" }

Delete Auction:

DELETE /api/auction/auctions/{id}/
Headers: { "Authorization": "Token <admin_token>" }

Bidding
Place a Bid:
POST /api/auction/auctions/{id}/bid/
Request body: { "amount": "float" }
Headers: { "Authorization": "Token <user_token>" }


Postman Collection
A Postman collection with all API endpoints is provided. You can import it to test the API endpoints.

Download Postman Collection

License
This project is licensed under the MIT License.


