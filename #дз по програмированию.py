#1
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}

print(min(my_dict) + max(my_dict))
#2
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '‪+7998-676-2532‬', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '‪+7948-799-2434‬', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '‪+7995-600-9080‬', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
names_ending_in_8 = []
for user in users:
    phone_number = user['phone']
    if phone_number.endswith('8'):
        names_ending_in_8.append(user['name'])
names_ending_in_8.sort()
print(' '.join(names_ending_in_8))
#3
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '‪+7998-676-2532‬', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '‪+7948-799-2434‬'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '‪+7995-600-9080‬', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
no_email_users = []
for user in users:
    if 'email' not in user or user['email'] == '':
        no_email_users.append(user['name'])
no_email_users.sort()
print(' '.join(no_email_users))
#4
digit_map = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
number_str = input()
result_str = ' '.join(digit_map[digit] for digit in number_str)
print(result_str)
#5
courses = {
    'CS101': ['3004', 'Хайнс', '8:00'],
    'CS102': ['4501', 'Альварадо', '9:00'],
    'CS103': ['6755', 'Рич', '10:00'],
    'NT110': ['1244', 'Берк', '11:00'],
    'CM241': ['1411', 'Ли', '13:00']}
course_number = input()
if course_number in courses:
    room, instructor, time = courses[course_number]
    print(f"{course_number}: {room}, {instructor}, {time}")
else:
    print(f"Курс с номером {course_number} не найден.")
#6
keypad_map = {
    ' ': '0',

    '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',

    'A': '2', 'B': '22', 'C': '222',
    'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444',
    'J': '5', 'K': '55', 'L': '555',
    'M': '6', 'N': '66', 'O': '666',
    'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
    'T': '8', 'U': '88', 'V': '888',
    'W': '9', 'X': '99', 'Y': '999', 'Z': '9999'}
input_text = input().upper()
output_sequence = ""

for char in input_text:
    if char in keypad_map:
        output_sequence += keypad_map[char]
print(output_sequence)
#7
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
input_message = input()
processed_message = input_message.upper()
encoded_parts = []
for char in processed_message:
    if char in MORSE_CODE:
        morse_code = MORSE_CODE[char]
        encoded_parts.append(morse_code)
output_message = " ".join(encoded_parts)
print(output_message)
#8
result = {}
for i in range(11, 16):
    result[i] = i * i
#9
dict1 = {'a': 100,
'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm':
230}
dict2 = {'a': 300,
'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = {}
result.update(dict1)
for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value
#10
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for char in text:
    result[char] = result.get(char, 0) + 1
#11
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

words = s.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
max_count = -1
most_frequent_word = ""
for word, count in word_counts.items():
    if count > max_count:
        max_count = count
        most_frequent_word = word
    elif count == max_count:
        if word < most_frequent_word:
            most_frequent_word = word
print(most_frequent_word)
#12
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

for pet_name, owner_first, owner_last, owner_age in pets:
    owner_key = (owner_first, owner_last, owner_age)
    pet_list = result.setdefault(owner_key, [])
    pet_list.append(pet_name)
#13
input_text = input()
punctuation = ".,!?:;-"
cleaned_text = input_text.lower()
for char in punctuation:
    cleaned_text = cleaned_text.replace(char, ' ')
words = [word for word in cleaned_text.split() if word]
if not words:
    print("")
else:
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    min_count = float('inf')
    rarest_word = None
    for word, count in word_counts.items():
        if count < min_count:
            min_count = count
            rarest_word = word
        elif count == min_count:
            if rarest_word is None or word < rarest_word:
                rarest_word = word
    print(rarest_word)
#14
input_text = input()
identifiers = input_text.split()
seen_counts = {}
corrected_identifiers = []

for identifier in identifiers:
    if identifier not in seen_counts:
        corrected_identifiers.append(identifier)
        seen_counts[identifier] = 0
    else:
        seen_counts[identifier] += 1
        n_suffix = str(seen_counts[identifier])

        new_identifier = identifier + "_" + n_suffix

        corrected_identifiers.append(new_identifier)
output_string = " ".join(corrected_identifiers)
print(output_string)