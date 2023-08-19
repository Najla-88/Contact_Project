from termcolor import colored
from json import load, dump
from validation import *


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as file_obj:
        # load function read the JSON file content
        return load(file_obj)


data = getDataFormJsonFile("db.json")


def addNewData():
    # get the last id and increase it for the new ID
    id = data["contacts"][-1]["id"] + 1
    validName = False
    validEmail = False
    validPhone = False

    while not validName:
        name = input("Enter Name: ")
        validName = isValidName(name)

    while not validPhone:
        phone = input("Enter Phone Number: ")
        validPhone = isValidPhone(phone)

    while not validEmail:
        email = "".join(input("Enter Email: ").split())
        validEmail = isValidEmail(email)

    contact = {"id": id, "name": name, "phone": phone, "email": email}

    # after get the JSON data add the new contact to them and reright the all file
    # with the updated data
    data["contacts"].append(contact)
    with open("db.json", "w") as file_obj:
        # dump function write in JSON file
        dump(data, file_obj)

        print(colored("Contact added successfully", color="green"))
