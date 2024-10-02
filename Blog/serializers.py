from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth.models import User


class BlogPostSerializer(serializers.ModelSerializer):

    author_name = serializers.SerializerMethodField() 
    created_at = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", read_only=True)
    updated_at = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", read_only=True)                     
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author_name']       
        extra_kwargs = {'author': {'read_only': True}}                                         

    def get_author_name(self, obj):
        return obj.author.username
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['updated_at'] = instance.updated_at.strftime('%B %d, %Y %I:%M %p')
        representation['created_at'] = instance.created_at.strftime('%B %d, %Y %I:%M %p')                 
        return representation                                                            

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user                                                
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
    
