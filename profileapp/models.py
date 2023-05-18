from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # on_delete : User 객체가 사라질 때 어떤 행동을 할 것인지
    # CASCADE : 해당되는 프로필이 사라지도록 함.
    # related_name : 바로 정보에 접근해 정보를 가져올 수 있도록 함.

    # 프로필 사진
    # upload_to : 이미지가 저장될 경로
    # null=True : 꼭 프로필 사진을 올려야 하는 것은 아니다.
    image = models.ImageField(upload_to='profile/', null=True)

    # nickname
    # unique=True : nickname은 유일해야한다. (여러명이 같은 닉네임을 사용할 수 없다.)
    nickname = models.CharField(max_length=20, unique=True, null=True)

    # 사진 아래의 소개글
    message = models.CharField(max_length=100, null=True)

    