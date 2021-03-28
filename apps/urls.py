from django.urls import path

from .views import (
    index, 
    create,
    detail,
    delete,
    update,
)

app_name = 'apps'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('<int:pk>/detail/', detail, name='detail'),
    path('<int:pk>/delete/', delete, name='delete'),
    path('<int:pk>/update/', update, name='update'),
]