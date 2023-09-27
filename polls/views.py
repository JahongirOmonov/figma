from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import AuthorSerializer, BookSerializer
from .models import authorModel, bookModel
from django.http import JsonResponse
from rest_framework import status

# Create your views here.


class getallAuthor(APIView):
    def get(self, request):
        all=authorModel.objects.all()
        serializer = AuthorSerializer(all, many=True)
        return Response(serializer.data)
    
class getallbooks(APIView):
    def get(self, request, *args, **kwargs):
        all=bookModel.objects.all()
        serializer = BookSerializer(all, many=True)
        return Response(serializer.data)
    
    
class getAuthorID(APIView):
    def get(self, request, *args, **kwargs):
        all=bookModel.objects.filter(author=kwargs['forid'])
        serializer = BookSerializer(all, many=True)
        return Response(serializer.data)
    

class postBook(APIView):
    def post(self, request, *args, **kwargs):
        if str(request.data)=="AnonymousUser":
            if request.user.roles == 2:
                serializer=BookSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
        return Response({"msg":"Something went wrong!"})
    
    
    
class patchBook(APIView):
    def patch(self, request, *args, **kwargs):
        if str(request.user)!="AnonymousUser":
            if request.user.roles==3:
                x=get_object_or_404(bookModel, id=kwargs['forid'])
                ser=BookSerializer(x, data=request.data, partial=True)
                if ser.is_valid():
                    ser.save()
                    return Response(ser.data)
                return Response(ser.errors)
        return Response({"msg":"go away"})
    
class putBook(APIView):
    def put(self, request, *args, **kwargs):
        if str(request.user)!="AnonymousUser":
            if request.user.roles==3:
                x=get_object_or_404(bookModel, id=kwargs['forid'])
                serializer=BookSerializer(x, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
        return Response(serializer.errors)
    
class deleteBook(APIView):
    def delete(self, request, *args, **kwargs):
        if str(request.user)!="AnonymousUser":
            if request.user.roles==3 or request.user.roles==2:
                x=get_object_or_404(bookModel, id=kwargs['forid'])
                x.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"msg":"go away"})
    

class postAuthor(APIView):
    def post(self, request, *args, **kwargs):
        if str(request.data)=="AnonymousUser":
            if request.user.roles == 2:
                serializer=AuthorSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
        return Response({"msg":"Something went wrong!"})
    
    
    
class patchAuthor(APIView):
    def patch(self, request, *args, **kwargs):
        if str(request.user)!="AnonymousUser":
            if request.user.roles==3:
                x=get_object_or_404(authorModel, id=kwargs['forid'])
                ser=BookSerializer(x, data=request.data, partial=True)
                if ser.is_valid():
                    ser.save()
                    return Response(ser.data)
                return Response(ser.errors)
        return Response({"msg":"go away"})
    
class putAuthor(APIView):
    def put(self, request, *args, **kwargs):
        if str(request.user)!="AnonymousUser":
            if request.user.roles==3:
                x=get_object_or_404(authorModel, id=kwargs['forid'])
                serializer=AuthorSerializer(x, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
        return Response(serializer.errors)
    
class deleteAuthor(APIView):
    def delete(self, request, *args, **kwargs):
        if str(request.user)!="AnonymousUser":
            if request.user.roles==3 or request.user.roles==2:
                x=get_object_or_404(authorModel, id=kwargs['forid'])
                x.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"msg":"go away"})