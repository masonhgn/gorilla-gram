from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    caption = models.TextField(max_length = 100)
    image = models.ImageField(upload_to='user_posts/', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return str(self.author) + ": " + self.caption

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])