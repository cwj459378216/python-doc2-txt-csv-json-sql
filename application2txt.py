import docx2txt
# pip install docx2txt
# extract text
text = docx2txt.process("./application.docx")

print text

# python .\application2txt.py > application.txt
# 手动转换utf-8格式