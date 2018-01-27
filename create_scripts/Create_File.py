from os import path
path = "C:\\Users\\Nikolai\\Desktop\\Name.txt"
file_name = open(path,'w')
question = input('what is your name? ')
file_name.write('answer :'+str(question))
file_name.close()
