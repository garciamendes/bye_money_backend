from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4
from .constants import Theme
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(TimeStampedModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    uuid = models.UUIDField(unique=True, editable=False,
                            db_index=True, default=uuid4)

    theme = models.CharField(choices=Theme.choices,
                             max_length=10, default=Theme.DARK)

    def __str__(self):
        return self.user.first_name


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
