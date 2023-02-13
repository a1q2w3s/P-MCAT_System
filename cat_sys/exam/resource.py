from import_export import resources
from .models import Student,Test,Item,Record

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = ['sid']
        exclude = ['id']
        import_id_fields = ('sid',)

class ItemResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        try:
            print(row)
            row['options'] = "{'a':'a'}"
            row['answer'] = "{'a':'a'}"
            row['parameters'] = "{'a':'a'}"
            row['dimensions'] = "{'a':'a'}"
        except Exception as e:
            print(e)

        return row


    class Meta:
        model = Item
        fields = [
            'title',
            'types',
            'options',
            'answer',
            'parameters',
            'dimensions'
            ]
        exclude = ['id']
