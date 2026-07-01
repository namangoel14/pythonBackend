from classes import MyClass, EmptyClass, Playlist, Person

# p1 is the object of class - MyClass from the classes.py file
p1 = MyClass()
print(p1.greet)
print(p1.marks("98"))
print(p1.welcome())
p1.greet = "Hello Nemo"
p1.lastName = "Goel"
print("Updated:",p1.greet,p1.lastName)
print("Last Name:",p1.lastName)

p = EmptyClass("Naman", 27)
#del p
print("result:", p.welcome())
print(p)

ob1 = Playlist("Favoutires")
ob1.add_songs("song1")
ob1.add_songs("song2")
ob1.show_playlist()
ob1.remove_songs("song1")
ob1.show_playlist()
ob1.self1()
#del Playlist.remove_songs

#ob1.remove_songs("song2")

Ob = Person("Mark")
Ob1 = Person("Naman", 27)

print(Ob.name, Ob.age)
print(Ob1.name, Ob1.age)
