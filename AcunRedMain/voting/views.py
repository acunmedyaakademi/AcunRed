from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Choice
from django.http import Http404

# Create your views here.
def index(request):
    return HttpResponse("Hello world")


def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("post does not exist")
    return render(request, "voting/detail.html", {"post": post})

def results(request, post_id):
    response = "You're looking at the results of post %s."
    return HttpResponse(response % post_id)


def vote(request, post_id):
    return HttpResponse("You're voting on post %s." % post_id)