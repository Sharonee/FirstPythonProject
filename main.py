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


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Hello World"




















