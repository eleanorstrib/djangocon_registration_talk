from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.all_reviews, name='all_reviews'),
	url(r'^write_review/$', views.write_review, name='write_review'),
]