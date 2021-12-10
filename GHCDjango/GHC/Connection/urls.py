from django.urls import re_path, path
from . import views
app_name="ghc"


urlpatterns = [
    path('', views.Index, name="index"),
    path( 'horaires/', views.Horaires, name="horaires" ), 
    path( 'admin/', views.Admin, name="admin" ), 

    path( 'admin/etudiant/', views.Etudiant, name="etudiant" ), 
    path( 'admin/etudiant/delete/<int:etudiantId>', views.EtudiantDelete, name="etudiantdelete" ), 
    path( 'admin/etudiant/create', views.EtudiantCreate, name="etudiantcreate" ), 
    path( 'admin/etudiant/add', views.EtudiantAdd, name="etudiantadd" ), 
    path( 'admin/etudiant/edit/<int:etudiantId>', views.EtudiantEdit, name="etudiantedit" ), 
    path( 'admin/etudiant/update/<int:etudiantId>', views.EtudiantUpdate, name="etudiantupdate" ), 

    path( 'admin/professeur/', views.Professeur, name="professeur" ), 
    path( 'admin/professeur/delete/<int:professeurId>', views.ProfesseurDelete, name="professeurdelete" ), 
    path( 'admin/professeur/create', views.ProfesseurCreate, name="professeurcreate" ), 
    path( 'admin/professeur/add', views.ProfesseurAdd, name="professeuradd" ), 
    path( 'admin/professeur/edit/<int:professeurId>', views.ProfesseurEdit, name="professeuredit" ), 
    # path( 'admin/professeur/update/<int:professeurId>', views.Professeur, name="professeurupdate" ), 

    path( 'admin/matiere/', views.Matiere, name="matiere" ),
    path( 'admin/matiere/delete/<int:matiereId>', views.MatiereDelete, name="matieredelete" ),
    path( 'admin/matiere/create', views.MatiereCreate, name="matierecreate" ),
    path( 'admin/matiere/add', views.MatiereAdd, name="matiereadd" ),
    path( 'admin/matiere/edit/<int:matiereId>', views.MatiereEdit, name="matiereedit" ), 
    # path( 'admin/matiere/update/<int:matiereId>', views.MatiereUpdate, name="matiereupdate" ), 

    path( 'admin/horaire/', views.Horaire, name="horaire" ),
    path( 'admin/horaire/delete/<int:horaireId>', views.HoraireDelete, name="horairedelete" ),
    path( 'admin/horaire/create', views.HoraireCreate, name="horairecreate" ),
    path( 'admin/horaire/add', views.HoraireAdd, name="horaireadd" ),
    path( 'admin/horaire/edit/<int:horaireId>', views.HoraireEdit, name="horaireedit" ), 
    # path( 'admin/horaire/update/<int:horaireId>', views.HoraireUpdate, name="horaireupdate" ), 



    # path( 'admin/<str:table>/<str:operation>/', views.Operations, name="operation" ), 
    # re_path(r'^(?P<studentId>[0-9])/$', views.Details), 
    # path('<int:studentId>/', views.Details, name='Details')
]
