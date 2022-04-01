from django.urls import path
from . import views

urlpatterns = [
    path('Api/', views.StudentApi.as_view(), name='Api'),
    # path('Api2/', views.hello_world, name='Api2'),

]
