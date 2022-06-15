from operator import mod
from unicodedata import category
from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField('카테고리', max_length=80)
    explain = models.CharField('설명', max_length=100)

    def __str__(self) -> str:
        return self.name

class Article(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField('제목', max_length=80)
    #ManytoMany 모델은 다중 선택이 가능
    category = models.ManyToManyField(Category, verbose_name='카테고리', related_name='article_category')
    content = models.TextField('내용', max_length=500)

    def __str__(self) -> str:
        return f'작성자 : {self.user}, 제목 : {self.title}'