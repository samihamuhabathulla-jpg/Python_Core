import re 
text="Alan Turing was a pioneer of theoretical computer scienece and Turing artificial intelligence. he was born on 23 june 1912 in maida vale, London"
res=re.search('computer',text)
print("Match object ={}",format(res))
print("--"*30)
print("group method output =",res.group())
print("--"*30)
print("start method output=",res.start())
print("--"*30)
print("end method output=",res.end())
print("--"*30)
print("span method output=",res.re)
print("--"*30)
print("string attribute output=",res.string)
print("--"*30)
text=r'search\\in the string'
res=re.search(r"\\",text)
print("With r as prefix=",res)

import re 
pattern =r'\b\w+ing\b'
text="Walking and talking are important activities."
match_result=re.search(pattern,text)
if match_result:
    print("Match found :",match_result.group())
else:
    print("No match found")

    import re 
    email_pattern= r'\b[A-Za-z0-%+-]+\[A-Z[a-z]{2,}]b'
    text_with_emails="Contect us at trainer@smartcliff.in or gayatri.manoj@smartcliff.in"
    email_found = re.findall(email_pattern,text_with_emails)
    if email_found:
        print("Email addresses found:",email_found)
    else:
        print("No email addresses found")


    import re 
    email_pattern= r'\b[A-Za-z0-9._%+-]+@[A-Z[a-z]{2,}]b'
    text_with_emails="Contact us at trainer@smartcliff.in or gayatri.manoj@smartcliff.in"
    email_found = re.findall(email_pattern,text_with_emails)
    if email_found:
        print("Email addresses found:",email_found)
    else:
        print("No email addresses found")
