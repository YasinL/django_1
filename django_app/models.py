import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)   # 字符字段     question_text 字段名称
    pub_date = models.DateTimeField('date published')  # 日期字段
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return  now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return  self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question =  models.ForeignKey(Question)   # models.ForeignKey 关联 买个Choice 只关联一个Question 一对一关联
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class UserProfile(models.Model):
    """用户管理模型"""
    STATUS_CHOICES = (
        (0, '禁用'),
        (1, '启用'),
    )
    username = models.CharField('用户名', max_length=50, unique=True)
    email = models.EmailField('邮箱', max_length=100, blank=True)
    phone = models.CharField('手机号', max_length=20, blank=True)
    real_name = models.CharField('真实姓名', max_length=50, blank=True)
    status = models.IntegerField('状态', choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户'
        verbose_name_plural = '用户管理'
        ordering = ['-created_at']

    def __str__(self):
        return self.username


class Menu(models.Model):
    """菜单管理模型"""
    STATUS_CHOICES = (
        (0, '禁用'),
        (1, '启用'),
    )
    name = models.CharField('菜单名称', max_length=50)
    url = models.CharField('菜单URL', max_length=200, blank=True)
    icon = models.CharField('图标', max_length=50, blank=True)
    parent = models.ForeignKey('self', verbose_name='父菜单', null=True, blank=True, related_name='children')
    order = models.IntegerField('排序', default=0)
    status = models.IntegerField('状态', choices=STATUS_CHOICES, default=1)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'menu'
        verbose_name = '菜单'
        verbose_name_plural = '菜单管理'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.name















