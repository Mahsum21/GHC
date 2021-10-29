import datetime
from connexion import *
# _req = "ORDER BY score DESC Limit 10"
def GetData(_table, _reqEnd = ""):
	""" Récupère tous les enregistrements d'une table spécifique de la Base de données"""
	try:
		cnx = Connect()
		curseur = cnx.cursor()
		curseur.execute(f"select * from {_table} {_reqEnd}")
		data = curseur.fetchall()
		curseur.close()
		cnx.close()
		return data
	except Exception as erreur:
		print("Une erreur est survenue dans la fonction GetData :", erreur)

def AddData(_req, _data = []):
	""" fonction qui ajoute un enregistrement à la BD """
	# req = """INSERT INTO films (titre, realisateur, pays, boxoffice, DateSortie, Genre) VALUES (%s, %s, %s, %s, %s, %s)"
    # data = (_filmToSave[0], _filmToSave[1], _filmToSave[2], _filmToSave[3], _filmToSave[4], _filmToSave[5])
	try:
		cnx = Connect()
		curseur = cnx.cursor()
		curseur.execute(_req, _data )
		cnx.commit()
		curseur.close()
		cnx.close()
	except Exception as erreur:
		print("Une erreur est survenue dans AddData :", erreur)

def UpdateData(_req, _data = []):
	"""met à jour un enregistrement dans une table quelconque"""
	# req = """UPDATE films SET Titre = %s, realisateur= %s, pays= %s, boxoffice= %s, DateSortie= %s, Genre= %s WHERE idfilm = %s"""
    # data = ( _filmToSave[0], _filmToSave[1], _filmToSave[2], _filmToSave[3], _filmToSave[4], _filmToSave[5], _id)
	try:
		cnx = Connect()
		curseur = cnx.cursor()
		curseur.execute(_req, _data )
		cnx.commit()
		curseur.close()
		cnx.close()
	except Exception as erreur:
		print("Une erreur est survenue dans UpdateData :", erreur)

def DeleteData(_req, _data = []):
	"""supprime un enregistrement dans une table quelconque de la BD"""
	try:
		cnx = Connect()
		curseur = cnx.cursor()
		curseur.execute("""UPDATE films SET deleted = 1 where idfilm = %s """ % ( _filmToDelete[int(_userInput)] ))
		cnx.commit()
		curseur.close()
		cnx.close()
	except Exception as erreur:
		print("Une erreur est survenue dans UpdateData :", erreur)

