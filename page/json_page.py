import json

class CreduForWatchdog:

    with open('kredu.json', 'r') as config_file:
        config = json.load(config_file)
    email = config['email']
    password = config['password']