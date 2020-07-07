class Lettre:
   def __init__(self, dest, exp, poids, mode, format):
      self.type = "Lettre"
      self.dest = dest
      self.exp = exp
      self.poids = poids
      self.mode = mode
      self.format = format
   def CalculTimbre(self):
      if self.format == "A4":
         tdb = 2.50
      elif self.format == "A3":
         tdb = 3.50
         montant = tdb + (self.poids / 1000)
      if mode == "express":
         montant = montant * 2
   def ToString(self):
      print(self.type," : ")
      print("Adresse destination : ", self.dest)
      print("Adresse expedition : ", self.exp)
      print("Poids : ", self.poids)
      print("Mode : ", self.mode)
      print("Prix du timbre : ", montant)

class Colis:
   def __init__(self, dest, exp, poids, mode, volume):
      self.type = "Colis"
      self.dest = dest
      self.exp = exp
      self.poids = poids
      self.mode = mode
      self.volume = volume
      montant = 0
   def CalculTimbre(self):
      montant = (0.25 * self.volume) * (self.poids / 1000)
      if mode == "express":
            montant = montant * 2


L1=Lettre("Lille","Paris",80,"normal","A4")
L1.ToString()
C1=Colis("Marrakeche","Barcelone",3500,"express",2.25)
C1.ToString()
