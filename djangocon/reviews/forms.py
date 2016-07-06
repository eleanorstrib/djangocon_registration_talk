from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ('title', 'text', 'stars_overall', 'stars_story', 'stars_characters', 'stars_relevance',)