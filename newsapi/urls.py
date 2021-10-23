from django.urls import path
from . import views

urlpatterns = [
    path('index', views.indexView, name="index"),
    # path('index', views.search, name="search"),
    path('api/news', views.NewsList.as_view(), name="news"),
    path('results/', views.SearchView.as_view(), name='search'),
    path("api/delete/<int:pk>/", views.NewsDetail.as_view(), name="detail"),
]
