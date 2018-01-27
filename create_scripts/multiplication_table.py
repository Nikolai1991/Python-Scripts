from os import path

def createFile(dest):

    FileName = "nikolai davidov.txt"

    if not (path.isfile(dest + FileName)):
        f= open(dest + FileName, 'w')
        f.write("")
        for i in range(10):
            for j in range(10):
                f.write("%3d " % (i * j))
            f.write("\n")
        f.close()


if __name__== '__main__':
   #destenaion = "C:\\Users\\Nikolai\\Desktop\\"
    destenaion = '/home/davidov/Desktop/DevOps/test scripts/'
    createFile(destenaion)
    input('Done!!')

