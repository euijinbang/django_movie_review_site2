from django.shortcuts import redirect, render
from community.forms import CommentForm, ReviewForm
from community.models import Comment, Review
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews,
    }
    return render(request, 'community/index.html', context)

@login_required
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
        return redirect('community:index')
    else:
        form = ReviewForm()
    context = {
        'form' : form,
    }

    return render(request, 'community/create.html', context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    # 오오오오
    form = CommentForm()
    context = {
        'review' : review,
        'form' : form,
    }
    return render(request, 'community/detail.html', context)

@require_POST
def create_comment(request, pk):
    # if request.user.is_authenticated:
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.review_id = pk
        comment.save()

        return redirect('community:detail', pk)

def likes(request, pk):
    user = request.user
    review = Review.objects.get(pk=pk)
    # 유저가 Likeuser 안에 있으면 unlike, 없으면 like
    if user in review.like_users.all():
        review.like_users.remove(user)
    else:
        review.like_users.add(user)

    return redirect('community:detail', pk)
        

