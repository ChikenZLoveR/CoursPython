
class Point:
   def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z
   def ToString(self):
      if self.z == None:
      print("P(",self.x,",",self.y,")")
      else:
      print("P(",self.x,",",self.y,",",self.z,")")
      
