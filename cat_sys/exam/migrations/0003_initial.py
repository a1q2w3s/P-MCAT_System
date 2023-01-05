# Generated by Django 4.1.5 on 2023-01-05 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exam', '0002_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('title', models.TextField(verbose_name='题干')),
                ('item_type', models.CharField(choices=[('MC', '选择题'), ('FI', '填空题')], default='MC', max_length=50, verbose_name='类型')),
                ('options', models.JSONField(null=True, verbose_name='选项')),
                ('answer', models.JSONField(verbose_name='正确答案')),
                ('parameters', models.JSONField(verbose_name='参数')),
                ('dimensions', models.JSONField(verbose_name='维度')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '题目',
                'verbose_name_plural': '题库',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='考生号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('sex', models.BooleanField(choices=[(0, '女'), (1, '男')], default=0, verbose_name='性别')),
                ('pwd', models.CharField(max_length=20, verbose_name='密码')),
            ],
            options={
                'verbose_name': '考生',
                'verbose_name_plural': '考生信息表',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='考试名称')),
                ('time', models.IntegerField(help_text='单位是分钟', verbose_name='时长')),
                ('items', models.ManyToManyField(to='exam.item', verbose_name='题目')),
            ],
            options={
                'verbose_name': '考试',
                'verbose_name_plural': '考试',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('record', models.JSONField(verbose_name='作答')),
                ('grade', models.FloatField(verbose_name='成绩')),
                ('ability', models.FloatField(verbose_name='能力估计值')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.student', verbose_name='考生号')),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.test', verbose_name='考试号')),
            ],
            options={
                'verbose_name': '作答记录',
                'verbose_name_plural': '作答记录',
            },
        ),
    ]
