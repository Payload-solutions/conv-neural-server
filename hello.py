

# from app.Net.execute_model import execute_model

# execute_model()


import re


with open("regular.txt", "r") as file:
    values = file.read()


values = values.strip("\x08")

print(values)
