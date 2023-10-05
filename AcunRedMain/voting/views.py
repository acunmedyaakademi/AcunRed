from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Choice
from django.http import Http404
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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
    print("----------------------")
    print("----------------------")
    return render(request, "voting/detail.html", {"post": post})

def results(request, post_id):
    response = "You're looking at the results of post %s."
    return HttpResponse(response % post_id)

def vote(request, post_id):
    if not request.user.is_authenticated:
        return HttpResponse("You are not logged in")
    return HttpResponse("You're voting on post %s." % post_id)

@login_required(login_url="/voting/login")
def comment(request, post_id):
    return HttpResponse("You're commeting on post %s." % post_id)

def add_comment(request, post_id,comment_text):
    if not request.user.is_authenticated:
        return HttpResponse("You are not logged in")
    return HttpResponse("added comment %s." % comment_text)

def login_view(request):
    #username = request.POST["jack"]
    #username = "jack"
    #password = "123"
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("success")
    else:
        return HttpResponse('invalid login' )
        