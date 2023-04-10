from app.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('rohit/',rohit,name='rohit'),
]