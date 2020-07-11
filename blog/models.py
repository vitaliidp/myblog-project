from django.db import models

# Create your models here.
class Blog(models.Model):
	blog_title = models.CharField(max_length = 150)
	blog_date = models.DateTimeField(auto_now = True)
	blog_text = models.TextField(max_length = 10000)
	blog_image = models.ImageField(upload_to = 'blog_images/')