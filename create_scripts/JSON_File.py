import json
from os import path
path = "C:\\Users\\Nikolai\\Desktop\\Student.txt"
myfile = open(path, mode='w', encoding='Latin-1')

Student1 = {
    'StudentName': "Nikolai Davidov",
    'Score': 90,
    'Experience': ['Python', 'Linux', 'AWS']
}

Student2 = {
    'StudentName': "Zion Davidov",
    'Score': 85,
    'Experience': ['JAVA', 'HTML', 'Python']
}

#Create a List in name mystudents
mystudents = []
mystudents.append(Student1)
mystudents.append(Student2)

#------------ SAVE by JSON --------------

json.dump(mystudents, myfile)

#------------ LOAD by JSON --------------

myfile = open(path, mode='r', encoding='Latin-1')
My_Data = json.load(myfile)

for user in My_Data:
    print("Student Name is: " + str(user['StudentName']))
    print("Student Score is: " + str(user['Score']))
    print("Student Experience: " + str(user['Experience'][:]))
    print('----------------------------------------------\n')
