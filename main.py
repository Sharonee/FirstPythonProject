# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#########################################################################

# def add_subtract_numbers(number_1, number_2):
#     return number_1 + number_2, number_1 - number_2, number_1 * number_2
#
# print(add_subtract_numbers(10, 20))
# print(add_subtract_numbers(number_2=10, number_1=20))

################################ File Handling

# f = open("test.txt", "a")
# f.write("Adding some content to the file.\n")
# f.close()
#
# def add_link_to_file(link: str):
#     f = open("test.txt", "a")
#     f.write(f"{link}\n")
#     f.close()
#
# add_link_to_file("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#
# f = open("test.txt", "r")
# print(f.read())


#################################


# from fastapi import FastAPI
# app = FastAPI()
#
# @app.get("/")
# def home():
#     return "Hello World"


###### Classes ##############

class Animal:
     # fur_color = "Black"
     friends = []


     def __init__(self, height, weight): # To initialize the class
        self.height = height
        self.weight = weight
        self._private_var = "This is a private variable"
        self.__secret_var = "This is a secret variable"

     def print_height_weight(self):
        print(f"Height: {self.height} and Weight: {self.weight}")

     def get_height(self):
         return self.height

     def get_weight(self):
         return self.weight

     def get_fur_color(self):
        return self.fur_color

     def get_friend(self):
         return self.friends

     def set_fur_color(self, color):
         self.fur_color = color

     def set_height(self, height):
         self.height = height

     def set_weight(self, weight):
         self.weight = weight



# animal_1 = Animal(8, 70)
# animal_2 = Animal(6, 50)
#
# # animal_1.print_height_weight()
# # animal_2.print_height_weight()
#
# animal_1.friends.append("Jerry")
#
# print(animal_1.get_height(), animal_1.get_friend())
# print(animal_2.get_weight())
# print(animal_1.get_fur_color())
# print(animal_1._private_var)

#############Calss Inheriting ##############################

class Dog(Animal):
     def __init__(self,height, weight, fur_color):
        self.fur_color = fur_color
        super().__init__(height, weight)

     @staticmethod
     def greet(greeting):
        print(f"{greeting}")



sample_dog = Dog(5, 20, "Brown")
print(sample_dog.height, sample_dog.weight, sample_dog.fur_color)
sample_dog.greet("Woof")





















