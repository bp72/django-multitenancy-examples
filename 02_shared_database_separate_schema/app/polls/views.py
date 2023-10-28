import json

from django.http.request import HttpRequest
from django.http.response import HttpResponse

from .models import Question


def questions(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        json.dumps({
            'tenant': request.tenant.name,
            'questions': [
                {
                    'id': question.id,
                    'question_text': question.question_text,
                    'choices': [
                        {
                            'id': choice.id,
                            'choice_text': choice.choice_text,
                        } for choice in question.choice_set.all()
                    ]
                } for question in Question.objects.prefetch_related('choice_set')
            ],
        }),
        content_type='application/json',
    )
