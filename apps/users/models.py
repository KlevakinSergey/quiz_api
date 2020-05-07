from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    QUIZ_AUTHOR = 'Quiz author'
    PLAYER = 'Player'

    ROLE_OF_USER_CHOICES = (
        (QUIZ_AUTHOR, 'Quiz author'),
        (PLAYER, 'Player'),
    )
    role = models.CharField(max_length=15, choices=ROLE_OF_USER_CHOICES, default=False)

    def __str__(self):
        return f'{self.username}'





