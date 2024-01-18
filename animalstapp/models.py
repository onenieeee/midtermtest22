from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Provide unique related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
        help_text='Specific permissions for this user.',
    )


class Animals(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gene = models.CharField(max_length=100)
    image = models.ImageField(upload_to='animal_images/', null=True, blank=True)

    class Meta:
        app_label = 'animalstapp'

    def __str__(self):
        return self.name
