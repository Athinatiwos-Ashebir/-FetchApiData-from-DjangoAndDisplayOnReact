from django.db.models import fields
from rest_framework import serializers
from student.models import DetailsModel

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetailsModel
        fields="__all__"
       
       
