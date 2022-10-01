from django.db.migrations import serializer

from myresume.models import Resume


class ResumeConvert(serializer.ModelFieldSerializer):
    class Meta:
        model = Resume
        fields = '__all__'
