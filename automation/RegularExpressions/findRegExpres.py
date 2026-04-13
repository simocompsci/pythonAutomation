import re
phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = phone_num_pattern_obj.search('My number is 415-555-4242. ')
print(match_obj.group())


phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #devided it to two groups
mo = phone_re.search('My number is 415-555-4242.')
print(mo.group(1)) # Returns the first group of the matched text
print(mo.group(2)) # Returns the second group of the matched text
print(mo.group(0)) # Returns the full matched text
mo.group()