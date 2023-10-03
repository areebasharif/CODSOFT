from django.urls import path
from .views import home,deletion
urlpatterns = [
    path('', home, name='index'),
    path('delete/<str:pk>', deletion,name='delete')
]
