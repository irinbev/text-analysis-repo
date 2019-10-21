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

library = {
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

if library.get(username) != password:
    print('Access denied!')
elif library.get(username) == password:
    print('Access allowed')

print('USERNAME: ', username)
print('PASSWORD: ', password)
print('-' * 40)

# 4.choose from 3 texts

print('We have 3 texts to be analyzed.')

text = int(input('Enter a number btw. 1 and 3 to select: '))
number = TEXTS[text - 1]

if text == 1:
    print(number)
elif text == 2:
    print(number)
elif text == 3:
    print(number)
else:
    print('The number entered is outside the given range')

print('-' * 40)

# 5. calculate statistics

total_words = len(number.split())
print('There are ', total_words, 'words in the selected text.')

capital = sum(map(str.istitle, number.split()))
print('There are ', capital, 'title case words')

uppercase = sum(map(str.isupper, number.split()))
print('There are ', uppercase, 'upper case words')

lowercase = sum(map(str.islower, number.split()))
print('There are ', lowercase, 'lower case words')

numeric = sum(map(str.isnumeric, number.split()))
print('There are ', numeric, 'numeric case words')

print('-' * 40)

# 6. calculate a chat: how many words of what length are presented in the text

formatted = number.split()

words_count = {}

while formatted:
    words = len(formatted.pop())
    words_count[words] = words_count.get(words, 0) + 1
print(sorted(words_count.items()))

while words_count:
    info = words_count.popitem()
    print(str(info[0]) + ' char has length of ' + str(info[1]) + ' word/s')

print('-' * 40)

# 7. calculate the sum of all the numeric "words" in the given text

numeric_sum = sum(map(int, filter(str.isnumeric, number.split())))
print('If we summed all the numbers in this text we would get: ', numeric_sum)

print('-' * 40)
