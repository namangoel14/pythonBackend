#file = open("demoFile.txt", "r")
#print(file.read())

#file.close()

#fileJson = open("/home/amantya/Downloads/exec_16474/itr_1/logsCollection/ue_logs/imsi_404100589702455.json", "r")
#print(fileJson.read())

#fileJson.close()

with open("demoFile.txt") as file:
    #for x in file:
    #    print(x, end="")
    print(file.readline())
    print("Tell:",file.tell())
    print("Seek:",file.seek(0))
    print("First 5 from starting:", file.read(5))

import json
import os
import subprocess

data = {
    "name": "Naman",
    "age": 25,
    "message": "Python file I/O append"
}

with open("writeFile.json", "w") as fileW:
    json.dump(data, fileW)


with open("writeFile.json", "r") as fileR:
    #data = json.load(fileR)
    print(json.load(fileR))
    #print(data)

if os.path.exists("writeFile.json"):
    os.remove("writeFile.json")
    print("File removed successfully")
else:
    print("File is not present")

os.system("mkdir fileName")
os.system("ls -lrth")

os.rmdir("fileName")

os.system("ls -lrth")


#subprocess.run(["ls", "-lrth"])
