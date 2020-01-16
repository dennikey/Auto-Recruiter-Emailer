import re
from organizer import final_list

# Possible Contact Information Format 1
email1Regex = re.compile(r'''
([\w-]+)                        # first name
\s
([\w-]+)                        # last name
\s
([][\w\s]+)                     # position
\:\s
([a-zA-Z0-9_.+-]+               # email
@                           
[a-zA-Z0-9_.+]+)
''', re.VERBOSE)

# Possible Contact Information Format 2
email2Regex = re.compile(r'''
([\w-]+)                        # first name
\s
([\w-]+)                        # last name
\:\s
([a-zA-Z0-9_.+-]+               # email
@                           
[a-zA-Z0-9_.+]+)
''', re.VERBOSE)

# Possible Contact Information Format 3
email3Regex = re.compile(r'''
([\w-]+)                        # first name
\s
([\w-]+)                        # last name
\s
[-–]
\s
([a-zA-Z0-9_.+-]+               # email
@                           
[a-zA-Z0-9_.+]+)
''', re.VERBOSE)

def email_splitter(text_input):
    test_list = []
    for i in range(len(text_input)):
        for j in range(1, len(text_input[i])):
            if email1Regex.search(text_input[i][j]) != None:
                sample_list = [text_input[i][0]]
                mo = email1Regex.findall(text_input[i][j])
                for elem in mo:
                    sample_list.append(elem)
                test_list.append(sample_list)
            elif email2Regex.search(text_input[i][j]) != None:
                sample_list = [text_input[i][0]]
                mo = email2Regex.findall(text_input[i][j])
                for elem in mo:
                    sample_list.append(elem)
                test_list.append(sample_list)
            elif email3Regex.search(text_input[i][j]) != None:
                sample_list = [text_input[i][0]]
                mo = email3Regex.findall(text_input[i][j])
                for elem in mo:
                    sample_list.append(elem)
                test_list.append(sample_list)
            else:
                test_list.append("")

    email_list = []

    for i in test_list:
        if i != "":
            email_list.append(i)
    
    return email_list
    
# Successfully retrieved and organized 106 out of 115 contact info (there were some discrepancies)!
email_list = email_splitter(final_list)
print(email_list[0][1][3])

'''
print(email1Regex.findall('Nicole Malagon [Tech Recruiter]: nicole.malagon@addepar.com'))
print(email2Regex.findall('Leah Busse-Geagan: L.busse-geagan@medium.com'))
print(email3Regex.findall('Janelle Saavedra - janelle_saavedra@apple.com'))
print(email3Regex.findall('Nathan Lim – nlim@apple.com'))
'''
