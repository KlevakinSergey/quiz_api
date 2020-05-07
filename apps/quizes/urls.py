from django.urls import path
from .views import QuizCreateView, QuizListView


urlpatterns = [
    path('', QuizCreateView.as_view(), name='quiz-create'),
    path('list/', QuizListView.as_view(), name='list-quizes'),

]
