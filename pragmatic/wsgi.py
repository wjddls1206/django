"""
WSGI config for pragmatic project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# pragmatic.settings 에서 수정함 .base를 붙여서 수정함
# 이거 수정해도안됨 뭐야;;; 그럼 일단 원래대로 돌려둠;;
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pragmatic.settings')

application = get_wsgi_application()
