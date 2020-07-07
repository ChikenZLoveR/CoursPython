def __init__(self, jour=, mois=, annee):
   self.jour = jour
   self.mois = mois
   self.annee = annee
   class Personne:
      def __init__(self, nom="Dupont", prenom="Jean", naissance=DateNaissance()):
      self.nom = nom
      self.prenom = prenom
      self.naissance = naissance
      def afficher(self):
         print("Nom:",self.nom,
         "\nPrénom:",self.prenom,
         "\nDate de naissance:")
	 print(self.jour,"/",self.mois,"/",self.année)
   class Employe:
      def __init__(self, personne=Personne(), salaire):
         self.nom = nom
         self.prenom = prenom
         self.naissance = naissance
	 self.personne = personne
         self.salaire = salaire
      def afficher(self):
         self.personne.afficher()
         print("salaire:",self.salaire) 
   class Chef:
      def __init__(self, employe=Employe(), service="service"):
         self.employe = employe
         self.service = service
      def afficher(self):
         self.employe.afficher()
         print("service:",self.service)
