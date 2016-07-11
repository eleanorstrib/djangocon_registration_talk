from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	# reviews partials
	url(r'^$', views.all_reviews, name='all_reviews'),
	url(r'^write_review/$', views.write_review, name='write_review'),
]