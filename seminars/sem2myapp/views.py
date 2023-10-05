from django.shortcuts import render

# Create your views here.

import random
from django.http import HttpResponse
import logging

from models import HeadsTails

logger = logging.getLogger(__name__)


# logging.basicConfig(level=logging.INFO, filename='logger.log', filemode='a',
# format='%(levelname)s %(message)s')


def heads_tails(request):
    logger.info(f'{request} request received!')
    n = request.GET.get('n', '5')
    res = random.choice(['Орёл', 'Решка'])
    res_w = HeadsTails(res=res)
    res_w.save()
    data = HeadsTails.statistic(n)
    return HttpResponse(f'{data.items()}')
