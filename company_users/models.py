from django.contrib.auth.models import AbstractUser
from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name="Shop Name")
    users = models.ManyToManyField('CustomUser', related_name='shops')  # Ko'p foydalanuvchini bog'lash uchun

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('market_owner', 'Market Owner'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='manager')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Yangi related_name qo'shildi
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Yangi related_name qo'shildi
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return f"{self.username}"
