import re 
email_pattern= r'\b[A-Za-z0-9._%+-]+@[A-Z[a-z]{2,}]b'
text_with_emails="Contact us at trainer@smartcliff.in or gayatri.manoj@smartcliff.in"
email_found = re.findall(email_pattern,text_with_emails)
if email_found:
     print("Email addresses found:",email_found)
else:
     print("No email addresses found")


