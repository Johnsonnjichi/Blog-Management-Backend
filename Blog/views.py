from django.shortcuts import render
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *



# Create your views here.
@api_view(['GET'])
def Home(request):
    print('johnson ')
    return Response({'Johnson Test Area!!'})


@api_view(['GET'])
def get_blog(request):
    blogs = BlogPost.objects.all()
    serializer = BlogPostSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_blog(request):
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Created successful", status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def update_blog(request, id):
    blog = BlogPost.objects.get(id=id)
    serializer = BlogPostSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Updated successful", status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_blog(request, id):
    blog = BlogPost.objects.get(id=id)
    blog.delete()
    return Response("Blog deleted", status=status.HTTP_200_OK)



