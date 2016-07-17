from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Review
from .forms import ReviewForm, UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse


def all_reviews(request):
	reviews = Review.objects.filter(review_date__lte=timezone.now()).order_by('review_date')
	return render(request, 'reviews/all_reviews.html', {'reviews': reviews})


def write_review(request):
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid:
			review = form.save(commit=False)
			review.author = request.user
			review.review_date = timezone.now()
			review.save()
			return redirect('write_review')
	else:
		form = ReviewForm()
	return render(request, 'reviews/write_review.html', {'form': form})


	