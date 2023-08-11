from termcolor import colored
from json import load, dump

def getDataFormJsonFile(_fileName):
    with open(_fileName, "r") as file_obj:

        # load function read the JSON file content
        return load(file_obj)

data = getDataFormJsonFile("db.json")

def delcontactbyName():
    
    # recive id of the deleted contact from user
    _id = int(input("Enter ID: "))

    # bool var to check if the operation success or not
    find = False
    
    # search for the specific contact by its ID
    for contact in data['contacts']:
        if contact['id'] == _id:

            # pop the contact by its id index from the list
            data['contacts'].pop(data['contacts'].index(contact))
            find = True

            # print alert msg after operation success 
            print(colored(f"{_id} -The ID number has been deleted from the database", color="green"))
            break

    with open("db.json", "w") as file_obj:
        
        # dump function write in JSON file
        dump(data, file_obj)

    # check if the operation failed to print alert msg
    if find == False:
        print(colored(f"{_id} -Number ID not found", color="red"))
