0-  OUTILS UTILISES:
    - Github (pour le partage de scripts)
    - Zoom (pour les réunions de travaille)
    - Google meet (pour les réunions de travaille)
    - Whatsapp (pour les échanges non planifiés )
    - MYSQL (SGBD de Base de Données )
    - VsCode (Ide = environnement de développement )
    - MYSQLconnector (Module python pour la connection au SGBD MYSQL)
    - Django (Module Python pour le web )
    - Langages : Python , sql, html, css, sass, js


I-  BASE DE DONNEES:

    1-  Creation de la Base de données: 

        Table Personne(Professeurs / Etudiant / Cadres ): 
            -   ID
            -   nom
            -   Prenom
            -   Photo profil
            -   Email
            -   Fonction ( Cadre / Prof / Etudiant / rien )
            -   Statut (consultant / Admin / superAdmin )
            -   Mot de pass (pour tous)

        Table Matières: 
            -   ID
            -   nom 
            -   Durée Totale
            -   Durée Actuelles
            -   Durée Quotidienne

        Table Professeur / Matière :
            -   ID 
            -   Poffesseur 
            -   matière 

        Table Formation (classe) : 
            -   ID
            -   nom
            -   Responsable(Titulaire)
            -   Lieu

        Table Classes/Personnes:   
            -   Année de formation
            -   Classe 
            -   Personnes 

        Table Horaires: 
            -   Classe 
            -   jour (Date)
            -   Matière 
            -   Horaire Début
            -   Horaire Fin
            -   Spécificité (Présentiel ou distanciel)
            -   Statut (à eu lieu ou pas) 
            -   Observations( sera visible à l'affichage)

    2-  Manipulations de manipulation de la base de données (pour les enregistrements de chaque tables ): 
        -   Créations de données 
        -   Lecture des données 
        -   Mise à jour 
        -   Suppresion 


II- Page d'accueil : 
    1-  message de bienvenue et de présentation 
    2-  formulaire de connection ou d'identification ===> vers la page de visualisation 


III- Page de visualisation de l'emploi de temps: 
    1- Affichage : 
        Programme de Formation de [nom de la classe ex "BlindCode4Data"]
        -   semaine du [1 Nomvembre 2021] au [07 Novembre 2021]
            *    [lundi 01] : 
                De [09:00] à [12:00] : [Python] - ([Distantiel]) prof : [philip]  
                De [12:45] à [15:45] : [mysql] - ([Présentiel]) prof : [johnny]  NB: [aucune absence ne sera tolérée]  

            *    [jeudi 04] : 
                De [09:00] à [12:00] : [Python] - ([Distantiel]) prof : [philip]  
                De [12:45] à [15:45] : [mysql] - ([Présentiel]) prof : [johnny]  NB: [aucune absence ne sera tolérée]  

    2- Options de la page d'affichage: 
        a -   Espace parsonnel (web Notes => pour sauvegarde de liens relatives à une matière)
            *   cours ou catégories
            *   intitulé du liens 
            *   commentaire personnel sur le lien 
        b-  Minichat entre les personnes enregistrées dans la bdd.
        c-  bouton Administrer (visible uniquement pour les ou l'administrateur(s). )


IV-    Page d'administration : 
    0-  Design
    pour cette page, 3colonnes sont à envisager : 
        -   gauche: présentant l'objet manipuler ( personnes, matiere , classe )
        -   central: présentant les différentes manipulations à éffectuer sur l'objets choisi à gauche 
        -   droite: présentant la visualisation en temps réel de l'object en cours de manipulation (liste des élèves dans la bd => si objet élève; liste des classes => si objet classe ; Horaie de cours => si objet horaire )
    1-  Ajout / modification / suppresion de : 
        *   PERSONNE 
        *   ELEVE
        *   PROF
        *   CADRE 
        *   MATIERE
        *   CLASSE

    2-  HORAIRE d'une classe (visible uniquement pour le titulaire de la classe et les supers admins)
    

v-  SPLITS (pour gestion de projet): 

    1-  split1 (durée = ):
        *   définition d	es paramètres des tables de la bd (clés, types, etc...)
        *   définition des relations entre les tables
        *   construction de la Bd (fichier sql)
        *   création des enregistrements de test (introduire des enregistrement dans chaque table )
        *   importer la bd et test de celle-ci 
        *   création d'un fichier python (prévoir de les inclure si possible dans l'orienté objet) avec: 
            -   le script de connection à la bd (pour tout le users) => NB: exclure de git via gitignore 
            -   le script de lecture dans une table quelconque prenant encompte les recherches
            -   le script d'ajout d'enregistrement dans une table quelconque 
            -   le script de suppression d'un enregistrement dans une table quelconque 
            -   le scriipt de modification d'un ou plusieurs enregistrement dans une table quelconque. 
            -   le script d'affichage des données récupérées par le script de lecture

    2-  split2(durée = ): 
        *   mise en forme la pages d'acceuil (prendre en compte l'accessibilité) incluant : 
            -   recherche de contenu (text, message d'acceuil, images, video , logo, etc )  
			-	Trouver le logo de Eqla
			-	Demender à Jonny les photos de classe
            -   formulaire de connection 
			-	Adresse mail + mot de passe 
            -   codage en html + css + js de la page d'accueil 
        *   mise en forme de la page d'affichache de l'emploi de temps (accessible) en html, css, js :
		-	Si on a du temps on le présente en tableau 
            -   rechercher du contenu pour cette page (text, photos, video, etc ) 
            -   titres 
            -   simulation d'un emploi de temps sur un ou deux mois  
        *   mise en forme de la page d'administration :
            -   recherche de contenu ()
            -   construction des blocs de gauche, central, droit (avec contenu minimum et représentatif du résultat final)
            -   
        
    3-  split3 (durée = ): 
        *   définition des classes et leurs l'orienté objet 
            -   nom et héritage des classes (leurs roles et leurs pertinence) 
            -   attributs 
            -   méthodes
        *   implémentation et création des classes 
        *   test sur les classes 

    4-  split4 Fusion du Travail (durée = ): 
        *   intégration des méthodes sql dans le projet (django)
        *   intégrations des fichiers html / css / js dans le project django 
        *   Test de toute les fonctionnalités 
 
    5-  split bonus (durée = ): 
        *   implémentation du mini chat
        *   implémentation de l'éspace perso et webnote. 




FO@tc2000x2807@FO
