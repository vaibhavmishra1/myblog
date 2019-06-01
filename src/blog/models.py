from django.contrib.auth.models import User
from django.db import models
class Blog(models.Model):
	owner = models.ForeignKey(User, editable=False,on_delete='DO_NOTHING')
	title = models.CharField(max_length=500)
	slug = models.CharField(max_length=500, editable=False)

class BlogPost(models.Model):
	shared_to = models.ManyToManyField(Blog, related_name='shared_posts')
	blog = models.ForeignKey(Blog,on_delete='DO_NOTHING')
	title = models.CharField(max_length=500)
	body = models.TextField()
	is_published = models.BooleanField(default=False)
	slug = models.SlugField(max_length=500, editable=False)