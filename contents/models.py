import datetime
import os
import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class SuperModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Gram(SuperModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=128, default="")
    content = models.TextField(default="")
    STATUS_CODE = (
        ("1", "초안"),
        ("2", "발행"),
    )
    status = models.CharField(max_length=5, choices=STATUS_CODE, default="1")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "컨텐츠"
        verbose_name_plural = "컨텐츠"
        ordering = ['-id']


def gen_upload_image_path(instance, filename):
    date_path = datetime.datetime.now().strftime('%Y/%m/%d')
    uuid_name = uuid.uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return "/".join([
        instance.UPLOAD_PATH,
        date_path,
        uuid_name + extension,
    ])


class Image(SuperModel):
    UPLOAD_PATH = 'upload'
    content = models.ForeignKey(Gram, on_delete=models.CASCADE)
    resource = models.ImageField(upload_to=gen_upload_image_path)
    order = models.SmallIntegerField()

    class Meta:
        verbose_name = "이미지"
        verbose_name_plural = "이미지"
        unique_together = ['content', 'order']
        ordering = ['-id']
