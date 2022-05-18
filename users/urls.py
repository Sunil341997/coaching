from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('createcoach/', CreateCoach.as_view()),
    path('createcoachee/', CreateCoachee.as_view()),
    path('getcoaches/', GetCoaches.as_view()),
    path('getcoachees/', GetCoachees.as_view()),
    path('updatecoach/', UpdateCoach.as_view()),
    path('updatecoachee/', UpdateCoachee.as_view()),
    path('deletecoachee/', DeleteCoachee.as_view()),
    path('deletecoach/', DeleteCoach.as_view()),
]