from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    """
    Lista todos os snippets, ou cria um novo
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Recupera, atualiza ou deleta uma instancia de snippets
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
