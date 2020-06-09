from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework import filters


# class SnippetViewSet(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Snippet.objects.all()
#         serializer = SnippetSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Snippet.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = SnippetSerializer(user)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = SnippetSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
#
#
#     def update(self, request, pk):
#         try:
#             snippet = Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk=None):
#         try:
#             snippet = Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
