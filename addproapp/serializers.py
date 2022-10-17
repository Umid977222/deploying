from .models import Adds
from rest_framework import serializers


class AddSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adds
        fields = ['id', 'name', 'img', 'description', 'add_bot_button']
