import mysql.connector as MC

#Il y a 7 étapes pour effectuer des requêtes dans MySql
#
#1. Création d'une connection (connect)
#2. Création d'un curseur à partir de la connexion créee
#3. Création d'une chaîne de requête
#4. Exécution (execute) de la requête à partir du curseur
#5. Valider (Commit) la requête, de la transaction en cours, pour des requêtes de type: INSERT, UPDATE, DELETE, etc. Pas pour un SELECT.
#6. Fermer (close) le curseur
#7. Fermer (close) la connexion

def Connect(): 
	"""Cette fonction crée et retourne un objet de type MysqlConnection
 
	Vu que nous avons presque tous des mots de passes différents, on va effectuer une succession de try except.
	En effet quand une connexion échoue, on réessaie avec un autre mot de passe."""
	try: 
		return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = 'g5gqwagr' )
	except:
		try:
			return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = 'python4life' )
		except:
			try:
				return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = 'elochat' )
			except:
				try:
					return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = 'eleochat' )
				except:
					try: 
						return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = 'Eleochat' )
					except:
						try:
							return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = 'isaac' )
						except:
							try:          
								return MC.connect(host = 'localhost', database='supersimon', user = 'root', password = '@Mcyber66' )
							except MC.Error as error:
								raise Exception(f"Connexion à la DB:{error}")

