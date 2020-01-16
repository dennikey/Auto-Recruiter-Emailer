import docx

#recruiterlist.docx is in the desktop
def getText():
    d = docx.Document('c:\\Users\\Mira\\Desktop\\recruiterlist.docx')
    fulltext = []
    for para in d.paragraphs:
        fulltext.append(para.text)
    return '\n'.join(fulltext)
