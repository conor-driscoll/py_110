munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for name, nested_dict in munsters.items():
    for index, data in enumerate(nested_dict.values()):
        if index == 0:
            age = data
        if index == 1:
            gender = data
    print(f'{name} is a {age}-year-old {gender}.')