import os
import shutil
from_dir ="C:/Users/240125/Downloads"
to_dir = "C:/Users/240125/Downloads/Project102/Document_Files"

list_of_files= os.listdir(from_dir)
print(list_of_files)


for file_name in list_of_files:
    name,extension =os.path.splitext(file_name)
  

    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 =from_dir+ '/'+file_name

        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name
        if os.path.exists(path2):
            print("Moving" + file_name + ".....")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving" + file_name + "...")
            shutil.move(path1, path3)