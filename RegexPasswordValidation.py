#Codewars Challenge: Regex Password Validation
#Will tell you if input password is strong. To be considered strong it must have:
#at least 1 digit, 6 or more characters, and have upper and lower case characters
import re
regex='Password123'
digitRegex= re.compile(r'\d')
upperRegex= re.compile(r'[A-Z]')
lowerRegex= re.compile(r'[a-z]')
lengthRegex= re.compile(r'.{6,}')
specialRegex= re.compile(r'\W')
spaceRegex= re.compile(r'\s')
if spaceRegex.search(regex) == None and digitRegex.search(regex) != None and upperRegex.search(regex) != None and lowerRegex.search(regex) != None and lengthRegex.search(regex) != None and specialRegex.search(regex) == None:
    print (True)
else:
    print (False)
