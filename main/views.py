from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from apps.quizes.permissions import IsQuizAuthor


@permission_classes((IsQuizAuthor,))
@api_view(['GET'])
def api_root(request, format=None):
    response = Response({
        'sign-up': reverse('sign-up', request=request, format=format),
        'quiz-create': reverse('quiz-create', request=request, format=format),
        'quiz-list': reverse('list-quizes', request=request, format=format)

    })
    return response

