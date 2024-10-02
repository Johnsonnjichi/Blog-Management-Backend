from django.shortcuts import render
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
# from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


# Signup route
@api_view(['POST'])
def SignUp(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        #jwt to generate token for a new user
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        #return token in the res
        return Response({
            "message": "User created successfully",
            "refresh": str(refresh),
            "access": access_token
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Generate JWT Token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Login route
@api_view(['POST'])
def LogIn(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(get_tokens_for_user(user), status=status.HTTP_200_OK)


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
@permission_classes([IsAuthenticated])
def create_blog(request):
    # Pass the request to the serializer context
    serializer = BlogPostSerializer(data=request.data, context={'request': request})

    # Validate and save the post
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Post created successfully"}, status=status.HTTP_201_CREATED)
    else:
        print(f"Validation errors: {serializer.errors}")  # Log validation errors for debugging
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
@permission_classes([IsAuthenticated])
def delete_blog(request, id):
    blog = BlogPost.objects.get(id=id)
    blog.delete()
    return Response("Blog deleted", status=status.HTTP_200_OK)



