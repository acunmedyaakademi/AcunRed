from django.urls import path
from . import views

app_name = "votings"
urlpatterns = [
    path("",views.index,name="index"),
    path("<int:post_id>",views.detail,name="detail"),
    path("<int:post_id>/results",views.results,name="results"),
    path("<int:post_id>/vote",views.vote,name="vote"),
    path("<int:post_id>/comment",views.comment,name="comment"),
]