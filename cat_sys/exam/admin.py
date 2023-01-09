from django.contrib import admin

from exam import models

admin.site.register(models.Student)
admin.site.register(models.Test)
admin.site.register(models.Item)
admin.site.register(models.Record)