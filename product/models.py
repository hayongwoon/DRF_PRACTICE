from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField("제목", max_length=50)
    thumbnail = models.ImageField("썸네일", upload_to="product/thumbnail", height_field=None, width_field=None, max_length=None)
    description = models.TextField("설명")
    created = models.DateTimeField("등록일자", auto_now_add=True)
    exposure_start_date = models.DateField("노출 시작 시간")
    exposure_end_date = models.DateField("노출 종료 시간")
    is_active = models.BooleanField("활성화 여부")

    def __str__(self):
        return f"{self.title} 이벤트입니다."
