class Person:
    def __init__(
        self,
        name: str = "Tejas",
        age: int = 20,
    ) -> None:
        self.name = name
        self.age = age

    def myname(self) -> None:
        print("My Name is :" + self.name)


# created Objets
# First Object
p1 = Person()
p1.myname()

# Second Object
p2 = Person("soham", 22)
print(p2.age)
p2.myname()
# This Will Prints name of person
del p2.age
# `del` Key Word is used to del object
