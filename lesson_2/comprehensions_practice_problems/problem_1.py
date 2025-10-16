munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# cum_male_age = 0

# for nested_dict in munsters.values():
#     if nested_dict['gender'] == 'male':
#         cum_male_age += nested_dict['age']

# print(cum_male_age)


print(sum([nested_dict['age'] for nested_dict in munsters.values() 
                              if nested_dict['gender'] == 'male']))