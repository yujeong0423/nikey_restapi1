from rest_framework import serializers
from nikey_api.models import User

class NikeySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'uname', 'password', 'ubirth', 'usex', 'uemail', 'uphone', 'admin', 'acc_allow']
