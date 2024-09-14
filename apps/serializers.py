from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product, User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'type'


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = 'updated_at',

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = CategoryModelSerializer(instance.category).data
        data['owner'] = UserModelSerializer(instance.owner).data
        return data


class RegisterModelSerializer(ModelSerializer):
    # password = CharField(write_only=True)
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'username', 'password', 'confirm_password'

        extra_kwargs = {'password': {'write_only': True}}

    # 1 - version
    # def create(self, validated_data: dict):
    #     password = validated_data.pop('password')
    #     first_name = validated_data['first_name']
    #     last_name = validated_data['last_name']
    #     if not first_name.isalpha():
    #         raise serializers.ValidationError("Please enter correct first name!")
    #     if not last_name.isalpha():
    #         raise serializers.ValidationError("Please enter correct last name!")
    #     user = super().create(validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user
    # 2 - version

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.pop('password')
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')
        if not first_name.isalpha():
            raise serializers.ValidationError('Please enter correct first name')
        if not last_name.isalpha():
            raise serializers.ValidationError('Please enter correct last name')
        if password != confirm_password:
            raise serializers.ValidationError('Passwords did not matched!')
        attrs['password'] = make_password(password)
        return attrs