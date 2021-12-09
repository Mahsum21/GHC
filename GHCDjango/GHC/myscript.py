from Connection.models import Personne, Formation, Professeur, Horaire, Matiere 

createPersonne = [ ["Sana", "Eleonore", "sana.elochat@gmail.com"], ["Kizmaz", "Mahsum", "mahsumkizmaz@gmail.com"], ["Tcheuyasi", "Isaac", "t.isaac@gmail.com"], ["Dupont", "Philip", "p.dupont@eqlas.be"], ["Piette", "Jonny", "j.piette@eqlas.be"], ["dufrane", "allain", "d.alain@gmail.com"] ]

for c in range(len(createPersonne)): 
	# for j in c : 
	try:
		Personne.objects.get(email = createPersonne[c][2])
	except:
		Personne.objects.create(nom = createPersonne[c][0], prenom = createPersonne[c][1], email = createPersonne[c][2])	

# for s in series: 
#     try :
#         maSerie = Serie.objects.get(title = s)
#     except:
#         maSerie = Serie.objects.create(title= s )
#     idx = series.index(s)
#     auts = auteurs[idx]
#     maSerie.picture = urls[idx]
#     maSerie.save()
#     for j in auts: 
#         aut = Creator.objects.get(name = j )
#         maSerie.creators.add(aut)


# #  select myfirstapp_Serie.title, myfirstapp_Creator.name from myfirstapp_Serie_creators 
# #  inner join myfirstapp_Serie on   myfirstapp_Serie_creators.serie_id = myfirstapp_Serie.title 
# #  inner join myfirstapp_creator  on myfirstapp_Serie_creators.creator_id = myfirstapp_Creator.name;


	