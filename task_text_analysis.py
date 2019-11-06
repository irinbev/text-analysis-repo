'''
author = Irina Bevz
'''

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

credentials = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

username = input('Please enter the User Name: ')
password = input('Please enter the Password: ')

# 1.greetings

print('-' * 40)
print('Welcome to the Text Analyser')

# 2 and 3.enter credentials and check for correctness

if credentials.get(username) != password:
    print('Access denied!')
    exit()
elif credentials.get(username) == password:
    print('Access allowed')

print('USERNAME: ', username)

print('-' * 40)

# 4.choose from 3 texts

print('We have 3 texts to be analyzed.')

selection = input('Enter a number btw. 1 and 3 to select: ')
number = 1

if int(selection) in (1, 2, 3) and (selection.isdigit()):
    print('Input is correct')
    text = TEXTS[int(selection) - number]
    print(text)
else:
    print('Please enter a number only from 1 to 3')
    exit()

print('-' * 40)

# 5. calculate statistics

formatted = text.split()

total_words = len(formatted)
print('There are ', total_words, 'words in the selected text.')

capital = sum(map(str.istitle, formatted))
print('There are ', capital, 'title case words')

uppercase = sum(map(str.isupper, formatted))
print('There are ', uppercase, 'upper case words')

lowercase = sum(map(str.islower, formatted))
print('There are ', lowercase, 'lower case words')

numeric = sum(map(str.isnumeric, formatted))
print('There are ', numeric, 'numeric case words')

print('-' * 40)

# 6. calculate a chat: how many words of what length are presented in the text

words_count = {}

while formatted:
    words_lenght = len(formatted.pop())
    words_count[words_lenght] = words_count.get(words_lenght, 0) + 1
print(sorted(words_count.items()))

while words_count:
    info = words_count.popitem()
    print(str(info[0]) + ' ' + str((info[1]) * '*') + ' ' + str(info[1]))

print('-' * 40)

# 7. calculate the sum of all the numeric "words" in the given text

numeric_sum = sum(map(int, filter(str.isnumeric, text.split())))
print('If we summed all the numbers in this text we would get: ', numeric_sum)

print('-' * 40)
