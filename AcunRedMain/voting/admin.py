from django.contrib import admin

# Register your models here.
from .models import Post, Choice

admin.site.register(Post)
admin.site.register(Choice)