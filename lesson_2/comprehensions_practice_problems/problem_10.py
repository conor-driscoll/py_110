import random

def uuid_generator():
    UUID_CHARACTERS = '012345789abcdef'
    char_num_list = [8, 4, 4, 4, 12]

    return '-'.join([''.join(random.sample(UUID_CHARACTERS, char_num))
                     for char_num in char_num_list])

print(uuid_generator())