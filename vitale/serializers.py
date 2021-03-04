from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, data):
        if data['first_name'] == "lol":
            raise serializers.ValidationError({"first_name": "you can't name it \"lol\" lol"})
        return data

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'date_of_birth', 'gender',
            'department_of_birth', 'social_security_number'
        )
