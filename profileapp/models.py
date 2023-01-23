from django.db import models

# Create your models here.

class Profile(models.Model):
    # on_delete 연결되어 있는 유저 객체가 없애질때 Profile은 CASCADE 행동을 할지 정책을 정하는 것
    # request 객체에서 user.profile.nickname을 호출할 수 있도록 연결해주는 기능
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # upload_to : 이미지가 저장될 서버 경로, media/profile 경로를 의미함, null=True는 반드시 올리지 않아도 괜찮음
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

    # model Form은 기존의 model을 보고 form을 만들어주는 기능