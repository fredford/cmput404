# CMPUT 404 Lab 4 - Django

Code for this lab was provided in the lab instruction https://uofa-cmput404.github.io/lab-4-django.html

## Question 1

> What is the link to your Github?

https://github.com/fredford/cmput404-lab4

## Question 2

>  What does the browser show you?

A web page displaying "The install worked successfully! Congratulations!". With a few links to things that can be done with Django.

## Question 3

> After creating the first view within polls, what does the browser show you when navigating to / and to /polls respectively?

The browser displays the text output "Hello, world. You're at the polls index."

## Question 4

> What is a Django migration and why do we need them?

Migrations are how Django manages changes to the database schema while maintaining consistency in the data.

## Question 5

> What do you see when you log into the Django administration site? From a high level, how do you get custom models to appear in the Django admin page?

A `Recent Actions` section of recent actions taken by super users. An `Authentication and Authorization` section of Groups and Users that can be added or changed. As well as a `Polls` section of `Choices` and `Questions` that can be added or changed.

Custom models can be added to the admin page by registering them in the `admin.py` file.

## Question 6

> What do you see what you /polls/38/ in your browser? What about /polls/38/results and /polls/38/vote? What happens when you don’t put a number, and instead use a string? How would you modify the urls.py file to allow arbitrary alphabetic characters?

- In the `/polls/38/` section it displays the readout: `You're looking at a question 38`.
- In the `/polls/38/results` section it displays the readout: `You're looking at the results of question 38`.
- In the `/polls/38/vote` section it displays the readout: `You're voting on question 38.`
- Changing the `path` from `<int:question_id>` to `<str:question_id>`.

## Question 7

> Why is it a bad idea to hardcode urls into the templates?

It takes away the whole point of making a template which is for reusability with a wide variety of url potentials.

## Question 8

> What are the benefits of using Django's generic views over writing views 'the hard way'? When should you use a generic view and when shouldn't you use a generic view?

It allows you to quickly and easily generate generic views without needing to write a lot of HTML. Generic views are not useful when you want a more personalized web page with more detail and information that you're looking display.

