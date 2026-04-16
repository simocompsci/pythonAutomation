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


# Matching Characters from Alternate Groups
# we use the pipe operator to represent the 'or' in the regex eg: 'Cat|Dog'

pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
match = pattern.search('Catch me if you can !! ')
print(match.group())
print(match.group(1))


# In addition to a search() method, Pattern objects have a findall() method.
# While search() will return a Match object of the first matched text in the
# searched string, the findall() method will return the strings of every match
# in the searched string.
# There is one detail you need to keep in mind when using findall(). The
# method returns a list of strings as long as there are no groups in the regular
# expression


pattern = re.compile(r'\d{3}-\d{3}-\d{4}') # This regex has no groups.
print(pattern.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# If there are groups in the regular expression, then findall() will return
# a list of tuples. Each tuple represents a single match, and the tuple has
# strings for each group in the regex.

