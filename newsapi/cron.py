# from .views import objectArray
# from .models import News
# from django.db import IntegrityError

# def my_cron_job():
#     dataList = objectArray()
#     for item in dataList:
#         try:
#             News.objects.create(author=item.get('by', ''), score=item.get('score', 0), title=item.get('title', ''), url=item.get('url', ''))
#         except IntegrityError as e:
#             if 'unique constraint' in str(e.args):
#                 continue