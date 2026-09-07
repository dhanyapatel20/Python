class family_member:
    def __init__(self, eye_color, height):
        self.eye_color = eye_color
        self.height = height
    def show_traits(self):
        print("Eye color: ", self.eye_color)
        print("Height: ", self.height)

class child(family_member):
    def __init__(self, name, age, eye_color, height):
        self.name = name
        self.age = age
        super().__init__(eye_color, height)
    def show_traits(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        super().show_traits()
    def favorite_hobby(self, hobby):
        print("Favorite hobby: ", hobby)

kid1 = child("alfi", 10, "Brown", "4'5\"")     
kid1.show_traits()
kid1.favorite_hobby("football")
print("is kid1 an instance of child? ", isinstance(kid1, child))