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

# <게시글, 작성자, 작성 시간, 내용>이 포함된 comment라는 테이블을 추가해주세요
# 게시글과 작성자는 fk 필드로 생성해주셔야 해요
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name="게시글", on_delete=models.CASCADE)
    content = models.TextField('내용', max_length=500)
    create_time = models.DateTimeField("작성 시간", auto_now_add=True)

    def __str__(self) -> str:
        return f'작성자 : {self.user}, 내용 : {self.content}'
