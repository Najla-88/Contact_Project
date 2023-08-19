from termcolor import colored
from json import load, dump

from validation import *


def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as file_obj:
        # load function read the JSON file content
        return load(file_obj)


data = getDataFormJsonFile("db.json")


def updateDataFromId():
    # bool var to check if the operation success or not
    found = False
    # while found != True:

    # recive id of the deleted contact from user
    _id = int(input("Enter ID: "))

    for contact in data["contacts"]:
        # check if there is a contact with this ID
        if contact["id"] == _id:
            found = True
            break

    else:
        print(colored("There is no contact with this ID", color="red"))

    if found == False:
        print(colored("No change was happened!", color="red"))

    else:
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

        # change contact data
        contact["name"] = name
        contact["phone"] = phone
        contact["email"] = email

        with open("db.json", "w") as file_obj:
            # dump function write in JSON file
            dump(data, file_obj)

            # TODO: color green
            print(
                colored(
                    f"Data of contact with ID {_id} updated successfully!",
                    color="green",
                )
            )
