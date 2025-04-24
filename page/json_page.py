import json


class Credu:

    with open('kredu.json', 'r') as config_file:
        config = json.load(config_file)
    email = config['email']
    password = config['password']
    login_to_broker_ePRO24 = config['login_to_broker_ePRO24']
    password_to_broker = config['password_to_broker']
    login_to_broker_MQTT = config['login_to_broker_MQTT']
    name_opc = config['name_opc']
    url_opc = config['url_opc']
    login_OPC = config['login_OPC']
    password_OPC = config['password_OPC']


class DateForTesting:

    name_new_project = 'Testing1'
    description_new_project = 'Description1'

    name_gateway_in_project = 'TEST name'
    serial_number_gateway = '9569194B'

    name_dashbord = 'test'