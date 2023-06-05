# f = open("practice.txt3", "w+")
# f.write("This is a testing string")
# f.close()

import os
print(os.getcwd())
print(os.listdir())
print(os.listdir("C:\\Users\\ÖmerGöker"))

import shutil

# shutil.move("practice3.txt", "C:\\Users\\ÖmerGöker\\PycharmProjects\\TheComlpletePythonBootcamp\\_10_Generators")
# shutil.move("C:\\Users\\ÖmerGöker\\PycharmProjects\\TheComlpletePythonBootcamp\\_10_Generators\\practice3.txt", os.getcwd() )

# os.unlink()
# os.rmdir()
# shutil.rmtree()

"""All of these methods can not be reversed! Which means if you make a mistake you won't be able to recover the file. 
Instead we will use the send2trash module. 
A safer alternative that sends deleted files to the trash bin instead of permanent removal. ___

Install the send2trash module with:

pip install send2trash"""

for folder, sub_folder, files in os.walk("C:\\Users\\ÖmerGöker\\PycharmProjects\\TheComlpletePythonBootcamp"):
    print(folder)
    print(sub_folder)
    print(files)

