from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime

from celery import Celery
from .views import objectArray
from .models import News
from django.db import IntegrityError
  
  
@shared_task(name="update_db_with_new_data")
def updateDB():
    dataSource = objectArray()
    for item in dataSource:
        try:
            News.objects.create(author=item.get('by', ''), score=item.get('score', 0), title=item.get('title', ''), url=item.get('url', ''))
        except IntegrityError as e:
            if 'unique constraint' in str(e.args):
                continue
