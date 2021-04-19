from django.db import models

# Create your models here.
class Tasktable(models.Model):
    task_number = models.CharField(max_length=30, unique=True, null=False)  # 任务ID
    task_name = models.CharField(max_length=30,null=True)                   # 任务名字
    task_type = models.CharField(max_length=30, null=False)        # 任务类型
    request_target = models.CharField(max_length=30, null=False)   # 请求目标网站

    create_time = models.DateTimeField(auto_now_add=True)   # 创建时间
    return_time = models.DateTimeField(null=True)           # return时间
    complete_time = models.DateTimeField(null=True)         # 完成时间

    parameter = models.TextField(null=True)       # 参数-josn格式
    state = models.SmallIntegerField(null=False)  # 状态-（已创建=1、已发送=2、已就绪=3、下载中=4、下载完成=5、任务完成=6、任务失败=7）
    fail_reason = models.TextField(null=True)     # 失败原因

    class Meta:
        db_table = 'api_task'       # 表名
        ordering = ['task_number']  # 排序

class Download(models.Model):
    task_number = models.CharField(max_length=30, null=False)  # 任务ID
    address = models.CharField(max_length=30)                  # 下载地址

    create_time = models.DateTimeField(auto_now_add=True)   # 创建时间
    complete_time = models.DateTimeField(null=True)         # 完成时间

    state = models.SmallIntegerField(null=False)   # 状态-（未下载=1、下载中=2、下载完成=3、下载失败=4）

    class Meta:
        db_table = 'api_download'   # 表名
        ordering = ['task_number']  # 排序
