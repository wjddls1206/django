from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    # pk가 지정되어있지 않음.
    # 맨 앞의 id로 자동배정해줌.
    text = models.CharField(max_length=255, null=False)