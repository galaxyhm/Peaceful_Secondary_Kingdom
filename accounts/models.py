from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return f'{self.username}'
    birthday = models.DateField(default='1990-01-01')
    address = models.TextField(null=True)


class PaymentInfo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='payment_info',
    )
    bank_account = models.IntegerField()
    bank_account_password = models.IntegerField()


'''
# 선택정보만 따로 뺀 것. (안씀)
class UserExtraInfo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_extra_info',
    )
    birthday = models.DateField()
    address = models.TextField()
'''