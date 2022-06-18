from email.policy import default
from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField('제목', max_length=100)
    thumbnail = models.ImageField('섬네일', upload_to='product/thumbnail',  height_field=None, width_field=None, max_length=None)
    content = models.CharField('설명', max_length=120)
    register_date = models.DateTimeField("등록일", auto_now_add=True)
    start_propose_date = models.DateTimeField("노출 시작일") 
    end_propose_date = models.DateTimeField("노출 종료일") 
    is_active = models.BooleanField('활성화 여부', default=True) 

    def __str__(self):
        return f"{self.title}이벤트 입니다."