from django.contrib.auth.models import AbstractUser

class TechUser(AbstractUser):
    ...

    def __str__(self):
        return self.username
