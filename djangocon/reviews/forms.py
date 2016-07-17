from django import forms
from .models import Review
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ('story', 'text', 'stars_overall', 'stars_story', 'stars_characters', 'stars_relevance',)


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')