from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.Index)
    # re_path(r'^$', views.Listing), 
    # re_path(r'^(?P<studentId>[0-9])/$', views.Details), 
    # path('<int:studentId>/', views.Details, name='Details')
]
