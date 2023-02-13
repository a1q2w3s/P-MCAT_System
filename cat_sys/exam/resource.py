from import_export import resources
from .models import Student,Test,Item,Record
from collections import OrderedDict
import json

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        fields = ['sid']
        exclude = ['id']
        import_id_fields = ('sid',)

class ItemResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        try:
            title = row['title']
            types = row['types']
            
            options_row = OrderedDict()
            try:
                for i in range(100):
                    options_row[f'opt_{i+1}'] = row[f'opt_{i+1}']
            except Exception as e:
                pass
            options = json.dumps(options_row,ensure_ascii=False)



            row.clear()
            row['title'] = title
            row['types'] = types
            row['options'] = options
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
        exclude = ['id',]
        import_id_fields = ('title',)
