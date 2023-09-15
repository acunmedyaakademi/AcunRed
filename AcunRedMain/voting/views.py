from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Choice
from django.http import Http404
from django.template import loader

# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by("-pub_date")[:5]
    template = loader.get_template("voting/index.html")
    context = {
        "latest_post_list": latest_post_list,
    }
    return HttpResponse(template.render(context, request))



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

def comment(request, post_id):
    return HttpResponse("You're commeting on post %s." % post_id)

def add_comment(request, post_id,comment_text):
    return HttpResponse("added comment %s." % comment_text)