
# from celery import Celery
# from .views import objectArray
# from .models import News
# from django.db import IntegrityError


# from celery import Celery
# app = Celery('tasks',broker="redis://localhost:6379/0")

# @app.task
# def check():
    # print('I am checking your stuff')
    # app.conf.beat_schedule = {
    # 'run-me-every-ten-seconds': {
    # 'task': 'tasks.check',
    # 'schedule': 10.0
    # }
    # }


# @shared_task(name="fetch_new_data")
# def updateDB():
#     dataSource = objectArray()
#     for item in dataSource:
#         try:
#             News.objects.create(author=item['by'], score=item.get('score', 0), title=item.get('title', ''), url=item.get('url', ''))
#         except IntegrityError as e:
#             if 'unique constraint' in str(e.args):
#                 continue

# from celery.schedules import crontab

# app.conf.beat_schedule = {
#     'add-every_five_minutes': {
#         'task': 'tasks.updateDB',
#         'schedule': crontab(minute=5,),
#         # 'args': (16, 16),
#     },
# }