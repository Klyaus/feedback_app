from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Feedback(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_DEFAULT, default=None)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(default='')

    def __str__(self):
        return 'Feedback #{}'.format(self.id)
