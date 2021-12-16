from django import template
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect 
# Create your views here.

from Connection.models import Personne, Formation, Professeur, Horaire, Matiere, Message


def Index(request):
    context = {
    }
    return render(request,'connection/index.html',context)

def Horaires(request):
    context = {
    }
    return render(request,'connection/horaires.html',context)

def TchatConnect(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mdp = request.POST.get('mdp')
        personne = Personne.objects.filter(email= email)
        if not personne.exists():
            return redirect('/')
        elif personne[0].mdp == mdp:
            expediteur = Personne.objects.get(email= email)
        else:
            return redirect('/')
    
        datas = Personne.objects.all()
        context = {
            'datas': datas, 
            'expediteur': expediteur, 
        }
        return render(request,'connection/tchat/tchat.html',context)
    return redirect('/')

def Tchat(request, id1=0, id2=0):
    if request.method == 'POST':
        Message.objects.create(
            message = request.POST.get('message'), 
            expediteur = id1, 
            destinataire = id2
        )
    if id1 >0:
        expediteur= Personne.objects.filter(pk = id1)
    if id2 >0:
        destinataire= Personne.objects.filter(pk = id2)
    datas = Personne.objects.all()
    messages = (Message.objects.filter(expediteur=id1, destinataire=id2) | Message.objects.filter(expediteur=id2, destinataire=id1)).order_by('date')
    from datetime import datetime
    context = {
        'datas': datas, 
        'expediteur': expediteur[0], 
        'destinataire': destinataire[0], 
        'messages': messages,
        'test':messages[0].date.strftime('%H:%M:%S')
    }
    return render(request,'connection/tchat/tchat.html',context)

def Admin(request):
    context = {
        'operation' : "",
        'table' : "", 
    }
    return render(request,'connection/admin.html', context)

def Etudiant(request):
    etudiants = Personne.objects.filter(fonction = "etudiant")
    context = {
        'option' : 0 , 
        'datas' : etudiants,
        'item' : "", 
    }
    return render(request,'connection/etudiant/index.html', context)

def EtudiantCreate(request):
    etudiants = Personne.objects.filter(fonction = "etudiant")
    context = {
        'option' : 0 , 
        'datas' : etudiants,
        'item' : "", 
    }
    return render(request,'connection/etudiant/index.html', context)

def EtudiantAdd(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        personne = Personne.objects.filter(email = email, fonction = "etudiant")
        if not personne.exists():
            etudiant = Personne.objects.create(
                nom = request.POST.get('nom'), 
                prenom = request.POST.get('prenom'), 
                email = email, 
                fonction = "etudiant", 
                mdp = request.POST.get('mdp')
            )
    return redirect('/admin/etudiant/')

def EtudiantEdit(request, etudiantId):
    datas = Personne.objects.filter(fonction = "etudiant")
    item = Personne.objects.get(pk = etudiantId, fonction="etudiant")
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
        personne.fonction = "etudiant"
        personne.save()
    return redirect('/admin/etudiant/')

def EtudiantDelete(request, etudiantId):
    if request.method == 'POST': 
        Personne.objects.get(pk = etudiantId).delete()
    return redirect('/admin/etudiant/')

def Professeur(request):
    datas = Personne.objects.filter(fonction = "professeur")
    context = {
        'option' : 0 , 
        'datas' : datas,
        'item' : ""
    }
    return render(request,'connection/professeur/index.html', context)

def ProfesseurCreate(request):
    datas = Personne.objects.filter(fonction = "professeur")
    context = {
        'option' : 0 , 
        'datas' : datas,
        'item' : "", 
    }
    return render(request,'connection/professeur/index.html', context)

def ProfesseurAdd(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        personne = Personne.objects.filter(email = email)
        if not personne.exists():
            Personne.objects.create(
                nom = request.POST.get('nom'), 
                prenom = request.POST.get('prenom'), 
                email = email, 
                fonction = "professeur", 
                mdp = request.POST.get('mdp')
            )
    return redirect('/admin/professeur/')

def ProfesseurEdit(request, professeurId):
    datas = Personne.objects.filter(fonction = "professeur")
    item = Personne.objects.get(pk = professeurId)
    context = {
        'option' : 1 , 
        'datas' : datas,
        'item' : item, 
    }
    return render(request,'connection/professeur/index.html', context)

def ProfesseurUpdate(request, professeurId):
    personne = Personne.objects.get(pk = professeurId)
    if request.method == 'POST':
        personne.nom = request.POST.get('nom')
        personne.prenom = request.POST.get('prenom')
        personne.email = request.POST.get('email')
        personne.mdp = request.POST.get('mdp')
        personne.fonction = "professeur"
        personne.save()
    return redirect('/admin/professeur/')

def ProfesseurDelete(request, professeurId):
    if request.method == 'POST': 
        Personne.objects.get(pk = professeurId).delete()
    return redirect('/admin/professeur/')

# def Matiere(request):
#     datas = Matiere.objects.all()
#     context = {
#         'option' : 0 , 
#         'datas' : datas,
#         'item' : ""
#     }
#     return render(request,'connection/matiere/index.html', context)

# def MatiereCreate(request):
#     datas = Matiere.objects.all()
#     context = {
#         'option' : 0 , 
#         'datas' : datas,
#         'item' : "", 
#     }
#     return render(request,'connection/matiere/index.html', context)

# def MatiereAdd(request):
#     if request.method == 'POST':
#         nomMat = request.POST.get('nom')
#         matiere = Matiere.objects.filter(nom= nomMat)
#         if not matiere.exists():
#             Matiere.objects.create(
#                 nom = request.POST.get('nom'), 
#                 dureeTotale = request.POST.get('prenom'), 
#                 dureeEnCours = request.POST.get('prenom'), 
#                 # dureeQuotidienne = request.POST.get('prenom'),
#                 # professeur = request.POST.get('prenom'),
#             )
#     return redirect('/admin/matiere/')

# def MatiereEdit(request, matiereId):
#     datas = Matiere.objects.all()
#     item = Matiere.objects.get(pk = matiereId)
#     context = {
#         'option' : 1 , 
#         'datas' : datas,
#         'item' : item, 
#     }
#     return render(request,'connection/professeur/index.html', context)

# def MatiereUpdate(request, matiereId):
#     personne = Personne.objects.get(pk = professeurId)
#     if request.method == 'POST':
#         personne.nom = request.POST.get('nom')
#         personne.prenom = request.POST.get('prenom')
#         personne.email = request.POST.get('email')
#         personne.mdp = request.POST.get('mdp')
#         personne.fonction = "professeur"
#         personne.save()
#     return redirect('/admin/professeur/')

# def MatiereDelete(request, matiereId):
#     if request.method == 'POST': 
#         Personne.objects.get(pk = professeurId).delete()
#     return redirect('/admin/professeur/')

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
