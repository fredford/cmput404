# CMPUT 404 - Lab 1

Fraser Redford

1245580

## Question 1

> What is your GitHub URL?

GitHub URL: https://github.com/fredford

Lab URL: https://github.com/fredford/cmput404_lab1

## Question 2

> What version is the requests library installed on the system?

Requests version 2.25.1 is installed.

## Question 3

> What version is the requests library installed in the virtualenv?

Requests version 2.25.1 is installed.

## Question 4

> What is the difference between the virtual environment and the not virtual environment python?

The versions are the same as both installed the same version from pip just into different environments.

## Question 5

> What status code is returned for http://google.com? What URL must you visit to get a 200 status code?

Using the command:

```bash
$ curl -i http://google.com/
```

Returns the error message `301 Moved Permanently`, stating the location of `http://www.google.com/`.

```bash
$ curl -i http://www.google.com/
```

Returns a valid status code of `200 OK`.

## Question 6

> What status code is returned for http://google.com/teapot? Is it the one returned by curl -i or curl -iL? What happens when you curl http://www.google.com/teapot?

Status code `301 Moved Permanently` is returned from the input URL of http://google.com/teapot and status code `418 I'm a Teapot` is returned from the input URL of http://www.google.com/teapot.

## Question 7

> What changed in the output of https://webdocs.cs.ualberta.ca/~hindle1/1.py when you used -X POST? What is this method useful for?

In the comparison between the two curl outputs, several new form field instances were added or changed. This could allow for making a POST request to send data.

## Question 8

> What is the raw URL to your Python script on GitHub?

https://raw.githubusercontent.com/fredford/cmput404_lab1/master/script.py