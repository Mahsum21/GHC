from datetime import datetime
import time
from Connection.models import Personne, Formation, Professeur, Horaire, Matiere 

createPersonne = [ ["Sana", "Eleonore", "sana.elochat@gmail.com"], ["Kizmaz", "Mahsum", "mahsumkizmaz@gmail.com"], ["Tcheuyasi", "Isaac", "t.isaac@gmail.com"], ["Bakashika", "Jessie", "j.bakashika@gmail.com"], ["Borsen", "Maxime", "m.borsen@gmail.com"], ["dufrane", "allain", "d.alain@gmail.com"] ]

for c in range(len(createPersonne)): 
	# for j in c : 
	try:
		Personne.objects.get(email = createPersonne[c][2])
	except:
		Personne.objects.create(nom = createPersonne[c][0], prenom = createPersonne[c][1], email = createPersonne[c][2])	

createFormation = [ ["Blindcode 4data", "LLN"], ["Blindcode", "Bruxel"] ]

for c in range(len(createFormation)): 
	# for j in c : 
	try:
		Formation.objects.get(nom = createFormation[c][0])
	except:
		Formation.objects.create(nom = createFormation[c][0], lieu = createFormation[c][1], responsable_id = 1)	

createProfesseur = [ ["Dupont", "Philip", "d.philip@eqlas.be"], ["Piette", "Jonny", "p.jonny@eqlas.be"], ["Goraj", "Sylviane", "s.goraj@forem.be"] ]

for c in range(len(createProfesseur)): 
	try:
		Professeur.objects.get(email = createProfesseur[c][2])
	except:
		Professeur.objects.create(nom = createProfesseur[c][0], prenom = createProfesseur[c][1], email = createProfesseur[c][2])	

# createHoraire = [ [Datetime('2021-12-22'), DateTime('00:09:00'), "mysql", "Blindcode 4data"], ['22/12/2021', '00:12:45', "python", "Blindcode 4data"], ['23/12/2021', '00:09:00', "recherche d'emploi", "Blindcode 4data"], ['23/12/2021', '00:12:45', "django", "Blindcode 4data"], ['24/12/2021', '00:09:00', "python", "Blindcode 4data"] ]

# for c in range(len(createHoraire)): 
# 	try:
# 		Horaire.objects.get(joursDeCours = createHoraire[c][0])
# 	except:
# 		Horaire.objects.create(joursDeCours = createHoraire[c][0], heureDeDebut  = createHoraire[c][1], matiere  = 2, formations = 1)	

createMatiere= [ ["mysql", datetime(/second=180000), datetime(/second=36000), datetime(/second=10800), Professeur.objects.get(nom = "Piette")],  ["python", datetime(/second=900000), datetime(/second=360000), datetime(/second=10800), Professeur.objects.get(nom = "Dupont")], ["django", datetime(/second=144000), datetime(/second=72000), datetime(/second=10800), Professeur.objects.get(nom = "Dupont")], ["recherche d'emploi", datetime(/second=54000), datetime(/second=18000), datetime(/second=10800), Professeur.objects.get(nom = "Goraj")] ]
# createMatiere= [ ["mysql", 180000, 36000, 10800, Professeur.objects.get(nom = "Piette")],  ["python", 900000, 360000, 10800, Professeur.objects.get(nom = "Dupont")], ["django", 144000, 72000, 10800, Professeur.objects.get(nom = "Dupont")], ["recherche d'emploi", 54000, 18000, 10800, Professeur.objects.get(nom = "Goraj")] ]
# createMatiere= [ ["mysql", datetime(50:00), datetime("10:00"), datetime(03:00), Professeur.objects.get(nom = "Piette")],  ["python", datetime(250), datetime(100), datetime(03), Professeur.objects.get(nom = "Dupont")], ["django", datetime(40), datetime(20), datetime(03), Professeur.objects.get(nom = "Dupont")], ["recherche d'emploi", datetime(15), datetime(05), datetime(03), Professeur.objects.get(nom = "Goraj")] ]
# timestamp = time.mktime(time.strptime('22:24:46', '%Y-%m-%d %H:%M:%S'))


for c in range(len(createMatiere)): 
	try:
		Matiere.objects.get(nom = createMatiere[c][0])
	except:
		currentMatiere = Matiere.objects.create(nom = createMatiere[c][0], dureeTotale = createMatiere[c][1], dureeEnCour = createMatiere[c][2], dureeQuotidienne = createMatiere[c][3] )	
		currentMatiere.professeur.set(createMatiere[c][4])

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


	