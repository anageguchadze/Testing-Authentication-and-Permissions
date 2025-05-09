# Testing-Authentication-and-Permissions

This project demonstrates how to implement authentication and permissions using JWT (JSON Web Token) in a Django REST Framework (DRF) application. The project includes endpoints protected by JWT authentication and tests to ensure proper functionality of authentication and permission settings.

Table of Contents
Prerequisites

Installation

Setup

API Endpoints

Testing

Notes

Prerequisites
Before setting up this project, ensure you have the following installed:

Python 3.x

Django 3.x+

Django REST Framework (DRF)

djangorestframework-simplejwt for JWT authentication

Installation

Clone the repository:
git clone https://github.com/anageguchadze/Testing-Authentication-and-Permissions.git
cd Testing-Authentication-and-Permissions

Create a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run migrations to set up the database:
python manage.py migrate
Setup

Add JWT Authentication:

In your settings.py, add the following configuration to enable JWT authentication.

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

Add URLs for JWT authentication:
In your urls.py file, make sure to include the JWT token endpoints for obtaining and refreshing the token.

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

API Endpoints
1. /api/private-items/ [Protected Endpoint]
Method: GET

Description: This endpoint returns a list of private items created by the authenticated user.

Authentication: Required. Users must provide a valid JWT token in the Authorization header.

Permissions: Only authenticated users can access this endpoint.

2. /api/token/ [Obtain Token]
Method: POST

Description: Users can obtain a JWT token by providing their username and password.

Request Data:
{
  "username": "your_username",
  "password": "your_password"
}

3. /api/token/refresh/ [Refresh Token]
Method: POST

Description: Users can refresh their JWT token using a valid refresh token.

Testing
Run Tests
This project includes tests to verify that the authentication and permissions work correctly. To run the tests, use the following command:

python manage.py test
Test Scenarios

Unauthenticated Access:

A request to /api/private-items/ without a JWT token will return 401 Unauthorized.

This test ensures that only authenticated users can access the private items.

Authenticated Access:

A request to /api/private-items/ with a valid JWT token will return 200 OK.

This test verifies that an authenticated user can access their private items.

Notes
JWT Token: After logging in (using /api/token/), a user receives an access token that must be included in the Authorization header as Bearer <token>.

Permissions: Only authenticated users are allowed to access the /api/private-items/ endpoint. If a user is not authenticated, they will receive a 401 Unauthorized error.

Owner Field: The PrivateItem model includes a foreign key to the User model, ensuring that each item belongs to a specific user. Only the user who created an item can access it.