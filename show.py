from termcolor import colored
from json import load

def getDataFormJsonFile(_fileName):

    # with replaces a try-catch block with a concise shorthand
    # using the with statement, the file closes automatically after you’ve processed the file.
    with open(_fileName, "r") as file_obj:

        # load function read the JSON file content
        return load(file_obj)

data = getDataFormJsonFile("db.json")

def showAllData():

    # print formated and colored table
    print(colored("ID:".center(5, " ")      + "|" + 
          "Name:".center(10, " ")           + "|" + 
          "Phone:".center(11, " ")          + "|" + 
          "E-mail:".center(15, " ")
          , color="blue") )
          
    print(colored("-", color="blue") * 41)

    for d in data['contacts']:
        print(f"{d['id']}".center(5, " ")     + "|" + 
              f"{d['name']}".center(10, " ")  + "|" + 
              f"{d['phone']}".center(11, " ") + "|" + 
              f"{d['email']}".center(15, " ") )
