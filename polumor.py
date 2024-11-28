class cat:
    def __init__(self,name,age):

        self.name=name
        self.age=age

    def intro(self):
        print(f"i am a cat my name is {self.name} my age is {self.age}")

    def make_sound(self):
        print("meow")



class dog:
    def __init__(self,name,age):

        self.name=name
        self.age=age

    def intro(self):
        print(f"i am a dog my name is {self.name} my age is {self.age}")

    def make_sound(self):
        print("bark")


cat1=cat("otre",2.3)
dog1=dog("tyon",7)

for animal in (cat1,dog1):
    animal.make_sound()
    animal.intro()