from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=255)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='quiz')

    def __str__(self):
        return self.quiz_name





