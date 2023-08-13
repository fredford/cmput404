# CMPUT404 CGI Experiments

Fraser Redford

Experimenting with CGI server stuff!

## Question 1

> How do you inspect all environment variables in Python?

Using `os.environ` you can see all python environment variables.

## Question 2

> What environment variable contains the query parameter data?

The variable `QUERY_STRING` contains query parameter data when it is being passed.

## Question 3

> What environment variable contains information about the user's browser?

The variable `HTTP_USER_AGENT` contains the related information about the users browser.

## Question 4

> How does the POSTed data come to the CGI script?

Using the class `FieldStorage` to store posted data fields for retrieval.

## Question 5

> What is the HTTP header syntax to set a cookie from the server?

The header syntax for setting a cookie is `Set-Cookie: key=value`

## Question 6

> What is the HTTP header syntax the browser uses to send the cookie back?

The header syntax for sending the cookie back is `Cookie: key=value`

## Question 7

> In your own words, what are cookies used for?

Cookies are a way of storing key-value pairs for easy information storage and retrieval. Allowing a webpage to easily implement variables that will represent cookie information.

