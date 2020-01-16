from word_scraper import getText

# These functions use the information that was gathered from my Word document consisting of the employers' contact information.
# The same regex expressions and methodology can be applied to the information scraped from the Web or PDF files by accessing the pdf_scraper() and web_scraper() files.
# Word_scraper() was chosen because it had the most accuracy where I collected information from a document that I made by copying and pasting contact information.

def list_companies(text_input):
    storage = []
    list_companies = []
    result = ""
    for character in text_input:
        if character != '\n':
            result = result + character
        else: 
            if "@" in result:
                result = ""
            else: 
                storage.append(result)
                result = ""
    
    for elem in storage:
        if elem != "":
            list_companies.append(elem)
    
    return list_companies

def company_splitter(text_input):
    storage = []
    list_by_line = []
    result = ""
    for character in text_input: 
        if character != '\n':
            result = result + character
        else: 
            storage.append(result)
            result = ""

    for elem in storage:
        if elem != "":
            list_by_line.append(elem)

    return list_by_line


def email_grouper(text_input1, text_input2):
    final_list = []
    acc = 0

    for i in range(len(text_input1)):
        sub_list = []
        j = acc

        if i == (len(text_input1) - 1):
            return final_list

        while text_input1[i+1] != text_input2[j]:
            sub_list.append(text_input2[j])
            j += 1
            acc = j

        final_list.append(sub_list)
    
    return final_list

# Import the full Word document text from word_scraper
fulltext = getText()

# Find all the companies in the text
list_of_companies = list_companies(fulltext)

# Divide the text into elements of an array by line
list_by_line = company_splitter(fulltext)

# Pair each company with the list of recruiter emails of random length into a single array
final_list = email_grouper(list_of_companies, list_by_line)
