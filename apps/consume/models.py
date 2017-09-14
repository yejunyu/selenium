from django.db import models
from users.models import UserProfile
from browser.models import ClickTask

# Create your models here.

class MyCharge(models.Model):
    user_name = models.ForeignKey(UserProfile, verbose_name=u"用户", default=1)
    money = models.CharField(max_length=10, verbose_name=u"充值款")
    remark = models.CharField(max_length=255, verbose_name=u"标记说明")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=u"充值日期")
    update_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = u"充值记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name.username


class MyConsume(models.Model):
    user_name = models.ForeignKey(UserProfile, verbose_name=u"用户", default=1)
    task_id = models.ForeignKey(ClickTask, verbose_name=u"业务ID")
    type = models.PositiveSmallIntegerField(choices=((0,"扣款"),(1,"退款")), verbose_name=u"类型")
    reason = models.CharField(max_length=255, verbose_name=u"消费内容")
    money = models.CharField(max_length=10, verbose_name=u"金额")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=u"时间")
    update_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = u"消费记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name.username
