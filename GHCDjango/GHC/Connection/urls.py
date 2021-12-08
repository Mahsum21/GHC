from django.urls import re_path, path
from . import views
app_name="ghc"


urlpatterns = [
    path('', views.Index, name="index"),
    path( 'horaires/', views.Horaires, name="horaires" ), 
    path( 'admin/', views.Admin, name="admin" ), 

    path( 'admin/personne/', views.Personne, name="personne" ), 
    # path( 'admin/personne/delete/<int:personneId>', views.Personne, name="personnedelete" ), 
    path( 'admin/personne/create', views.Personne, name="personnecreate" ), 
    path( 'admin/personne/add', views.Personne, name="personneadd" ), 
    # path( 'admin/personne/edit/<int:personneId>', views.Personne, name="personneedit" ), 
    # path( 'admin/personne/update/<int:personneId>', views.Personne, name="personneupdate" ), 


    # path( 'admin/<str:table>/<str:operation>/', views.Operations, name="operation" ), 
    # re_path(r'^(?P<studentId>[0-9])/$', views.Details), 
    # path('<int:studentId>/', views.Details, name='Details')
]
