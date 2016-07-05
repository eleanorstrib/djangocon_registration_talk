from django.shortcuts import render

def all_reviews(request):
	return render(request, 'reviews/all_reviews.html', {})