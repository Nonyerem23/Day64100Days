
class animal:
  species = None
  name = None
  sound = None

  def __init__(self, name, species, sound): # missed the 'self'
    self.name = name
    self.species = species
    self.sound = sound


  def print(self):
    print(f"""{self.name} is a {self.species} with a {self.sound} sound.""")
dog = animal("Brian", "Canine", "Woof")
dog.print()

def talk(self):
    print((f"{self.name} says {self.sound}"))

class bird(animal): # missed the inheritance from animal

 def __init__(self, color): # missed the 'self'
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color


cow = animal("Ermintrude", "Bo Taurus", "Moo")
print(cow.sound)
#print(cow.color) # no such property in the animal class.

polly = bird("Green")
polly.talk() # inherited method from animal class
print(polly.color)


