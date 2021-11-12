from django.urls import re_path, path
from . import views
app_name="ghc"


urlpatterns = [
    path('', views.Index, name="index"),
    path( 'horaires/', views.Horaires, name="horaires" ), 
    path( 'admin/', views.Admin, name="admin" ), 
    # re_path(r'^(?P<studentId>[0-9])/$', views.Details), 
    # path('<int:studentId>/', views.Details, name='Details')
]
