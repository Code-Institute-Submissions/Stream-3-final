# Stream 3 Final Project

## We Are Social
 
## Overview
 
This is an Python Website Website using the Django Framework
## The Website is Deployed Using Heroku
-[http://johnarnold-stream3.herokuapp.com/] (http://johnarnold-stream3.herokuapp.com/)

##Overview
We Are Social is a fictitious Social Enterprise Website that allows the exchange of ideas that benefit both businesses and society as a whole.  The site is built using a Python Django Framework and features Blogs which allow discussions using disqus, forums which allow the exchange of ideas and discus projects using the forum app, users can also vote on ideas created in the forum.
We are social required a monthly subscription payable using Stripe.
 
### Some the tech used includes:
- [Bootstrap](http://getbootstrap.com/)
    - We use **Bootstrap** to give our project a simple, responsive layout
- [Python] (https://www.python.org/) A powerful and fast Object Oriented Programming Language
- [Python Django] (https://www.djangoproject.com/) A high-level Python Web framework that encourages rapid development and clean, pragmatic design.  The Django Framework is built around the Model View Control architecture.
- [MySQL](https://www.mysql.com/) An Open Source Database Management System.


##Pages in Detail

We Are Social is a collection of Apps, which are packages that provide a set of features.  Apps include a combination of model classes, views, form classes, template tags, static files, URL's and Middleware.
#Home Page
(http://johnarnold-stream3.herokuapp.com/) Offers a vibrant introduction to the website with links into the facilities available to members.

#Register
- (https://johnarnold-stream3.herokuapp.com/register/) Users can Register with We Are Social which requires a monthly subscription fee of £2.
Payments are made using [Stripe](https://stripe.com/] Payment API.  As this website is fictitious, all payments use the test mode.  When attempting to Register, a Card Number of 4242424242424242, CVV of 123 and an expiry date in the future should work sufficiently.
The registration form features a {Captcha Control](https://djangopackages.org/packages/p/django-simple-math-captcha/) which asks a simple Math question.  This is to prevent robots attempting to log in.
#Login
- (https://johnarnold-stream3.herokuapp.com/login/) the login page features a login form in a Bootstrap Modal window.  The page uses JQuery to open the login modal on entering the page.  The login form is submitted via AJAX, so that the modal window does not close upon logging in.  Login success or failure messages are displayed with the modal window.
- If your login is not successful but an account with the supplied email address is supplied, you will receive a link to reset your password.
- (https://johnarnold-stream3.herokuapp.com/resetuser/) [The Change Password and Reset User Account] Page has a form which will send an email to the registered email account, which contains a link to another page to change the login password for that user account. This uses the SMTP service of a Gmail Account.
#Profile
- (https://johnarnold-stream3.herokuapp.com/profile/) - When you register or log in, you are redirected to you profile page.  This has details of you account such as youe email address, when you joined and how long you have on your subscription.
#About We Are Social
(http://johnarnold-stream3.herokuapp.com/pages/about/) Gives an overview of the We Are Social Organisation and what a social enterprise is.  This application uses [Flat Pages] (https://docs.djangoproject.com/en/1.10/ref/contrib/flatpages/) which is HTML content in a database.
#Blog