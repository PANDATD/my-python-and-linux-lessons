#!/bin/usr/python3.10


class Person:
    def __init__(
        self,
        fname: str,
        lname: str,
    ) -> None:
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


p1 = Person("Tejas", "Dixit")
p1.printname()


class Student(Person):
    def __init__(self, fname: str, lname: str, year: int) -> None:
        super().__init__(fname, lname)
        """Where as Super Keyword is helps child class inherit all method from Praent class"""
        self.graduationYear = year

    def printstdname(self) -> None:
        print(f"Name:{self.fname + self.lname} Graduation Year: {self.graduationYear}")


s1 = Student("Vignesh", "Gawali", 2019)
s1.printstdname()
