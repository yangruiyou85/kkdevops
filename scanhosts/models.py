from django.db import models


# Create your models here.



class UserIPinfo(models.Model):
    ip = models.CharField(max_length=40, default='', verbose_name=u'ip地址')
    time = models.DateTimeField(verbose_name=u"更新时间"，auto_now = True)

    class Meta:
        verbose_name = u'用户访问地址信息表'
        verbose_name_plural = verbose_name
        db_table = "useripinfo"
