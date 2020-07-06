class CompteBancaire:
   def __init__(self, nom, solde):
      self.nom = nom
      self.solde = solde
      def depot(self, somme):
         self.solde = self.solde + somme
      def retrait(self, somme):
         self.solde = self.solde - somme
      def affiche(self):
         print("Le solde du compte bancaire de ",client," est de ",solde," euros.")

print("Bonjour,")
compte1 = CompteBancaire("Corentin", 3900)
compte1.depot(250)
compte1.retrait(75)
compte1.affiche()
compte2 = CompteBancaire("Phillipe", 1000)
compte2.depot(50)
compte2.affiche()
