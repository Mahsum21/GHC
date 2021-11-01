
DROP DATABASE IF EXISTS ghcdb;
CREATE DATABASE ghcdb;

/* On Change de base de données */
use ghcdb;

SET FOREIGN_KEY_CHECKS=0;




/* Creation de la Table Genre pour les score. */


DROP TABLE IF EXISTS personnes; 

CREATE TABLE personnes(
    Idpersonne int UNSIGNED AUTO_INCREMENT PRIMARY KEY ,
    nom varchar(255) not null,
    prenom varchar(255) not null,
    email varchar(255) not null,
    fonction varchar(255) not null,
    statut varchar(255) not null,
    mdp varchar(255) not null,
    photoProfil varchar(255),
	dateEnregistrement date
	);

DROP TABLE IF EXISTS matieres; 

CREATE TABLE matieres(
    Idmatiere int UNSIGNED AUTO_INCREMENT PRIMARY KEY ,
    nom varchar(255) not null,
    totalDuration int not null,
    currentDuration int not null,
    dailyDuration int not null
	);


DROP TABLE IF EXISTS professeurs; 

CREATE TABLE professeurs(
    Idprofesseur int UNSIGNED AUTO_INCREMENT PRIMARY KEY ,
    nom varchar(255) not null,
    professeur varchar(255) not null,
    matiere varchar(255) not null
	);


DROP TABLE IF EXISTS formations; 

CREATE TABLE formations(
    Idformation int UNSIGNED AUTO_INCREMENT PRIMARY KEY ,
    nom varchar(255) not null,
    responsable varchar(255) not null,
    lieu varchar(255) not null
	);


DROP TABLE IF EXISTS classes; 

CREATE TABLE classes(
	anneeDeFormation date not null,
	classe varchar(255) not null,
	personne varchar(255) not null
	);


DROP TABLE IF EXISTS horaires; 

CREATE TABLE horaires(
	classe varchar(255) not null,
	joursDeCours date not null,
	matiere varchar(255) not null,
	heureDeDebut time not null,
	heureDeFin time not null,
	specificite varchar(255) not null,
	aEuLieu varchar(255) not null,
	remarque varchar(255) 
	);



INSERT INTO personnes(nom, prenom, email, fonction, statut, mdp, dateEnregistrement)
VALUES('tcheuyassi', 'Isaac', 'test', 'eleve', 'admin', 'test',  '2021/12/12'),
('Kizmaz', 'Mahsum', 'mahsumkizmaz@gmail.com', 'eleve', 'admin', 'test',  '2021/01/11');


select * from personnes;	

INSERT INTO formations(nom, responsable, lieu)
VALUES('Blindcode 4 data', 'Jonny', 'Louvin La Neuv'),



select * from formations;	

