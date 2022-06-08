from django.urls import path
from AppCoder.views import curso, profesores, inicio

urlpatterns = [
    path('curso/', curso),
    path('profesores/', profesores),
    path('', inicio),
]
