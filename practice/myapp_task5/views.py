import random
import logging

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

logger = logging.getLogger(__name__)


def one(request):
    answer = ['Орёл', 'Решка']
    i = random.randint(0, 1)
    logger.info(answer[i])
    return HttpResponse(f'{answer[i]}')


def two(request):
    answer = random.randint(1, 6)
    logger.info(answer)
    return HttpResponse(f'{answer}')


def three(request):
    answer = random.randint(0, 100)
    logger.info(answer)
    return HttpResponse(f'{answer}')
