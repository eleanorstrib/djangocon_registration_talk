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


def register(request):
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)

		if user_form.is_valid:
			user = user_form.save()
			user.save()

			registered = True

	else:
		user_form = UserForm()


	return render_to_response(
            'registration/registration_form.html', {'user_form': user_form})


	