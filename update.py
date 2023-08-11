from termcolor import colored
from json import load, dump

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

    for contact in data['contacts']:

        # check if there is a contact with this ID
        if contact['id'] == _id:
            found = True
            break
        
    else:
        print(colored("There is no contact with this ID", color="red"))

    if found == False:
        print(colored("No change was happened!", color="red"))

    else:
        # change contact data
        contact['name'] = input("Enter Name: ")
        contact['phone'] = int(input("Enter Phone Number: "))
        contact['email'] = input("Enter Email: ")

        with open("db.json", "w") as file_obj:

            # dump function write in JSON file
            dump(data, file_obj)

            # TODO: color green
            print(colored(f"Data of contact with ID {_id} updated successfully!", color="green"))
