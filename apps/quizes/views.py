from .serializers import QuizSerializer
from .models import Quiz
from .permissions import IsQuizAuthor

from rest_framework import generics


class QuizCreateView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsQuizAuthor,)


class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer



