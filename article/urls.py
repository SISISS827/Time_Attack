from django.urls import path
from article import views

urlpatterns = [
    path('api/article/', views.ArticleView.as_view(), name="ArticleView"),
]