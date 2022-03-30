

from rest_framework import serializers

from api.models import Lang

class LangSerializer(serializers.ModelSerializer):
   class Meta:
       model=Lang
       fields = "__all__"
