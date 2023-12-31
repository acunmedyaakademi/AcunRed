from django.db import models

# Create your models here.

class Post(models.Model):
    post_text = models.CharField(max_length=200)
    pub_date =  models.DateTimeField("date published")
    def __str__(self):
        return self.post_text

class Choice(models.Model):
    question = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class Comment(models.Model):
    question = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
