from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import path, reverse
from django.core.validators import MinLengthValidator

# Create your database models below.

content_validator = MinLengthValidator(limit_value=20, message="Content should be at least 20 characters")


class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(validators=[content_validator])
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # with the function below, it helps to create a unique url 
    # for a specific webpage using the primary key of the value
    def get_absolute_url(self):
        return reverse ("blog_detail", kwargs={'pk': self.pk})

    class Meta: # this is used to order the list of blog post according to cetain value passed in the list below
        ordering = ['-date_published']