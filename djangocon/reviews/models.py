from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Review(models.Model):
	author = models.ForeignKey('auth.User')
	TITLE_CHOICES = (
		('cinderella', 'Cinderella'),
		('hansel_gretel', 'Hansel & Gretel'),
		('rapunzel', 'Rapunzel'),
		('snow_white', 'Snow White and the Seven Dwarfs'),
		('three_pigs', 'The Three Little Pigs'),
		('twelve_princesses', 'The 12 Dancing Princesses')
		)
	title = models.CharField(max_length=100, choices=TITLE_CHOICES)
	text = models.TextField()
	stars_overall = models.IntegerField()
	stars_story = models.IntegerField()
	stars_characters = models.IntegerField()
	stars_relevance = models.IntegerField()
	review_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title



