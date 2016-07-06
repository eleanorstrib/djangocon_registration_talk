from django.shortcuts import render
from .models import Review
from django.utils import timezone

def all_reviews(request):
	reviews = Review.objects.filter(review_date__lte=timezone.now()).order_by('review_date')
	return render(request, 'reviews/all_reviews.html', {'reviews': reviews})


def write_review(request):
	return render(request, 'reviews/write_review.html', {})