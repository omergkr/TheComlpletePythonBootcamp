f = open("new_file.txt", 'w+')
f.write("Here is some text")
f.close()

f = open("new_file2.txt", 'w+')
f.write("Here is some text")
f.close()

# Zipping Files
import zipfile

comp_file = zipfile.ZipFile("comp_file.zip", "w")
comp_file.write("new_file.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()


zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall("extracted_content")


import shutil

directory_to_zip = "C:\\Users\\ÖmerGöker\\PycharmProjects\\TheComlpletePythonBootcamp\\_11_AdvancedPythonModules"
# Creating a zip archive
output_filename = 'example'
# Just fill in the output_filename and the directory to zip
# Note this won't run as is because the variable are undefined
shutil.make_archive(output_filename, 'zip', directory_to_zip)

# Extracting a zip archive
# Notice how the parameter/argument order is slightly different here
shutil.unpack_archive(output_filename, dir_for_extract_result,'zip')
