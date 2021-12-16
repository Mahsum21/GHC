import datetime
import time
from Connection.models import Personne, Formation, Professeur, Horaire, Matiere 

createPersonne = [ 
	["Sana", "Eleonor", "etudiant", "e.sana@gmail.com", "es"], 
	["Kizmaz", "Mahsum", "etudiant", "mahsumkizmaz@gmail.com", "mk"], 
	["Tcheuyasi", "Isaac", "etudiant", "t.isaac@gmail.com", "it"], 
	["Bakashika", "Jessie", "etudiant", "j.bakashika@gmail.com", "jb"], 
	["Borsen", "Maxime", "etudiant", "m.borsen@gmail.com", "mb"], 
	["dufrane", "allain", "etudiant", "a.dufrane@gmail.com", "ad"] ]

for c in range(len(createPersonne)): 
	# for j in c : 
	try:
		Personne.objects.get(email = createPersonne[c][3], mdp = createPersonne[c][4])
	except:
		Personne.objects.create(nom = createPersonne[c][0], prenom = createPersonne[c][1], fonction = createPersonne[c][2], email = createPersonne[c][3], mdp = createPersonne[c][4])	

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
	["Dupont", "Philip", "professeur", "p.dupont@eqla.be", "dp"], 
	["Piette", "Johnny", "professeur", "j.piette@eqla.be", "pj"], 
	["Goraj", "Sylviane", "professeur", "s.goraj@forem.be", "gs"] ]

for c in range(len(createProfesseur)): 
	try:
		Professeur.objects.get(email = createProfesseur[c][3], mdp = createProfesseur[c][4])
	except:
		Professeur.objects.create(nom = createProfesseur[c][0], prenom = createProfesseur[c][1], fonction = createProfesseur[c][2], email = createProfesseur[c][3], mdp = createProfesseur[c][4])	


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
		
