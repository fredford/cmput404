# authentication-lab

University of Alberta, CMPUT 404 Lab 9 starter repository. Use the different
HTTP authentication schemes provided in Django Rest Framework.

## Getting Started

1. Clone this repository.
   - `git clone https://github.com/uofa-cmput404/authentication-lab.git`
2. Change directory into this repository.
   - `cd authentication-lab`
3. Initialize a Python3 virtual environment
   - `virtualenv venv --python=python3`
4. Activate the virtual environment and install the application dependencies
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```
5. Run the migrations and create a superuser.
   ```bash
   ./manage.py migrate
   ./manage.py createsuperuser
   ```
6. Start the Django application.
   `./manage.py runserver`

## Questions

### Question 0

https://github.com/fredford/authentication-lab

### Question 1

The "session authentication" is the default used for Django Rest Framework's browsable API.

### Question 2

Httpie uses "basic authentication" passing username:password creditials in the request.

### Question 3

Session authentication utilizes cookies to store session information regarding the users's verification, while Token authentication requires tokens to be passed for authenticated user requests.

### Question 4

When something like "Log in with Google" is pressed, a user authorization request is made from the application to Google, if the user is authenticated an authorization code is sent to the user and an access token request is made, this access token is granted if the user is authenticated.
