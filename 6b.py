import os
import sys
import pathlib
import zipfile

dirName = input("Enter Directory name that you want to backup : ")

if not os.path.isdir(dirName):
    print("Directory", dirName, "doesn't exists")
    sys.exit(0)
    
curDirectory = pathlib.Path(dirName)
   
with zipfile.ZipFile("ex.zip","w") as  f:
   for file_path in curDirectory.rglob("*"):  
     f.write(file_path, arcname=file_path.relative_to(curDirectory))
print(file_path)  

if os.path.isfile("ex.zip"):
    print("created successfully")
else:
    print("Error in creating zip archive")
