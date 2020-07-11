from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length = 150)
	date = models.DateTimeField(auto_now = True)
	text = models.TextField(max_length = 10000)
	image = models.ImageField(upload_to = 'blog_images/')