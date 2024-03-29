# coding=utf8
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Student,Test,Item,Record
from .resource import StudentResource,ItemResource

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource

    list_display = ('sid','sex','grade')
    fields = ('sid','sex','grade')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('tid','title','total_time')
    fields = ('title','items','total_time','student')

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource


admin.site.register(Record)