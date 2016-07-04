from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Workshop(models.Model):
	WORKSHOP_CHOICES = (
		('cinderella', 'Cinderella'),
		('goldilocks', 'Goldilocks & the Three Bears'),
		('hansel_gretel', 'Hanzel and Gretel'),
		('snow_white', 'Snow White and the Seven Dwarves'),
		('three_pigs', 'The Three Little Pigs')
		)
	title = models.CharField(max_length=100, choices=WORKSHOP_CHOICES)
	description = models.TextField()
	time_and_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title


class Review(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.ForeignKey(Workshop)
	text = models.TextField()
	stars_overall = models.IntegerField()
	stars_speaker = models.IntegerField()
	stars_content = models.IntegerField()
	stars_relevance = models.IntegerField()
	review_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title



