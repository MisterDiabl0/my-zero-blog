from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #статья по теме Мамочки
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # redact
    # watching = models.                            #сколько просмотрело?
    # image = models.
    # video = models.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class Page(models.Model):
#     pass
# class Comment(models.Model):
#     author =
#     title = models.CharField(max_length=200)
#     text = models.TextField()
