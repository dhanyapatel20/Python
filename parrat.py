class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age


Blu = parrot("Blu", 11)
woo = parrot("Woo", 11)

print(f"blu is a {Blu.species}")
print(f"woo is a {woo.species}")

print(f"{Blu.name} is {Blu.age} years old")
print(f"{woo.name} is {woo.age} years old")