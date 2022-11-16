
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

from rest_framework.urlpatterns import format_suffix_patterns
router = SimpleRouter()
router.register('snippets', SnippetViewSet,basename="snippet")


urlpatterns = [
    path('api', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
    path('SnippetList', SnippetList.as_view()),
    path('SnippetDetail/<int:todo_id>/', SnippetDetail.as_view(), name= 'snippetdetail'),
     path('SnippetList', SnippetList.as_view()),
    path('SnippetDetail/<int:pk>/', SnippetDetail.as_view()),
    path('Login/',LoginView.as_view()),
    path('Register/', Register.as_view()),
   # path('api/login/', LoginAPI.as_view(), name='login'),
    path('product/', ProductAPI.as_view()),
    path('product/<int:pk>', ProductDetails.as_view()),
]+router.urls

