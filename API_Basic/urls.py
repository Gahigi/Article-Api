from django.urls import path
from . import views
urlpatterns = [
    path('article/', views.ViewAllArticle.as_view()),
    path('article/<int:id>', views. ViewArticle.as_view()),
]
