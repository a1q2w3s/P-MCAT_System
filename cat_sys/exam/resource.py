from import_export import resources
from .models import Student,Test,Item,Record

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
