from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorList, ItemViewSet, BookList

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('authors/', AuthorList.as_view()),  # class-based 
    path('books/', BookList.as_view()),  # class-based    
]