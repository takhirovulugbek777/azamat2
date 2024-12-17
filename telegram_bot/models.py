from django.db import models


# Create your models here.
class TelegramUser(models.Model):
    user_id = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
