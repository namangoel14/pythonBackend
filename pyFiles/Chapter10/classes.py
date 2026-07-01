class MyClass:
    greet = "Hello Naman"
    def marks(self,mark):
        self.mark = mark
        print(self.mark)
    @staticmethod
    def welcome():
        print("Hello")

class EmptyClass:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hello {self.name}"
    def greet(self):
        return f"Hello {self.name}"

    def welcome(self):
        return f"{self.greet()} ! Welcome!"

class Playlist:

    def __init__(self,name):
        self.name = name
        self.songs = []
    def add_songs(self,song):
        self.songs.append(song)
        print(f"{song}")
    def remove_songs(self,song):
        if song in self.songs:
            self.songs.remove(song)
        print(f"Removed: {song}")
    def show_playlist(self):
        print(f"Playlist - {self.songs}")
        for song in self.songs:
            print(f" - {song}")
    def greet(self):
        return f"This {self.name} is Awesome!!"
    def self1(self):
        message = self.greet()
        print(f"Message: {message} NOICE!")

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age






