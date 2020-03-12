import pendulum
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField


def user_path(instance, file_name):
    today = pendulum.today()
    return "audio/user_{}/{}-{}-{}/{}".format(
        instance.user.id, today.day, today.month, today.year, file_name
    )


class Krankaoke(models.Model):
    artist = models.CharField(blank=False, max_length=128)
    title = models.CharField(blank=False, max_length=128)
    audio = models.FileField(upload_to=user_path, blank=False)
    timings = JSONField(blank=True, null=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "< artist: {} title: {} >".format(self.artist, self.title)
