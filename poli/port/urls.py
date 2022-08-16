from django.urls import path
from .views import *

urlpatterns = [
    path('magic_square/', magic_square, name='magic_square'),
    path('student_statistics/', student_statistics, name='student_statistics'),
    path('progress/', progress, name='progress'),
]