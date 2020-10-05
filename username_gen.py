import random
## Imports ## 

def generate_username():
    '''
    generates usernames
    '''
    with open(r'names.txt') as names:
        names = names.read().replace('\n', ' ')
        names = names.split(' ')
        username = random.choice(names) + str(random.randint(1, 999)) ## finds a username from the list generated above
        return username




