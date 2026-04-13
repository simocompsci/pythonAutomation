import re
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242. ')
print(match_obj.group())


phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #devided it to two groups
mo = phone_re.search('My number is 415-555-4242.')
print(mo.group(1)) # Returns the first group of the matched text
print(mo.group(2)) # Returns the second group of the matched text
print(mo.group(0)) # Returns the full matched text
print(mo.groups()) # retrieve all groups at ounce

area_code, main_number = mo.groups()
print(area_code)
print(main_number)

pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') # using escape characters to escape the parenthesis
mo = pattern.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))

# in regular expressions these chars : # $ & ( ) * + - . ? [ \ ] ^ { | } ~
# have special meaning , that 's why we need to escape them

# If you want to detect these characters as part of your text pattern, you
# need to escape them with a backslash:
# \# \$ \& \( \) \* \+ \- \. \? \[ \\ \] \^ \{ \| \} \~