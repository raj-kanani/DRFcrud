from django.urls import path
from . import views


urlpatterns = [
    path('student/', views.StudentApi.as_view(), name='student'),
    path('hello/', views.hello_world, name='hello'),

]
