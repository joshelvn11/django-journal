from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    content = models.TextField(default='')
    excerpt = models.TextField(max_length=500, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-title"]

    def __str__(self):
        return f"{self.title} | By: {self.author}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default='')
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    challenge = models.FloatField(default=2.3)

    def __str__(self):
       return f"{self.body} | By: {self.author}"