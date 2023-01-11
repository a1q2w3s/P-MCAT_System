from import_export import resources
from .models import Student,Test,Item,Record

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = ['sid']
        exclude = ['id']
        import_id_fields = ('sid',)
