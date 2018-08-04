"""Django sample app in single file.

To run as a stand-alone app, run:

.. code-block:: sh

    django-admin runserver --pythonpath=. --settings=app

"""
import random
import string
import django
from django.conf import settings
from django.http import HttpResponse
if django.VERSION >= (2,):
    from django.urls import re_path
else:  # django1 support
    from django.conf.urls import url as re_path


SECRET_KEY = ''.join(
    random.choice(string.ascii_lowercase + string.digits) for _ in range(40))

SETTINGS = dict(
    DEBUG=False,
    SECRET_KEY=SECRET_KEY,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['127.0.0.1', 'localhost', 'testserver'],
)

globals().update(SETTINGS)  # django-admin support (in module doc)
settings.configure(**SETTINGS)  # module import support (see test_app.py)


def sample_page(request):
    return HttpResponse('Hello, World!')


urlpatterns = [
    re_path(r'^$', sample_page),
]
