import datetime
import time
from Connection.models import Personne, Formation, Professeur, Horaire, Matiere 

createPersonne = [ 
	["Sana", "Eleonore", "etudiant", "e.sana@gmail.com"], 
	["Kizmaz", "Mahsum", "mahsumkizmaz@gmail.com"], 
	["Tcheuyasi", "Isaac", "t.isaac@gmail.com"], 
	["Bakashika", "Jessie", "j.bakashika@gmail.com"], 
	["Borsen", "Maxime", "m.borsen@gmail.com"], 
	["dufrane", "allain", "d.alain@gmail.com"] ]

for c in range(len(createPersonne)): 
	# for j in c : 
	try:
		Personne.objects.get(email = createPersonne[c][2])
	except:
		Personne.objects.create(nom = createPersonne[c][0], prenom = createPersonne[c][1], email = createPersonne[c][2])	

createFormation = [ 
	["Blindcode 4data", "LLN"], 
	["Blindcode", "Bruxel"] ]

for c in range(len(createFormation)): 
	# for j in c : 
	try:
		Formation.objects.get(nom = createFormation[c][0])
	except:
		Formation.objects.create(nom = createFormation[c][0], lieu = createFormation[c][1], responsable_id = 1)	

createProfesseur = [ 
	["Dupont", "Philip", "d.philip@eqlas.be"], 
	["Piette", "Jonny", "p.jonny@eqlas.be"], 
	["Goraj", "Sylviane", "s.goraj@forem.be"] ]

for c in range(len(createProfesseur)): 
	try:
		Professeur.objects.get(email = createProfesseur[c][2])
	except:
		Professeur.objects.create(nom = createProfesseur[c][0], prenom = createProfesseur[c][1], email = createProfesseur[c][2])	

createHoraire = [ 
['2021-12-22', '00:09:00', Matiere.objects.get(nom="mysql").id, "Blindcode 4data"], 
['2021-12-22', '00:12:45', Matiere.objects.get(nom="python").id, "Blindcode 4data"], 
['2021-12-23', '00:09:00', Matiere.objects.get(nom="recherche d'emploi").id, "Blindcode 4data"], 
['2021-12-23', '00:12:45', Matiere.objects.get(nom="django").id, "Blindcode 4data"], 
['2021-12-24', '00:09:00', Matiere.objects.get(nom="python").id, "Blindcode 4data"] ]

for c in range(len(createHoraire)): 
	try:
		Horaire.objects.get(joursDeCours = createHoraire[c][0], matiere = createHoraire[c][2])
	except:
		currentHoraire = Horaire.objects.create(joursDeCours = createHoraire[c][0], heureDeDebut  = createHoraire[c][1], matiere_id = createHoraire[c][2])	
		# currentHoraire.matiere.add(createHoraire[c][2])


createMatiere= [ 
	["mysql", datetime.timedelta(hours = 18000), datetime.timedelta(hours =36000), datetime.timedelta(hours =10800), Professeur.objects.get(nom = "Piette")],  
["python", datetime.timedelta(hours =900000), datetime.timedelta(hours =360000), datetime.timedelta(hours =10800), Professeur.objects.get(nom = "Dupont")], 
["django",datetime.timedelta(hours =144000), datetime.timedelta(hours =72000), datetime.timedelta(hours =10800), Professeur.objects.get(nom = "Dupont")], 
["recherche d'emploi", datetime.timedelta(hours =54000), datetime.timedelta(hours =18000), datetime.timedelta(hours =10800), Professeur.objects.get(nom = "Goraj")] ]

# createMatiere= [ 
# 	["mysql", datetime.timedelta(hours = 50:00), datetime.timedelta(hours = 10:00), datetime.timedelta(hours = 03:00), Professeur.objects.get(nom = "Piette")],  
# 	["python", datetime.timedelta(hours = 250:00), datetime.timedelta(hours = 100:00), datetime.timedelta(hours = 03:00), Professeur.objects.get(nom = "Dupont")], 
# 	["django", datetime.timedelta(hours = 40:00), datetime.timedelta(hours = 20:00), datetime.timedelta(hours = 03:00), Professeur.objects.get(nom = "Dupont")], 
# 	["recherche d'emploi", datetime.timedelta(hours = 15:00), datetime.timedelta(hours = 05:00), datetime.timedelta(hours = 03:00), Professeur.objects.get(nom = "Goraj")] ]

for c in range(len(createMatiere)): 
	try:
		Matiere.objects.get(nom = createMatiere[c][0])
	except:
		currentMatiere = Matiere.objects.create(nom = createMatiere[c][0], dureeTotale = createMatiere[c][1], dureeEnCour = createMatiere[c][2], dureeQuotidienne = createMatiere[c][3] )	
		currentMatiere.professeur.add(createMatiere[c][4])

# # for s in series: 
# #     try :
# #         maSerie = Serie.objects.get(title = s)
# #     except:
# #         maSerie = Serie.objects.create(title= s )
# #     idx = series.index(s)
# #     auts = auteurs[idx]
# #     maSerie.picture = urls[idx]
# #     maSerie.save()
# #     for j in auts: 
# #         aut = Creator.objects.get(name = j )
# #         maSerie.creators.add(aut)


# # #  select myfirstapp_Serie.title, myfirstapp_Creator.name from myfirstapp_Serie_creators 
# # #  inner join myfirstapp_Serie on   myfirstapp_Serie_creators.serie_id = myfirstapp_Serie.title 
# # #  inner join myfirstapp_creator  on myfirstapp_Serie_creators.creator_id = myfirstapp_Creator.name;


	