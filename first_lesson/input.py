note = '''
input()
syntax :-
        object = input("<Message to display on screen>")
        object  = funcation - message
        the taken input is being stored in object variable
        don't be upset we will dissuss more about variavles in
        upcomming leactures
example :-
        my_name = input("Enter Your Name : )
        print(my_name)
output  :-
        Enter Your Name : Tejas Dixit
        Tejas Dixit

        please don't include the <> symbols ,
        in python you can use double or single quotes to print.
        A) Today , we will learn about how to take input in python
        1. The input funcation will take  string parameter by deafult
        2. Yes, we can take integer input also , but we have to pass in
           int() funcation. '''

input("Lets start lesson Press any key to start")
my_name = input("Enter Your Name : ")
print(my_name)
type_of_data = type(my_name)
print("This is ",type_of_data,"Type of data")
my_age = input("Enter Your Age : ")
print("My Age is :",my_age)
type_of_data = type(my_age)
print("my_age is ",type_of_data,"Type of data")
print("Hey wonder !!! I Entered number but it shows string why ?")
input("Press Any key to next ")
print("Now you can enter the age one's again ")
code = '''my_age = int(input("Enter Your Age: "))
          print(my_age)
          print("myage is ",type(my_age),"type of data")'''

my_age = int(input("Enter Your Age: "))
print(my_age)
print("myage is ",type(my_age),"type of data")
print("Now it shows int confused how is it happen.")
input("For Explenetion press any key")
print("code of following example")
print(code)
print("Explenetion: ")
print(note)
