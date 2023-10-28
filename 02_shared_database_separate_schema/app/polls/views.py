import json

from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist

from .models import Tenant, Question


def questions(request: HttpRequest) -> HttpResponse:
    host = request.get_host()
    host = host.split(':')[0] if host else ''
    try:
        tenant = Tenant.objects.get(host=host)
    except ObjectDoesNotExist:
        raise Http404()

    return HttpResponse(
        json.dumps([
            {
                'id': question.id,
                'question_text': question.question_text,
                'choices': [
                    {
                        'id': choice.id,
                        'choice_text': choice.choice_text,
                    } for choice in question.choice_set.all()
                ]
            } for question in Question.objects.filter(tenant=tenant).prefetch_related('choice_set')
        ]),
        content_type='application/json',
    )
