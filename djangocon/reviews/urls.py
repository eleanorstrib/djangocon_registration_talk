from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	# templates
	url(r'^$', views.all_reviews, name='all_reviews'),
	url(r'^write_review/$', views.write_review, name='write_review'),
	
	## registration
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('registration.backends.default.urls')),
]