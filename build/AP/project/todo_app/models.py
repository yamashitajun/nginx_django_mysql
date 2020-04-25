from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Status(models.Model):
    name = models.CharField('ステータス',max_length=10)

    def __str__(self):
        return self.name
        
class Todo(models.Model):
    title = models.CharField(verbose_name ='タイトル',max_length=100)
    content = models.TextField(verbose_name ='内容', null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT,verbose_name ='ステータス')
    limit_date = models.DateTimeField(verbose_name ='期限',default=timezone.now)
    created_date = models.DateTimeField(verbose_name ='登録日',default=timezone.now)
    modify_date = models.DateTimeField(verbose_name ='変更日',blank=True, null=True)



    def modify(self):
        self.modify_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
        