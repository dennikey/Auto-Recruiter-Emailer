import smtplib
from regex_organizer import email_list

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()

# Input the email address and password
conn.login('emailaddress@gmail.com', 'password')

# Text format 1
text1 = '''
Subject: {} Internship Summer 2020 Inquiry \n\n

Dear Mr./Ms.{} {}, 

My name is Dennis Bae, and I am a first year Computer Science student at the University of Waterloo. As I understand that you are the {}
of {}, I am requesting a software developer internship at your company.

As an avid programmer with a strong background in coding, I believe that I am a suitable fit for the company and would highly appreciate any 
opportunity to discuss my qualifications with you in person. For more information, I can send you my resume and transcript.

Regards,
Dennis Bae
'''

# Text format 2
text2 = '''
Subject: {} Internship Summer 2020 Inquiry \n\n

Dear Mr./Ms.{} {}, 

My name is Dennis Bae, and I am a first year Computer Science student at the University of Waterloo.
I am currently looking for a software developer internship at your company, {}. 

As an avid programmer with a strong background in coding, I believe that I am a suitable fit for the company and would highly appreciate any 
opportunity to discuss my qualifications with you in person. For more information, I can send you my resume and transcript.

Regards,
Dennis Bae
'''

for i in email_list:
    if len(email_list[i][1]) == 4:
        # Send email in the text format 1
        company_name = email_list[i][0]
        first_name = email_list[i][1][0]
        last_name = email_list[i][1][1]
        sample = email_list[i][1][2]
        position = sample[1:(len(sample) - 1)]
        employer_email = email_list[i][1][3]
        conn.sendmail('emailaddress@gmail.com', employer_email, text1.format(company_name, first_name, last_name, position, company_name))
    else:
        # Send email in the text format 2
        company_name = email_list[i][0]
        first_name = email_list[i][1][0]
        last_name = email_list[i][1][1]
        employer_email = email_list[i][1][2]
        conn.sendmail('emailaddress@gmail.com', employer_email, text2.format(company_name, first_name, last_name, company_name))

conn.quit()
