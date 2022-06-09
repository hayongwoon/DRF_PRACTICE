from django.db import models

class User(models.Model):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=60)
    fullname = models.CharField("이름", max_length=20)
    join_date = models.DateTimeField("가입일", auto_now_add=True)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.ForeignKey(to=User, verbose_name="사용자", on_delete=models.CASCADE, unique=True)
    hobby = models.ManyToManyField(to='Hobby', verbose_name="취미") #to=문자열 은 하비 모델이 해당 선언 시 보다 아래에 있어서 ''를 붙여줘야한다.
    introduction = models.TextField("소개")
    birthday = models.DateField("생일")
    age = models.IntegerField("나이")


class Hobby(models.Model):
    name = models.CharField("취미", max_length=50)

    def __str__(self):
        return self.name