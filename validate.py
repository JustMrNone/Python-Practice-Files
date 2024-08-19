'''email = input("what's your email? (optional)").strip()

if "@" in email and "." in email:
    print("email is valid")
else:
    print("email is invalid")'''
    
#we can set the bar higher by
'''
email = input("what's your email? (optional)").strip()

if "@" in email and "." in email:
    name, domain = email.split("@")
    if name and "." in domain:
        print("email is valid")
    else:
        print("email is invalid")
else: 
    print("email is invalid")
'''

#this can get long and can escalate really quickly 

'''email = input("what's your email? (optional)").strip()

if "@" in email and "." in email:
    name, domain = email.split("@")
    if name and domain.endswith(".edu"):
        print("email is valid")
    else:
        print("email is invalid")
else: 
    print("email is invalid")

'''
'''
import re 

email = input("what's your email? (optional)").strip()

if re.search("@", email):
    print("email is valid")
else:
    print("email is invalid")
    
'''

'''
import re 

email = input("what's your email? (optional)").strip()

if re.search("..*@..*", email):
    print("email is valid")
else:
    print("email is invalid")
    '''
#or


'''import re 

email = input("what's your email? (optional)").strip()

if re.search(r".+@.+\n.edu", email):
    print("email is valid")
else:
    print("email is invalid")
    
'''

import re 

email = input("what's your email? (optional)").strip()

if re.search(r"^.+@.+\n.edu$", email):
    print("email is valid")
else:
    print("email is invalid")
    
