from django import template
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
# Create your views here.

from Connection.models import Personne, Formation, Professeur, Horaire, Matiere

table = ""


def Index(request):
    context = {
    }
    return render(request,'connection/index.html',context)

def Horaires(request):
    context = {
    }
    return render(request,'connection/horaires.html',context)

def Admin(request):
    context = {
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/admin.html', context)

def Etudiant(request):
    etudiants = Personne.objects.all()
    context = {
        'option' : 0 , 
        'datas' : etudiants,
        'item' : "", 
    }
    return render(request,'connection/etudiant/index.html', context)

def EtudiantCreate(request):
    etudiants = Personne.objects.all()
    context = {
        'option' : 0 , 
        'datas' : etudiants,
        'item' : "", 
    }
    return render(request,'connection/etudiant/index.html', context)

def EtudiantAdd(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        personne = Personne.objects.filter(email = email)
        if not personne.exists():
            etudiant = Personne.objects.create(
                nom = request.POST.get('nom'), 
                prenom = request.POST.get('prenom'), 
                email = email, 
                mdp = request.POST.get('mdp')
            )
    return redirect('/admin/etudiant/')

def EtudiantEdit(request, etudiantId):
    datas = Personne.objects.all()
    item = Personne.objects.get(pk = etudiantId)
    context = {
        'option' : 1 , 
        'datas' : datas,
        'item' : item, 
    }
    return render(request,'connection/etudiant/index.html', context)

def EtudiantUpdate(request, etudiantId):
    personne = Personne.objects.get(pk = etudiantId)
    if request.method == 'POST':
        personne.nom = request.POST.get('nom')
        personne.prenom = request.POST.get('prenom')
        personne.email = request.POST.get('email')
        personne.mdp = request.POST.get('mdp')
        personne.save()
    return redirect('/admin/etudiant/')

def EtudiantDelete(request, etudiantId):
    Personne.objects.get(pk = etudiantId).delete()
    return redirect('/admin/etudiant/')

def Professeur(request):
    context = {
        'option' : 0 ,
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/professeur/index.html', context)

def ProfesseurCreate(request):
    context = {
        'option' : 0 , 
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/professeur/index.html', context)

def ProfesseurAdd(request):
    context = {
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/professeur/index.html', context)

def ProfesseurEdit(request, professeurId):
    context = {
        'option' : 1 , 
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/professeur/index.html', context)

def ProfesseurDelete(request, professeurId):
    context = {
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/etudiant/index.html', context)

def Matiere(request):
    context = {
        'option' : 0 ,
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/matiere/index.html', context)

def MatiereCreate(request):
    context = {
        'option' : 0 , 
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/matiere/index.html', context)

def MatiereAdd(request):
    context = {
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/matiere/index.html', context)

def MatiereEdit(request, matiereId):
    context = {
        'option' : 1 , 
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/matiere/index.html', context)

def MatiereDelete(request, matiereId):
    context = {
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/matiere/index.html', context)

def Horaire(request):
    context = {
        'option' : 0 ,
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/horaire/index.html', context)

def HoraireCreate(request):
    context = {
        'option' : 0 , 
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/horaire/index.html', context)

def HoraireAdd(request):
    context = {
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/horaire/index.html', context)

def HoraireEdit(request, horaireId):
    context = {
        'option' : 1 , 
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/horaire/index.html', context)

def HoraireDelete(request, horaireId):
    context = {
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/horaire/index.html', context)

def Delete(request, matiereId):
    context = {
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/etudiant/index.html', context)

def Operations(request, table, operation):
    context = {
        'operation' : operation,
        'table' : table, 
    }
    return render(request,'connection/etudiant/index.html',context)

