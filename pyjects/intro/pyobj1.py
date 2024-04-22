class Animal:

    def __init__(self, name, age):
        """Initialize objects with name and age attributes"""
        self.name = name
        self.age = age
        self.trained = False

    def run(self):
        print(f"{self.name.title()} is running")

    def walk(self):
        print(f"{self.name.title()} is walking")

    def train_me(self):
        print(f"Finally, {self.name} is trained")
        self.trained = True

class Bird(Animal):

    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type

    def migrate(self):
        print(f"{self.name} is a {self.type} and has migrated south")

    def train_me(self):
        super().train_me()

    def walk(self):
        print(f"Only lazy birds walk")

dog = Animal('Ghost', 9)
print(dog.__dict__)
dog.run()
dog.train_me()
print(dog.__dict__)
bird = Bird("Kush", 2, "Cockatoo")
print(bird.__dict__)
bird.train_me()
bird.walk()