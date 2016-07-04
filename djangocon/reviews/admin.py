from django.contrib import admin
from .models import Review, Workshop

all_models = [Review, Workshop]
admin.site.register(all_models)
