class student:
  #  pass

   def __init__(self, name, age):   #  Self represent the current object. it lets python object
      self.name =name       
      self.age =age

   def diplay(self):
      print(self.name)
      
      s1=student("Rahul", 23)
      s2=student("Sai", 22)

      s1.display()
      s2.display()