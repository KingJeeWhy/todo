from rest_framework import serializers
from hello.models import Test


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name', 'checked')
