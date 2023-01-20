from django.db import models


class Product(models.Model):
    # 거래코드
    TRANSACTION_CODE = (
        (1, '직거래'),
        (2, '안전거래'),
        (3, '직거래 + 안전거래'),

    )
    # user = models.ForeignKey() Account 개발 될때 까지 중단
    title = models.CharField(max_length=100)
    content = models.TextField()

    transaction_code = models.PositiveSmallIntegerField(choices=TRANSACTION_CODE, default=1)
    is_expired = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField()


class Photo(models.Model):
    # user = models.ForeignKey
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='photos')
    image = models.ImageField(upload_to='images/')


class Comment(models.Model) :
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    add_modify_at = models.DateTimeField(auto_now=True)

