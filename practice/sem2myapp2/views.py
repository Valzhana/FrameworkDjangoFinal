from django.http import HttpResponse

# Create your views here.

import logging
from practice.sem2myapp2.models import Author

logger = logging.getLogger(__name__)


def author_read(request):
    logger.info(f'{request} request received!')
    authors = Author.objects.all()
    return HttpResponse(authors)
