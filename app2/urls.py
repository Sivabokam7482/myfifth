from django.urls import path
from app2.views import*
app_name='something2'

urlpatterns=[
    path('third/',third,name='third'),
    path('forth/',forth,name='forth'),
]