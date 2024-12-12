class animal:
    species="dog"
    def __init__(self,breed,color,age):
        self.breed=breed
        self.color=color
        self.age=age

dog1=animal("Bulldog","white",6)
dog2=animal("Beagle","brown",10)
dog3=animal("Dachshund","black",5)
print("{} is a species of {} of breed {} and color is {}".format(dog1.breed,dog1.color,dog1.age))
print("{} is a species of {} of breed {} and color is {}".format(dog2.breed,dog2.color,dog2.age))
print("{} is a species of {} of breed {} and color is {}".format(dog3.breed,dog3.color,dog3.age))