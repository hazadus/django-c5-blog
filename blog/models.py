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
        Used to redirect to individual page after editing post.

        One place Django uses get_absolute_url() is in the admin app. If an object defines this method,
        the object-editing page will have a “View on site” link that will jump you directly to the object’s
        public view, as given by get_absolute_url().

        Used in tests to check if the absolute URL is correct.

        https://docs.djangoproject.com/en/4.1/ref/models/instances/#get-absolute-url
        """
        return reverse('view_post', kwargs={'pk': self.pk})
