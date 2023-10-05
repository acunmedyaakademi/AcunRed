from django.urls import path
from . import views
from django.contrib.auth.urls import views as auth_views

app_name = "votings"
urlpatterns = [
    path("",views.index,name="index"),
    path("<int:post_id>",views.detail,name="detail"),
    path("<int:post_id>/results",views.results,name="results"),
    path("<int:post_id>/vote",views.vote,name="vote"),
    path("<int:post_id>/comment",views.comment,name="comment"),
    path("<int:post_id>/comment/<str:comment_text>",views.add_comment,name="comment"),
    path("login",views.login_view,name="login_view")
]