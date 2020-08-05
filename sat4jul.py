#LIST COMPREHENSION

#FIRST LINE
# lst = []
# for i in range(10):
#     lst.append(i)

#SECOND LINE
#lst = [i for i in range(10)]

#THIRD LINE
#lst = [i for i in range(25) if i >= 5]

#4TH LINE
# lst_lst = [[1,2,3,4,5], [6,7,8], [9,10]]
# lst = [y for x in lst_lst if len(x) < 4 for y in x if y % 2 == 1]

# print(lst)

#FIFTH LINE

# lst_lst = [[1,2,3], [4,5,6], [7,8,9]]

# lst = []
# for x in lst_lst:
#     for y in x:
#         lst.append(y)


#SIXTH LINE
# lst_lst = [[1,2,3], [4,5,6], [7,8,9]]
# lst = [y for x in lst_lst for y in x]
# print(lst)

#READING MULTIPLE FILES
# import os 
# import pandas as pd
# file_list = [f for f in os.listdir('/Users/anielkaaslan/Documents/GitHub/files') if f.endswith('.twbx')]
# data_sets = [pd.read_csv(os.path.join('/Users/anielkaaslan/Documents/GitHub/files', f)) for f in file_list]
# data = pd.concat(data_sets, axis=0)
# data

#DICTS, SETS AND TUPLES

#TUPLES, Same as lists but immutable (can't be changed)
# chocos = ('cocoa', 'milk', 'almond', 'semi-sweet')
# for chocolate in chocos:
#     print(chocolate)
# print(chocos[0])
# print(len(chocos))

#DICTIONARIES
# contacts = {'John': '312-555-1234', 'Paul': '312-555-3123', 'George': '312-555-3333', 'Ringo': '312-555-2222'}
# print(contacts.keys())
# print(contacts.values())
# print(contacts.items())
# for i in contacts.keys():
#      print(i)
# for k, v in contacts.items():
#      print(k+": "+v)

#DICTIONARIES COMPREHENSIONS
# international = {k: "+1-"+v for k, v in contacts.items()}
# for k, v in international.items():
#      print(k+": "+v)

#SETS

# letters = set()
# letters.add('a')
# letters.remove('a')
# print(letters)

# girls = set(['morgan', 'bill', 'pete', 'ray'])
# boys = set(['robert', 'lucas', 'morgan', 'ray'])

# unisex = girls.intersection(boys)
# union_ = boys.union(girls)
# only_boys = boys - girls
# print(only_boys)
# print(unisex)
# print(union_)

#STRING OPERATIONS

# x = 'anal'
# y = 'sex'
# z = [x,y]
# print(' '.join(z))

# a = 'They ate the mystery meat. It tasted like chicken.'

# print(a.split())
# print(a.split('.'))
# print(a.split('m'))


# b = 'There is no business like show business.'
 
# print(b.startswith('T'))
# print(b.startswith('There'))
# print(b.startswith('there'))
# print(b.endswith('.'))
# print(b.endswith('business.'))
# print(b.endswith('Business.'))

# print('like' in b)
# print('business' in b)
# print('Business' in b)

# c = 'shE HaD a maRveLoUs aSsoRtmeNt of PUPPETS.'
 
# print(c.lower())
# print(c.upper())
# print(c.capitalize())
# print(c.title())

#We can also remove any white space from the beginning and end of a string using the strip method. 
# If we want to remove white space from just the beginning, we would use lstrip. If we wanted to remove white space from just the end, we would use rstrip.

# d = ' I have a tendency to leave trailing spaces. '
 
# print(d.strip())
# print(d.lstrip())
# print(d.rstrip())

# e = 'I thought the movie was wonderful!'
 
# print(e.replace('wonderful', 'horrible'))
# print(e.replace('wonderful', 'just OK'))

# \w: Any alphanumeric character.
# \W: Any non-alphanumeric character.
# \d: Any numeric character.
# \D: Any non-numeric character.
# \s: Any whitespace characters.
# \S: Any non-whitespace characters.
# .: Any character except newline (\n).

# import re

# text = 'My neighbor, Mr. Rogers, has 5 dogs.'
# # print(re.findall('[neigh]', text))
# print(re.findall('[\d]', text))
# print(re.findall('[\w]', text))
# print(re.findall('[\S]', text))
# print(re.findall('.', text))

# print(re.split('[0-9]', text))
# print(re.sub('[0-9]', '100', text))

#FUNCTIONS 07/23


# def concat_string(lst):
#     string = ' '.join(lst)
#     return print(string)

# to_string = ['mi', 'familia', 'me', 'ama']

# concat_string(to_string)

# a = 17

# def mult(number, multiplier=5):
#     b = number * multiplier
#     return b

# c = mult(a)

# print(a, c)

# sqr = lambda x: x * x

# def sqr_fnc(x):
#     return print(x * x)

# print(sqr(9))
# print(sqr_fnc(9))

# rest = lambda a,b,c: a - b - c

# print(rest(4,5,6))

# div = lambda num, den: num/den if (den != 0) else 0

# print(div(4,0))

# sqrd = [lambda x: x * x for x in range(2,3)]
# print(sqrd) # returns a lambda object

sqr_d = lambda x: x * x
sq = [sqr_d(x) for x in range(1,10)]
print(sq)

school = ['spanish', 'spanish-latam', 'spanish-europe', 'english', 'english-uk']
space = [(lambda x : x.replace('-', ' ')) (x) for x in school]
last = lambda x: x[-1]

print(sorted(space, key=last))

# Advantages and Disadvantages of Lambda Functions
# Lambda functions have several advantages but also some disadvantages.

# Advantages:

# Lambda functions are concise since mthey only contain one expression.
# Lambda can be passed around without a variable (hence why they are considered anonymous).
# Lambda functions return automatically.
# Disadvantages:

# Sometimes lambda functions can over-complicate and it would be better to use a regular function instead. Particularly, when the expression is complex and may benefit from being separated into multiple lines.
# They use different syntax (for example, if statements have different syntax in lambda functions).