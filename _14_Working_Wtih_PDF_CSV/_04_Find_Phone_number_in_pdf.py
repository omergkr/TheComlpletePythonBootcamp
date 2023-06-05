import PyPDF2
import re

f = open("Find_the_Phone_Number.pdf", "rb")
pdf = PyPDF2.PdfReader(f)
print(len(pdf.pages))

pattern = r"\d[3}"
all_text = ""
for n in range(len(pdf.pages)):
    page = pdf.pages[n]
    page_text = page.extract_text()
    all_text += page_text + " "


print(all_text)
print(re.findall(pattern, all_text))

re.findall(pattern, all_text)
print()
for match in re.finditer(pattern, all_text):
    print(match)



