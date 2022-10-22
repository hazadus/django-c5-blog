from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(
        to="auth.User",  # Reference built-in User model
        on_delete=models.CASCADE,  # Delete all the stuff if user is deleted?
    )  # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.CASCADE
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Used in tests to check if the absolute URL is correct.
        """
        return reverse('view_post', kwargs={'pk': self.pk})
