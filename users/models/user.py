from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from rest_framework.authtoken.models import Token
from django.db.utils import IntegrityError

class UserExistsException(Exception):
    pass

class CustomToken(Token):
    user = models.ForeignKey("User", on_delete=models.CASCADE)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email: str, password: str, **extra_fields): 
        try:
            user: User = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self.db)
            return user
        except IntegrityError:
            raise UserExistsException()

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()
