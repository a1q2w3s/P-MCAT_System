from django.db import models

# 考生表
class Student(models.Model):
    sid = models.CharField(max_length=20,primary_key=True,verbose_name='考生号')
    name = models.CharField(max_length=20,verbose_name='姓名')
    sex = models.BooleanField(default=0,choices=[(0,'女'),(1,'男')],verbose_name='性别')
    pwd = models.CharField(max_length=20,verbose_name='密码')

    class Meta:
        verbose_name = '考生'
        verbose_name_plural = '考生信息表'

    def __str__(self):
        return self.sid

# 题目表
class Item(models.Model):
    MULTICHOICE = 'MC'
    FILLIN = 'FI'
    ITEM_TYPE_CHOICES = [
        (MULTICHOICE,'选择题'),
        (FILLIN,'填空题'),
    ]

    iid = models.AutoField(primary_key=True,verbose_name='序号')
    title = models.TextField(verbose_name='题干')
    types = models.CharField(max_length=50,default=MULTICHOICE,choices=ITEM_TYPE_CHOICES,verbose_name='类型')
    options = models.JSONField(null=True,verbose_name='选项')
    answer = models.JSONField(verbose_name='正确答案')
    parameters = models.JSONField(verbose_name='参数')
    dimensions = models.JSONField(verbose_name='维度')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')

    class Meta:
        verbose_name = '题目'
        verbose_name_plural = '题库'

    def __str__(self):
        return self.iid


# 考试表
class Test(models.Model):
    tid = models.AutoField(primary_key=True,verbose_name='序号')
    title = models.CharField(max_length=50,unique=True,verbose_name='考试名称')
    items = models.ManyToManyField(Item,verbose_name='题目') # 之后单独出题库表便于复用题库
    total_time = models.IntegerField(help_text='单位是分钟',verbose_name='时长')
    student = models.ManyToManyField(Student,verbose_name='考生列表')

    # ability_est_method 能力估计方法
    # selection_strategy 选题策略
    # terminal_criteria 终止规则

    class Meta:
        verbose_name = verbose_name_plural = '考试'

# 作答记录表
class Record(models.Model):
    rid = models.AutoField(primary_key=True,verbose_name='序号')
    student = models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name='考生号')
    test = models.ForeignKey(Test,on_delete=models.CASCADE,verbose_name='考试号')
    record = models.JSONField(verbose_name='作答')
    grade = models.FloatField(verbose_name='成绩')
    ability = models.FloatField(verbose_name='能力估计值')
    
    # process 过程性数据

    class Meta:
        verbose_name = verbose_name_plural = '作答记录'

