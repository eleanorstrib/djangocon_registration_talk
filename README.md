This repo is an accompaniment to a presentation at DjangoCon USA 2016, called "Sign Me Up: Choosing & using a registration package for your Django project".   It was given in Philadelphia, PA on July 18, 2016.

You can view the [slide deck in Keynote](https://drive.google.com/file/d/0B1A8in1PFh3idEV3OUVfWk1lTDA/view?usp=sharing) or [video](https://youtu.be/WHEjVBTBXcA) alone, or along with the description below.

###Intended audience
This talk was designed with the novice Django user in mind (some basic familiarity, has completed a tutorial or done a small project) but it could be useful for anyone who has not set up user registration for a site before.

If you have any questions, or see any errors in this repo, please open an issue or email me.


###Tech
This repo uses the following languages, frameworks & libraries:
* Python 3
* Django 1.9
* django-registration-redux 1.4
* Bootstrap
* Google Fonts
I use a Mac so all of the directions are written from that perspective (sorry, Windows users!).

###Getting started with this repo

While this talk was inspired by stuggles I had with a side project of mine called [valeez](http://www.valeez.com):baggage_claim:, the example is a very simple Django app called _Fairy Tale Reviews_:european_castle: (inspired by my four year old) where people can leave a review of one of six stories.  _Fairy Tale Reviews_ has a very simple data model, a single form, and some minimal styling; after all, we're here to focus on registration!


###Overview

Registration is a common component of most web applications, so knowing how to implement it is a useful skill.  After working through the process for a personal project in 2015 (available at valeez.com), I submitted this talk to DjangoCon in order to share:
* Criteria and resources for choosing a registration package
* How the pieces of a registration package fit into the Django framework
* Some ‘gotchas’ that aren’t clear in or absent from documentation


###Choosing a registration package

This repo and tutorial use django-registration-redux, but there are many other options out there! 

Some key considerations are:

* _Matching product requirements_: To pick the right tools, you need to know what your end goals are.  Do your requirements call for social media login? OAuth? Email validation?  Sounds obvious, but this is an often overlooked step.  Addressing those now and understanding the benefits and limitations of your choice will save you headaches down the road, I promise!

* _Compatibility_: Keep in mind you may need to upgrade your version of Django (for example) to use a package, or certain packages may not be compatible with newer versions (probably not a great sign...).  I advocate using the latest stable release of software for an application that will be available to real users.  

* _Maintenance & Usage_: As a rule of thumb, good maintenance and a decent user base go hand in hand.  Maybe you'll find an undiscovered gem, feel like experimenting, etc. but if you need things to be reliable, I recommend sticking with the tried and true.

* _Quality of documentation and tutorials_: Good documentation is important.  If the official write ups for the package you want to use are confusing, look for online tutorials (I'm a big fan of YouTube), Stack Overflow Q&As, meetups or other gatherings where you might find people who can help you.  If there's a derth of information, and the package creators aren't responsive, might be better to choose something else.

I love the site http://djangopackages.com to evaluate my options, even if it doesn't answer all of your questions, it's a great starting point.

Now, let's get to the nitty gritty.

###Fitting django-registration-redux in the django framework
If you've already cloned the repo, you have some project files, but if not, this will walk you through what to create.

Start by creating a project and an app.  If you need help with this, I highly recommend the Django Girls tutorial. 

Then if you go into your top-level project folder, you should see: 
* manage.py file
* Database 
* App folder (`reviews` in this example)
* Project folder (`djangocon` in this example)
![django framework illustration](/django_framework_overview.png?raw=true)

First, an overview of what we'll need to do here to add user registration.

###Things to add
Here are the files and folders that we need to add in the app folder (again, that's `reviews` in this example).

* _forms.py file_: We'll use this to create a user registration form, based on Django's built in User model, which you can learn about here: 
https://docs.djangoproject.com/en/1.9/ref/contrib/auth/#django.contrib.auth.models.User

* _templates folder_: This will hold all of your templates.  In most cases, these are the HTML files that display between your navigation bar and footer (if you have one).  If you have an app that displays some views in the browser, you've already done this.

Inside the `templates` folder, you should have:
* _base.html_: This is what the templates will extend (a fancy way of saying display under/inside of)

* _Application templates folder (`reviews` in this example)_: This folder holds all of the application templates that are not part of the registration flow.  Again, if you have an app that displays some views in the browser, you've already got this.

*_`registration` folder_: This is where you will put all of the templates you'll need for the registration flow, for registering, logging in and out, resetting a password.  More on those in a minute.

####Files that will be modified
In addition to the files and folders listed above, we will need to make changes to two files in the project folder:

* _settings.py_: Add the registration app and some settings to control its behavior, from the login page we show to how we deliver account verification messages.

* _urls.py_: Code to point Django to the registration templates.

That's it!  

Now that we have an overview of what's going on, let's get coding.

##Making it work
**Step 0: Install in venv & update requirements**

I'm going to use `pip` a bunch here.  In your virtual environment, in your root, type `pip install django-registration-redux'.  And it's installed! Magical. :tada:

Next, you want to update your requirements.txt file by typing `pip freeze > requirements.txt'.  If you don't already have a requirements file, it's a good idea to create one in case you or someone else wants to clone and run your project on another machine.

**Step 1: Create a form for the User in forms.py**

You need to make a form for the user to add their data.  Fortunately, we can leverage the [Django User model](https://docs.djangoproject.com/en/1.9/ref/contrib/auth/#django.contrib.auth.models.User) to accomplish this.

The only two fields that are _required_ are username and password, but if you want to have a step where the user validates their account with an email link, you should have email in there as well.  First and last name are built in, and you can extend the User model to add more fields, although that's beyond the scope of this talk.

Head on over to your `forms.py` and add/make sure you have these lines of code:
```
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
```
For the fields variable, add the built in attributes of the User model that you want to include, per the documentation.

**Step 2: Install the app in settings.py, migrate**

Head over to your `settings.py` file and add `'registration',` to the list in the `INSTALLED_APPS` variable.

At this point, you should make sure that you have `'django.contrib.auth',` and `'django.contrib.sites',`
in that list as well.  In the slides and the documentation for this package, there are other variables you can set that are really important for user experience, like how long the authorization link is valid for, if they are automatically signed in when they enroll, etc.  You could definitely set `LOGIN_URL = 'accounts/login/'` and the `LOGIN_REDIRECT_URL` to the path that you want.

**Step 3: Get the registration templates**

You can write all of these yourself, but why do that when a nice person has already done it for us!  Visit [this repo](https://github.com/macdhuibh/django-registration-templates) where you can download the whole set!  Add this to the `registration` folder in the `templates` folder.

**Step 4: Add the url pattern to the urls.py that's NOT in your app**

In the `urlpatterns` list, add this line, to tell django to use the registration urls: `url(r'^accounts/', include('registration.backends.default.urls')),`.  This instructs Django to use the 'standard' registration urls, so you don't need to add one for each template individually, which is a big headache.

That's it -- _almost_!  Here are a couple of other things you might want to do that tripped me up :scream: -- don't let it happen to you. 


##Pitfalls
These two issues are documented, but I had a hard time tracking down these problems.

**Issue #1: Custom registration templates did not show up!**

This was one of the more frustrating problems I had -- I made beautiful customizations on my registration templates and none of them showed up.  

To fix this, you need to be sure that the 'registration' app shows up in the `settings.py` file in the `INSTALLED_APPS` list before `'django.contrib.admin', and your app before that.  


**Issue #2: Errors when trying to test the email on my local machine**
Before you've set up an email server, Django knows it must send an email, but doesn't know where to send it.  

Before you have all of that set up, you can test that the email verification works by printing it into the console.  This requires a single line of code in your `settings.py`: `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`.  Easy, right??

Two caveats: 

1. You need to set your SITE_ID variable, either by opening the shell (`python manage.py shell`) and instantiating a class, like so:
'''
from django.contrib.sites.models import Site
Site.objects.create(name='localhost:8000', domain='localhost:8000')
'''

I show `localhost:8000` because this is the easiest way to check locally (substituting whatever port you use for the 8000 if applicable) -- you would definitely want to update this in the shell or the admin panel before putting it in production.

2. Remember to update your `EMAIL_BACKEND` variable before you test with an email server.  This is easy to forget, but will cause errors if you set the rest of the variables needed in your `settings.py`.  You will need to change `console` to `smtp` in most cases.


***THATS IT!*** Thanks for reading, and please don't hesitate to contact me if you have any questions or suggestions about this tutorial.  :snake:



