from django.shortcuts import render
import requests
from django.core.paginator import Paginator
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from django.db import IntegrityError
from django.views.generic.list import ListView

# Create your views here.

def objectArray():
    dataObj = []
    for i in range(1,21):
        url = f'https://hacker-news.firebaseio.com/v0/item/{str(i)}.json?print=pretty'
        response = requests.get(url)
        data = response.json()
        dataObj.append(data)
    return dataObj

def indexView(request):
    dataList = objectArray()
    
    paginator = Paginator(dataList, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(dataList)
    
    
    # for item in dataList:
    #     try:
    #         News.objects.create(author=item['by'], score=item.get('score', 0), title=item.get('title', ''), url=item.get('url', ''))
    #     except IntegrityError as e:
    #         if 'unique constraint' in str(e.args):
    #             continue
 
  
    context = {
        'dataList': page_obj,
    }
    return render(request, 'newsapi/index.html', context)

def search(request):
    value = request.GET.get('value')
    queryset = News.objects.filter(title__contains=value)
        
    context = {
        'queryset': queryset,
    }
    return render(request, 'newsapi/index.html', context)

class SearchView(ListView):
    model = News
    template_name = 'newsapi/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = News.objects.filter(title__contains=query)
            result = postresult
        else:
            result = None
        return result


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
class NewsDetail(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    

