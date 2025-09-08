from django.db.models import TextChoices


class Theme(TextChoices):
    DARK = 'dark', 'Dark',
    LIGHT = 'light', 'Light'
