from django.contrib import admin

from .models import Student,Test,Item,Record

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('sid','name','sex','grade')
    fields = ('sid','name','sex','grade','pwd')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('tid','title','total_time')
    fields = ('title','items','total_time','student')
admin.site.register(Item)
admin.site.register(Record)